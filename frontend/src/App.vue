<script lang="ts">
import AppContainer from './components/AppContainer.vue';
import { NConfigProvider, darkTheme, NGlobalStyle, lightTheme, NThemeEditor } from 'naive-ui';
import { useThemeStore } from './stores/theme';
import hljs from 'highlight.js/lib/core';

hljs.registerLanguage('madokami-log', () => ({
  contains: [
    {
      className: 'timestamp',
      begin: /\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/,
      end: / /,
      excludeEnd: true
    },
    {
      scope: 'level-info',
      begin: /SUCCESS/,
      end: / /,
      excludeEnd: true
    }
  ]
})
)

hljs.registerLanguage('naive-log', () => ({
    contains: [
      {
        className: 'string',
        begin: /\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[SUCCESS\].*/,
      },
      {
        className: 'number',
        begin: /\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[WARNING\].*/,
      },
      {
        className: 'keyword',
        begin: /\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[ERROR\].*/,
      },
      {
        className: 'comment',
        begin: /\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[INFO\].*/,
      }
    ]
  }))

export default {
  components: {
    AppContainer,
    NConfigProvider,
    NGlobalStyle,
    NThemeEditor
  },
  setup() {
    const themeStore = useThemeStore();
    return {
      darkTheme,
      themeStore,
      hljs
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
  <NConfigProvider :theme="theme" :theme-overrides="themeStore.theme" :hljs="hljs">
  <!-- <NThemeEditor> -->
    <AppContainer />
    <NGlobalStyle />
  <!-- </NThemeEditor> -->
  </NConfigProvider>
</template>

<style>
header {
  line-height: 1.5;
  /* max-height: 100vh;
  max-width: 100vw; */
}

.timestamp { color: #888; }
.level-info { color: green; }
.level-warning { color: orange; }
.level-error { color: red; }


</style>
