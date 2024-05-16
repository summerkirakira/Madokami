<script lang="ts">
import SettingsItem from './SettingsItem.vue';
import { getSettings } from '@/services/settingService';
import { getPluginByNamespace } from '@/utils/plugin';
import { getPluginInfos } from '@/services/pluginService';
import { type SettingRecord } from '@/client';

export default {
  components: {
    SettingsItem,
  },
  mounted() {
    this.fetchSettings();
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
  },
};
</script>

<template>
  <div>
    <SettingsItem v-for="setting in settings" :key="setting.namespace" :pluginName="setting.namespace" :settings="setting.settings" />
  </div>
</template>