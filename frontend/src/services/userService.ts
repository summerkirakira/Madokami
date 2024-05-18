import { UserApi } from "@/client";
import { useUserStore } from "@/stores/user";
import pinia from "../stores"
import { getToken } from "@/utils/tokenManager";


const userStore = useUserStore(pinia);


const userApi = new UserApi();


export function jumpToLogin() {
    window.location.href = "/login";
}


export async function userLogin(username: string, password: string) {
    
    return await userApi.userLoginV1UserLoginPost(
        { username, password }
    );
}

export async function userUpdate(username: string, password: string) {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await userApi.createUserV1UserCreatePost(token, { username, password });
}