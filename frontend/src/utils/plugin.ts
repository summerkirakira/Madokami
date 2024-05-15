import type { PluginInfo } from "@/client";


export function getPluginByNamespace(plugins: PluginInfo[], namespace: string): PluginInfo | undefined {
    return plugins.find(plugin => plugin.namespace === namespace);
}