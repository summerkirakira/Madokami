<script lang="ts">

import { type DownloadData } from '@/client';
import { NProgress, NEllipsis, NSplit} from 'naive-ui';
import { formatBytes } from '@/utils/formatter';

export default {
  props: {
    data: {
      type: Object as () => DownloadData,
      required: true,
    },
  },
  components: {
    NProgress,
    NEllipsis,
    NSplit,
  },
  computed: {
    downloadSpeedString(): string {
        return formatBytes(this.data.current_speed) + '/s';
    },
    totalSizeString(): string {
      return formatBytes(this.data.total_length);
    },
  }
};

</script>

<template>
<div class="download-item">
  <n-ellipsis line-clamp="1">
    <p>{{ data.name }}</p>
  </n-ellipsis>
  <!-- <n-ellipsis line-clamp="1">
    <p>{{ data.target_path }}</p>
  </n-ellipsis> -->
  <n-progress :percentage="data.progress" :processing="true">
    {{ downloadSpeedString }}
  </n-progress>
  <p class="total-size">{{ totalSizeString }}</p>
</div>
</template>

<style scoped>
.download-item {
  padding: 10px;
  border-bottom: 1px solid #f0f0f0;
  min-width: 300px;
}
</style>