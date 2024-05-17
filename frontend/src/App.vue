<script lang="ts">
import AppContainer from './components/AppContainer.vue';
import { NConfigProvider, darkTheme, NGlobalStyle, lightTheme } from 'naive-ui';
import { useThemeStore } from './stores/theme';


export default {
  components: {
    AppContainer,
    NConfigProvider,
    NGlobalStyle
  },
  setup() {
    const themeStore = useThemeStore();
    return {
      darkTheme,
      themeStore
    }
  },
  computed: {
    theme() {
      return this.themeStore.dark ? this.darkTheme : lightTheme;
    }
  }
}

</script>

<template>
  <NConfigProvider :theme="theme" :theme-overrides="themeStore.theme">
    <AppContainer />
    <NGlobalStyle />
  </NConfigProvider>
</template>

<style scoped>
header {
  line-height: 1.5;
  /* max-height: 100vh;
  max-width: 100vw; */
}

</style>
