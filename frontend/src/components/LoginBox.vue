<script lang="ts">
import { NInput, NButton } from "naive-ui";
import { useUserStore } from "@/stores/user";

export default {
  setup() {
    const userStore = useUserStore();
    return {
      userStore
    };
  },
  components: {
    NInput,
    NButton
  }
}
</script>

<template>
  <div class="box">
    <div class="login-form">
      <h1 class="green">登录</h1>
      <div class="container">
          <NInput placeholder="用户名" />
          <NInput type="password" placeholder="密码" />
          <NButton type="primary">登录</NButton>
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
