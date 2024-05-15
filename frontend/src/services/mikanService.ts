import { MikanApi } from "@/client";
import { getToken } from "@/utils/tokenManager";


const mikanApi = new MikanApi();

export async function getSearchResult(searchString: string) {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await mikanApi.runEngineV1MikanSearchPost(token, {keyword: searchString});
}