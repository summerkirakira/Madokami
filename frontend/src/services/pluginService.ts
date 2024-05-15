import { PluginApi } from "@/client";
import { getToken } from "@/utils/tokenManager";


const pluginApi = new PluginApi();


export async function getPluginInfos() {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await pluginApi.runEngineV1PluginInfoGet(token);
}