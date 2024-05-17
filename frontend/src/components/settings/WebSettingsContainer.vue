<script lang="ts">
import { NCard, NButton, NSpace, NAvatar, NSwitch, NIcon } from 'naive-ui';
import { useThemeStore } from '@/stores/theme';
import { Sunny as LightIcon, Moon as DarkIcon } from '@vicons/ionicons5';

export default {
  emits: [
    'update:settings'
  ],
  components: {
    NCard,
    NButton,
    NSpace,
    NAvatar,
    NSwitch,
    LightIcon,
    DarkIcon,
    NIcon
  },
  setup() {
    const themeStore = useThemeStore()
    return {
      themeStore
    }
  },
  data() {
    return {
      themes: [
        {
          name: 'Pink',
          value: 'pink',
          color: '#ff80aa'
        },
        {
          name: 'Blue',
          value: 'blue',
          color: '#33cbff'
        },
        {
          name: 'Green',
          value: 'green',
          color: '#5cd65c'
        }
      ]
    }
  },
  methods: {
    async emitUpdateSettings() {
      this.$emit('update:settings')
    }
  },
  watch: {
    'themeStore.dark': {
      handler: function (val) {
        this.themeStore.setDark(val)
      },
      immediate: true
    }
  }
}

</script>
<template>
    <NCard size="medium" title="通用设置">
        <template #header-extra>
            <NButton type="primary" size="small" @click="emitUpdateSettings">保存</NButton>
        </template>
        <NCard size="small" title="主题设置">
          <template #header-extra>
            <NSwitch v-model:value="themeStore.dark">
              <template #checked-icon>
                <NIcon>
                  <DarkIcon />
                </NIcon>
              </template>
              <template #unchecked-icon>
                <NIcon>
                  <LightIcon />
                </NIcon>
              </template>
            </NSwitch>
          </template>
            <NSpace>
                <div v-for="theme in themes" :key="theme.name">
                    <NAvatar :style="{ backgroundColor: theme.color }" @click="themeStore.setTheme(theme.value)"/>
                    <!-- <p>{{ theme.name }}</p> -->
                </div>
            </NSpace>
        </NCard>
    </NCard>
</template>