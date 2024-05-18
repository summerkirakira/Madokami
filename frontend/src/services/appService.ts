import { AppApi } from "@/client";
import { getToken } from "@/utils/tokenManager";


const appApi = new AppApi();


export async function restartApp() {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await appApi.getLogAllV1AppRestartGet(token);
}