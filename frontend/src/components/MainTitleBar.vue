<script lang="ts">
import { NDivider } from 'naive-ui';
export default {
  components: {
    NDivider
  }
}
</script>

<template>
  <div class="inline-container">
    <img
      alt="Madokami logo"
      class="logo"
      src="@/assets/logo.png"
      width="40"
      height="40"
    />
    <h2>Madokami</h2>
  </div>
</template>

<style scoped>
.inline-container {
    display: grid;
    grid-template-columns: auto 1fr;
    height: 50px;
    border-bottom: 1px solid #7877772a;
}

hr {
    margin: 0;
    background-color: #7877772a;
    margin-top: 10px
}

h2 {
    margin-left: 0.6rem;
    font-size: 1.7rem;
    font-weight: 500;
    color: #f67ba4;
}
</style>