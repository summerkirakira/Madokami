<script lang="ts">
import { NSpace, NCard, NInput, NIcon, NButton } from 'naive-ui';
import { CreateOutline as CreateIcon } from '@vicons/ionicons5';



export default {
  components: {
    NSpace,
    NCard,
    NInput,
    NIcon,
    CreateIcon,
    NButton
  },
  props: {
    pluginName: {
      type: String,
      required: true,
    },
    settings: {
      type: Array as () => { key:string, name: string, description: string, value: string | null }[],
      required: true,
    },
  },
  emits: [
    // 'update:settings'
  ],
  setup() {
    return {
      
    }
  },
  data() {
    return {
    }
  },
  methods: {
    // async emitUpdateSettings() {
    //   this.$emit('update:settings')
    // }
  }
}
</script>

<template>
  <NCard size="medium" :title="pluginName">
    <!-- <template v-if="pluginName === '默认设置'" #header-extra>
      <NButton type="primary" size="small" @click="emitUpdateSettings">保存</NButton>
    </template> -->
    <NSpace>
      <div v-for="setting in settings" :key="setting.name">
        <NCard size="small" :title="setting.name">
          <p class="description">{{ setting.description }}</p>
          <NInput class="input" v-model:value="setting.value" placeholder="">
            <template #suffix>
              <n-icon>
                <CreateIcon />
              </n-icon>
            </template>
          </NInput>
        </NCard>
      </div>
    </NSpace>
  </NCard>
</template>

<style scoped>
.input {
  width: 400px;
}
.description {
  margin-bottom: 10px;
  opacity: 0.7;
}
</style>