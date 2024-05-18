import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { setToken, getToken } from "@/utils/tokenManager";


export interface User {
  username: string;
  token: string;
}

export interface UserState {
  isLogin: boolean;
  user: User | null;
}


export const useUserStore = defineStore("user", {
  state: (): UserState => {
    let user =  localStorage.getItem("user");
    if (user) {
      return {
        isLogin: true,
        user: JSON.parse(user),
      };
    } else {
      return {
        isLogin: false,
        user: null,
      };
    }
  },
  actions: {
    bindUser(username: string, token: string) {
      let user = {
        username,
        token,
      };
      this.isLogin = true;
      this.user = user;
      setToken(user.token);
      localStorage.setItem("user", JSON.stringify(user));
    },
    logout() {
      this.isLogin = false;
      this.user = null;
    },
  }
});
