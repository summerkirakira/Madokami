<script lang="ts">
import SettingsItem from './SettingsItem.vue';
import { getSettings } from '@/services/settingService';
import { getPluginByNamespace } from '@/utils/plugin';
import { getPluginInfos } from '@/services/pluginService';
import { type SettingRecord } from '@/client';
import { addSetting } from '@/services/settingService';
import { useMessageStore } from '@/stores/message';
import WebSettingsContainer from './WebSettingsContainer.vue';
import { getSchedules } from '@/services/scheduleService';
import { type Plugin } from '@/client';
import { convertCronToMinutes, convertMinutesToCron } from '@/utils/formatter';
import { updateSchedule, restartScheduler } from '@/services/scheduleService';

interface Setting extends SettingRecord {
  name: string | undefined;
  tasks: { id: number, name: string, interval: number }[];
}

export default {
  components: {
    SettingsItem,
    WebSettingsContainer
  },
  mounted() {
    this.fetchSettings();
  },
  setup() {
    return {
      messageStore: useMessageStore(),
    };
  },
  data() {
    return {
      settings: [] as Setting[]
    };
  },
  methods: {
    getScheduleByNamespace(schedules:Plugin[], namespace: string) {
      return schedules.find(schedule => schedule.namespace === namespace);
    },
    async fetchSchedules() {
      let schedules = (await getSchedules()).data?.data;
      if (schedules === undefined || schedules === null) {
        return;
      }
      return schedules;
    },
    async fetchSettings() {
        let settingsRaw = (await getSettings()).data.data  as Setting[] | undefined;
        if (settingsRaw === undefined || settingsRaw === null) {
           return;
        }
        let pluginInfos = (await getPluginInfos()).data.data;
        if (pluginInfos === null || pluginInfos === undefined) {
           return;
        }
        let schedules = await this.fetchSchedules();
        for (let setting of settingsRaw) {
            let plugin = getPluginByNamespace(pluginInfos, setting.namespace);
            if (plugin === undefined) {
                setting.name = "默认设置";
            } else {
                setting.name = plugin.name;
            }
            if (schedules === undefined) {
                continue;
            }
            let schedule = this.getScheduleByNamespace(schedules, setting.namespace);
            if (schedule === undefined) {
                setting.tasks = [];
                continue;
            }
            let tasks: { id: number, name: string, interval: number }[] = [];
            schedule.tasks.forEach(task => {
              let interval = convertCronToMinutes(task.cron_str);
              if (interval === null) {
                return;
              }
              tasks.push({
                  id: task.id,
                  name: task.name,
                  interval: interval
              });
            });
            setting.tasks = tasks;
        }
        this.settings = settingsRaw as Setting[];
    },
    async updateSettings() {
      // console.log(this.settings)
      this.settings.forEach(config => {
        config.settings.forEach(async setting => {
          await addSetting(setting.key, setting.value)
        });
        config.tasks.forEach(async task => {
          await updateSchedule(task.id, convertMinutesToCron(task.interval));
        });
      })
      this.messageStore.setMessage("设置已保存", "success")
      setTimeout(() => {
        restartScheduler();
      }, 5000);
    },
  },
};
</script>

<template>
  <div>
    <WebSettingsContainer @update:settings="updateSettings"/>
    <SettingsItem class="setting-item" v-for="setting in settings" :key="setting.namespace" :pluginName="setting.name!" :settings="setting.settings" :tasks="setting.tasks"/>
  </div>
</template>

<style scoped>
.setting-item {
  margin-top: 15px;
}
</style>