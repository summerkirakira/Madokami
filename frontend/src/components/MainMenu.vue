<script lang="ts">
import { h, type Component } from 'vue'
import { NIcon, NSplit, NMenu } from 'naive-ui'
import type { MenuOption } from 'naive-ui'

import {
  BookOutline as BookIcon,
  SettingsOutline as SettingsIcon,
  HomeOutline as HomeIcon,
  DocumentTextOutline as LogIcon
} from '@vicons/ionicons5'


function renderIcon (icon: Component) {
  return () => h(NIcon, null, { default: () => h(icon) })
}

const menuOptions: MenuOption[] = [
  {
    label: '媒体库',
    key: 'media',
    icon: renderIcon(HomeIcon)
  },
  {
    label: '订阅管理',
    key: 'subscriptions',
    icon: renderIcon(BookIcon),
    disabled: false,
  },
  {
    label: '日志',
    key: 'logs',
    icon: renderIcon(LogIcon),
    disabled: false,
  },
  {
    label: '设置',
    key: 'settings',
    icon: renderIcon(SettingsIcon),
    disabled: false,
  }
]

function isHorizontal(): 'horizontal' | 'vertical' {
  let width = window.innerWidth
  if (width < 1024) {
    return 'horizontal'
  } else {
    return 'vertical'
  }
}

export default {
  setup() {
  
    return {

    };
  },
  mounted() {
    window.addEventListener('resize', this.updateWidth);
  },

  data() {
    return {
      menuOptions,
      menuMode: isHorizontal()
    }
  },
  methods: {
    updateWidth() {
      this.menuMode = isHorizontal()
    },
    handleSelect(key: string, item: MenuOption) {
      // console.log(key)
      this.$router.push({ name: key })
    }
  },
  components: {
    NSplit,
    NMenu
  },
  computed: {
    currentPage() {
      return this.$route.name?.toString() || 'media'
    }
  }
}

</script>

<template>
  <n-menu
    :on-update:value="handleSelect"
    :mode="menuMode"
    :options="menuOptions"
    :value="currentPage"
    responsive
  />
</template>

<style scoped>

</style>