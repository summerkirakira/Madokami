import { MediaApi } from "@/client";
import { getToken } from "@/utils/tokenManager";


const mediaApi = new MediaApi();

export async function getMediaList() {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await mediaApi.getAllMediaV1MediaAllGet(token);
}