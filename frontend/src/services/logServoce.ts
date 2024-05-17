import { LogApi } from "@/client";
import { getToken } from "@/utils/tokenManager";


const logApi = new LogApi();


export async function getLogs() {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await logApi.getLogAllV1LogAllGet(token);
}