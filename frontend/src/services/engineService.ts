import { EngineApi } from "@/client";
import { getToken } from "@/utils/tokenManager";


const engineApi = new EngineApi();


export async function runAllEngines() {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await engineApi.refreshAllEnginesV1EngineRunAllGet(token);
}