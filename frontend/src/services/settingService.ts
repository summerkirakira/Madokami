import { SettingsApi } from './../client/api';
import { getToken } from "@/utils/tokenManager";


const settingsApi = new SettingsApi();


export async function getSettings() {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await settingsApi.getSettingsV1SettingsAllGet(token);
}

export async function addSetting(key: string, value: string | null) {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await settingsApi.updateSettingsV1SettingsUpdatePost(token, {key, value});
}