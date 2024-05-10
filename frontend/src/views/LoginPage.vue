<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import MadokamiTitle from "@/components/MadokamiTitle.vue";
import LoginBox from "@/components/LoginBox.vue";
</script>

<template>
  <div class="container">
    <header>
    <div class="wrapper">
      <MadokamiTitle />
    </div>
    <LoginBox />
  </header>
  </div>
  
  
</template>

<style scoped>
header {
  line-height: 1.5;
  width: 100%;
  opacity: 0;
  animation: fadeUp 2s ease forwards;
  max-width: 1000px;
}

.container {
  height: 100vh;
  display: grid;
  place-items: center;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0 2rem;
    align-items: center;
  }
}

@keyframes fadeUp {
  from {
    /* 动画开始状态：完全透明且向下30px */
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    /* 动画结束状态：完全不透明且在原位 */
    opacity: 1;
    transform: translateY(0);
  }
}

/* 应用动画到目标元素 */
.element {
  opacity: 0; /* 初始状态设置为透明，确保动画从看不见的状态开始 */
  animation: fadeUp 1s ease forwards; /* 动画名称，持续时间，缓动函数，动画填充模式 */
}

</style>