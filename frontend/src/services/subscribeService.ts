import { SubscribeApi } from './../client/api';
import { getToken } from "@/utils/tokenManager";


const subscribeApi = new SubscribeApi();


export async function getSubscriptions() {
    const token = getToken();
    console.log(subscribeApi)
    if (!token) {
        throw new Error("User not logged in");
    }
    return await subscribeApi.getDownloadsV1SubscribeAllGet(token);
}

export async function addSubscription(namespace: string, name: string, value: string) {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await subscribeApi.addSubscriptionV1SubscribeAddPost(token, {namespace, name, data: value});
}

export async function deleteSubscription(namespace: string, id: string) {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await subscribeApi.removeSubscriptionV1SubscribeRemovePost(token, {namespace, id})
}