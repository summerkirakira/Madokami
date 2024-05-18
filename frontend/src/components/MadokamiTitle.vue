<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div class="wrapper">
    <img
      alt="Madokami logo"
      class="logo"
      src="@/assets/logo.png"
      width="125"
      height="125"
    />
  <div class="greetings">
    <h1 class="green">Madokami</h1>
    <h3>
      一个轻量的ACGN订阅与管理平台
    </h3>
  </div>
  <!-- <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
  </nav> -->
  </div>
</template>

<style scoped>

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: #000;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid #000;
}

nav a:first-of-type {
  border: 0;
}



h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
  color: #f67ba4;
}

h3 {
  font-size: 1.2rem;
  color: #f67ba471;
}

.greetings {
  width: 100%;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

/* @media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: center;
  }
}

.wrapper {
  max-width: 800px;
}

.wrapper img {
  display: block;
  margin: 0 auto 2rem;
} */
</style>
