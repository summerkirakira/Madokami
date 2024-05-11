<script lang="ts">
import { defineComponent, h, type Component } from 'vue'
import { NIcon, useMessage, NSplit, NMenu } from 'naive-ui'
import type { MenuOption } from 'naive-ui'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

import {
  BookOutline as BookIcon,
  PersonOutline as PersonIcon,
  SettingsOutline as SettingsIcon,
  HomeOutline as HomeIcon
} from '@vicons/ionicons5'


function renderIcon (icon: Component) {
  return () => h(NIcon, null, { default: () => h(icon) })
}

const menuOptions: MenuOption[] = [
  {
    label: "媒体库",
    key: 'hear-the-wind-sing',
    icon: renderIcon(HomeIcon)
  },
  {
    label: '订阅管理',
    key: 'subscription-manage',
    icon: renderIcon(BookIcon),
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
    }
  },
  components: {
    NSplit,
    NMenu
  }
}

</script>

<template>
  <n-menu
    :mode="menuMode"
    :options="menuOptions"
    responsive
  />
</template>

<style scoped>

</style>