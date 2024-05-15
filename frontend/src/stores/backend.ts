import { defineStore } from "pinia";
import { PluginApi, type PluginInfo } from "@/client";


export const usePluginStore = defineStore("plugin", {
    state: (): {pluginInfo: PluginInfo | null} => ({
      pluginInfo: null,
    }),
    actions: {
      
    },
  });