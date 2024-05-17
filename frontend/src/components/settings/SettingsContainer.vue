<script lang="ts">
import SettingsItem from './SettingsItem.vue';
import { getSettings } from '@/services/settingService';
import { getPluginByNamespace } from '@/utils/plugin';
import { getPluginInfos } from '@/services/pluginService';
import { type SettingRecord } from '@/client';
import { addSetting } from '@/services/settingService';
import { useMessageStore } from '@/stores/message';
import WebSettingsContainer from './WebSettingsContainer.vue';

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
      settings: [] as SettingRecord[],
    };
  },
  methods: {
    async fetchSettings() {
        let settingsRaw = (await getSettings()).data.data;
        if (settingsRaw === undefined || settingsRaw === null) {
           return;
        }
        let pluginInfos = (await getPluginInfos()).data.data;
        if (pluginInfos === null || pluginInfos === undefined) {
           return;
        }
        for (let setting of settingsRaw) {
            let plugin = getPluginByNamespace(pluginInfos, setting.namespace);
            if (plugin === undefined) {
                setting.namespace = "默认设置";
            } else {
                setting.namespace = plugin.name;
            }
        }
        this.settings = settingsRaw;
    },
    updateSettings() {
      console.log(this.settings)
      this.settings.forEach(async config => {
        config.settings.forEach(async setting => {
          // console.log(setting)
          await addSetting(setting.key, setting.value)
        });
      })
      this.messageStore.setMessage("设置已保存", "success")
    },
  },
};
</script>

<template>
  <div>
    <WebSettingsContainer @update:settings="updateSettings"/>
    <SettingsItem class="setting-item" v-for="setting in settings" :key="setting.namespace" :pluginName="setting.namespace" :settings="setting.settings"/>
  </div>
</template>

<style scoped>
.setting-item {
  margin-top: 15px;
}
</style>