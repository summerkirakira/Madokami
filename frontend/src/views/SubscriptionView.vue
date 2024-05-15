<script lang="ts">
import type { PluginInfo, SubscriptionRecord } from '@/client';
import { getPluginInfos } from '@/services/pluginService';
import { getSubscriptions } from '@/services/subscribeService';
import { getPluginByNamespace } from '@/utils/plugin';
import SubscriptionItem from '@/components/SubscriptionItem.vue';

export default {
  components: {
    SubscriptionItem,
  },
  setup() {
    return {
    }
  },
  mounted() {
    this.refresh();
  },
  data() {
    return {
      pluginInfos: [] as PluginInfo[],
      subscriptions: [] as SubscriptionRecord[],
    }
  },
  methods: {
    async fetchPluginInfos() {
      this.pluginInfos = (await getPluginInfos()).data.data!;
      // console.log(this.pluginInfos);
    },
    async fetchSubscriptions() {
      this.subscriptions = (await getSubscriptions()).data.data!;
      // console.log(this.subscriptions);
    },
    async refresh() {
      await this.fetchPluginInfos();
      await this.fetchSubscriptions();
    },
  },
  computed: {
    subscriptionRecords() {
      let records = this.subscriptions.map(subscription => {
        const plugin = getPluginByNamespace(this.pluginInfos, subscription.namespace);
        return {
          pluginName: plugin?.name,
          pluginNamespace: plugin?.namespace,
          subscriptions: subscription.subscriptions.map(sub => {
            return {
              name: sub.name,
              value: sub.data,
            };
          })
        };
      });
      return records;
    }
  }
}

</script>


<template>
  <SubscriptionItem
    v-for="record in subscriptionRecords"
    :need-refresh="refresh"
    :key="record.pluginNamespace"
    :pluginName="record.pluginName!"
    :pluginNamespace="record.pluginNamespace!"
    :subscriptions="record.subscriptions" />
</template>


<style scoped>


</style>