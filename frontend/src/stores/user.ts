import { ref, computed } from "vue";
import { defineStore } from "pinia";


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
    return {
      isLogin: false,
      user: null,
    };
  }
});
