import { UserApi } from "@/client";
import { useUserStore } from "@/stores/user";
import pinia from "../stores"


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