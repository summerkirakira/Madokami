<script lang="ts">
import { RouterView } from "vue-router";
import MessageContainer from "./components/MessageContainer.vue";
import { NMessageProvider } from "naive-ui";


export default {
  components: {
    RouterView,
    MessageContainer,
    NMessageProvider
  },
}

</script>

<template>
  <n-message-provider>
  <MessageContainer />
  <header>
      <RouterView class="main" />
  </header>
  </n-message-provider>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  max-width: 100vw;
}

header .main {
  width: 100%;
}
</style>
