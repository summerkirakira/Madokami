<script lang="ts">

import MainMenu from '@/components/MainMenu.vue'

import { RouterView } from 'vue-router'

export default {
  components: {
    RouterView,
    MainMenu
  }
}

</script>


<template>
  <div class="container">
    <MainMenu />
    <RouterView />
  </div>
</template>


<style scoped>
.container {
  display: grid;
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