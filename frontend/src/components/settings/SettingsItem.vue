<script lang="ts">
import { NSpace, NCard, NInput, NIcon, NButton, NInputNumber } from 'naive-ui';
import { CreateOutline as CreateIcon } from '@vicons/ionicons5';

export default {
  components: {
    NSpace,
    NCard,
    NInput,
    NIcon,
    CreateIcon,
    NButton,
    NInputNumber
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
    tasks: {
      type: Array as () => { id: number, name: string, interval: number }[],
      required: true
    }
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
      <div v-if="tasks !== undefined">
        <NCard size="small" title="定时任务" v-if="pluginName !== '默认设置'">
          <p class="description">为插件提供的订阅引擎设置定时任务, 0代表永不自动执行</p>
          <div v-for="task of tasks" :key="task.id">
            <n-space justify="start" vertical>
              <p>{{ `${task.name}:` }}</p>
              <n-input-number class="input" placeholder="" :precision="0" v-model:value="task.interval">
                <!-- <template #prefix>
                  <p class="input-number-text">每</p>
                </template> -->
                <template #suffix>
                  <p class="input-number-text">分钟循环执行</p>
                </template>
              </n-input-number>
          </n-space>
          </div>
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

.input-number-text {
  opacity: 0.7;
}
</style>