<script setup lang="ts">
import { RouterView } from "vue-router";
</script>

<template>
  <header>
    <RouterView class="main" />
  </header>
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
