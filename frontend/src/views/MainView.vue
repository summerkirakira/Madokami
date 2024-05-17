<script lang="ts">

import MainMenu from '@/components/MainMenu.vue'
import MainTitleBar from '@/components/MainTitleBar.vue'

import { RouterView } from 'vue-router'
import { NScrollbar, NConfigProvider, darkTheme } from 'naive-ui';

export default {
  components: {
    RouterView,
    MainMenu,
    MainTitleBar,
    NScrollbar,
    NConfigProvider
  }
}

</script>


<template>
  <div>
    <MainTitleBar />
    <div class="container">
      <MainMenu />
      <n-scrollbar style="max-height: calc(100vh - 60px);">
        <RouterView />
      </n-scrollbar>
    </div>
  </div>
</template>


<style scoped>
.container {
  display: grid;
  /* height: calc(100vh - 200px); */
}

@media (min-width: 1024px) {
  .container {
    grid-template-columns: 200px 1fr;
  }
}

@media (max-width: 1023px) {
  .container {
    grid-template-rows: 50px 1fr;
  }
}

</style>