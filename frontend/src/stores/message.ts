import { defineStore } from "pinia";


export interface MessageState {
  message: string;
  type: string;
  timestamp: number;
}

export const useMessageStore = defineStore("alert", {
  state: (): MessageState => ({
    message: "",
    type: "",
    timestamp: 0,
  }),
  actions: {
    setMessage(message: string, type: string) {
      this.message = message;
      this.type = type;
      this.timestamp = Date.now();
    },
    clearMessage() {
      this.message = "";
      this.type = "";
      this.timestamp = 0;
    },
  },
});