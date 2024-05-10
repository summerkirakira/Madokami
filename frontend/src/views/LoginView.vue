<script lang="ts">
import LoginBox from '../components/LoginBox.vue';

export default {
  components: {
    LoginBox
  }
}
</script>

<template>
    <LoginBox msg="需要登录" />
</template>

<style scoped>

.container {
  display: flex;
  justify-content: center;
}

</style>