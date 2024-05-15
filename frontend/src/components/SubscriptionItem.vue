<script lang="ts">
import { NCard, NDataTable, NIcon, NModal, NButton, NSpace, NInput, NAutoComplete } from 'naive-ui';
import { AddOutline as AddIcon } from '@vicons/ionicons5';
import { ref } from 'vue';

import { SearchOutline } from '@vicons/ionicons5';
import MikanSubscriptionAdd from './MikanSubscriptionAdd.vue';
import { addSubscription } from '@/services/subscribeService';

export default {
    emits: ['need-refresh'],
    props: {
        pluginName: {
            type: String,
            required: true,
        },
        pluginNamespace: {
            type: String,
            required: true,
        },
        subscriptions: {
            type: Array as () => {name: string, value: string}[],
            required: true,
        },

    },
    components: {
        NCard,
        NDataTable,
        AddIcon,
        NIcon,
        NModal,
        NButton,
        NSpace,
        NInput,
        SearchOutline,
        NAutoComplete,
        MikanSubscriptionAdd
    },
    setup() {
        const showModal = ref(false);
        return {
            showModal,
        }
    },
    data() {
        return {
            newItemName: '',
            newItemValue: '',
            isLoading: false,
        }
    },
    methods: {
        receiveMikanResult(msg: {data: {name: string, value: string}}) {
            // console.log('receiveMikanResult', name, msg);
            this.newItemName = msg.data.name;
            this.newItemValue = msg.data.value;
        },
        handleConfirm() {
            this.isLoading = true;
            addSubscription(this.pluginNamespace, this.newItemName, this.newItemValue).then(() => {
                this.isLoading = false;
                this.showModal = false;
            });
            this.$emit('need-refresh');
        }
    }
}
</script>

<template>
    <NCard :title="pluginName">
        <template #header-extra>
        <NButton circle @click="showModal = true">
            <template #icon>
                <NIcon>
                    <AddIcon />
                </NIcon>
            </template>
        </NButton>
        </template>
        <NDataTable
            :data="subscriptions"
            :columns="[
                { title: '订阅名', key: 'name' },
                { title: '订阅地址', key: 'value' },
            ]"
        />
    </NCard>


    <n-modal v-model:show="showModal">
    <n-card
      style="width: 600px"
      title="添加订阅"
      :bordered="false"
      size="huge"
      role="dialog"
      aria-modal="true"
    >
      <template #header-extra>
        噢！
      </template>
      <MikanSubscriptionAdd v-if="pluginNamespace === 'summerkirakira.mikan_project'" @search-result="receiveMikanResult" />
      <h3>订阅名</h3>
      <n-input :placeholder="''" v-model:value="newItemName" />
      <h3>订阅地址</h3>
      <n-input :placeholder="''" v-model:value="newItemValue" />
      <template #action>
        <n-space reverse>
            <n-button type="primary" :loading="isLoading" @click="handleConfirm">确定</n-button>
            <n-button @click="showModal = false">取消</n-button>
        </n-space>
      </template>
    </n-card>
  </n-modal>

</template>

<style scoped>
h3 {
  margin-top: 20px;
  margin-bottom: 5px;
  font-weight: bold;
  font-size: 16px;
}
</style>