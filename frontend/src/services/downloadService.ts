import { DownloadApi } from "@/client";
import { getToken } from "@/utils/tokenManager";


const downloadApi = new DownloadApi();

export async function getDownloads() {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await downloadApi.getDownloadsV1DownloadAllGet(token);
}

export async function clearAll() {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await downloadApi.clearDownloadsV1DownloadClearPost(token);
}