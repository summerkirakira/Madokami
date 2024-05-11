<script lang="ts">
import { NInput, NButton } from "naive-ui";
import { useUserStore } from "@/stores/user";
import { userLogin } from "@/services/userService";
import { useMessageStore } from "@/stores/message";

export default {
  setup() {
    const userStore = useUserStore();
    const messageStore = useMessageStore();
    return {
      userStore,
      messageStore
    };
  },
  data() {
    return {
      username: "",
      password: "",
      isButtonLoading: false
    };
  },
  components: {
    NInput,
    NButton
  },
  methods: {
    async login() {
      this.isButtonLoading = true;
      let { data } = await userLogin(this.username, this.password);
      debugger;
      if (data.success) {
        this.userStore.bindUser(this.username, data.data!)
        this.messageStore.setMessage("登录成功", "success");
        this.$router.push("/");
      } else {
        this.isButtonLoading = false;
        this.messageStore.setMessage(data.message!, "error");
      }
    }
  }
}
</script>

<template>
  <div class="box">
    <div class="login-form">
      <h1 class="green">登录</h1>
      <div class="container">
          <NInput placeholder="用户名" v-model:value="username" :disabled="isButtonLoading"/>
          <NInput type="password" placeholder="密码" v-model:value="password" :disabled="isButtonLoading"/>
          <NButton type="primary" @click="login" :loading="isButtonLoading">登录</NButton>
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.0rem;
  position: relative;
  top: -10px;
}

.container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.login-form {
  width:100%;
  max-width: 400px;
  min-width: 300px;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: white;
}

.box {
  padding: 20px;
  /* max-width: 1024px; */
}

@media (min-width: 0px){
  .box {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .box > * {
    width: 100%;
  }
}


</style>
