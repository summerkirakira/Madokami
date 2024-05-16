<script lang="ts">
import { NSpace, NCard, NInput, NIcon } from 'naive-ui';
import { CreateOutline as CreateIcon } from '@vicons/ionicons5';


export default {
  components: {
    NSpace,
    NCard,
    NInput,
    NIcon,
    CreateIcon
  },
  props: {
    pluginName: {
      type: String,
      required: true,
    },
    settings: {
      type: Array as () => { name: string, description: string, value: string | null }[],
      required: true,
    },
  },
  setup() {
    return {
    }
  },
  data() {
    return {
    }
  },
  methods: {
  }
}
</script>

<template>
  <NCard size="medium" :title="pluginName">
    <NSpace>
      <div v-for="setting in settings" :key="setting.name">
        <NCard size="small" :title="setting.name">
          <p class="description">{{ setting.description }}</p>
          <NInput class="input" v-model:value="setting.value">
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