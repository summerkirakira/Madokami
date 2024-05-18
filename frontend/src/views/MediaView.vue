<script lang="ts">

import { type Media } from '@/client';
import { getMediaList } from '@/services/mediaService';
import { NCard, NEllipsis, NBadge, NFloatButton, NIcon, NFloatButtonGroup, NPopover } from 'naive-ui';
import { 
  ArrowDownCircleOutline as DownloadIcon,
  SettingsOutline as SettingsIcon,
  RefreshOutline as RefreshIcon,
  RemoveCircleOutline as RemoveIcon,
} from '@vicons/ionicons5'
import DownloadContainer from '@/components/DownloadContainer.vue';
import { getDownloads } from '@/services/downloadService';
import { type DownloadData } from '@/client';
import { runAllEngines } from '@/services/engineService';
import { useMessageStore } from '@/stores/message';
import { clearAll } from '@/services/downloadService';

export default {
  setup() {
    const messageStore = useMessageStore();
    return {
      messageStore,
    }
  },
  mounted() {
    this.fetchMedia();
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth;
    });
    this.needRefresh = true;
    this.repeatFetchDownloads();
  },
  unmounted() {
    this.needRefresh = false;
  },
  data() {
    return {
      media: [] as Media[],
      windowWidth: window.innerWidth,
      downloads: [] as DownloadData[],
      needRefresh: true,
    };
  },
  components: {
    NCard,
    NEllipsis,
    NBadge,
    NFloatButton,
    NFloatButtonGroup,
    NIcon,
    DownloadIcon,
    DownloadContainer,
    NPopover,
    SettingsIcon,
    RefreshIcon,
    RemoveIcon
  },
  methods: {
    async fetchMedia() {
      this.media = (await getMediaList()).data.data!;
    },
    simplifyTitle(title: string) {
      return title.length > 20 ? title.slice(0, 12) + '...' : title;
    },
    async fetchDownloads() {
          this.downloads = (await getDownloads()).data.data!;
      },
    async repeatFetchDownloads() {
        while (this.needRefresh) {
            await this.fetchDownloads();
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    },
    handleRefresh() {
      runAllEngines().then(() => {
        this.messageStore.setMessage('已刷新订阅', 'success');
      });
    },
    handleClearAll() {
      clearAll().then(() => {
        this.messageStore.setMessage('已清除所有下载任务', 'success');
      });
    },
  
  },
}

</script>


<template>
  <div class="media-view">
    <div class="media-box">
      <n-card v-for="m in media" :key="m.id" style="width: 200px" hoverable header-style="padding: 10px;" content-style="padding: 10px;" size="medium">
      <template #header>
        <n-ellipsis line-clamp="1">
        <p class="img-title">{{ m.title }}</p>
        </n-ellipsis>
      </template>
      <template #cover>
        <img :src="`http://localhost:8000/v1/media/cover/${m.id}`" alt="media thumbnail" />
      </template>
      <p class="img-content">{{ `已下载${m.contents.length}集` }}</p>
    </n-card>
    </div>
  </div>
  <div class="button-group">
    <n-float-button-group shape="square" position="relative">
      <n-float-button>
        <n-popover placement="left-start" trigger="hover" scrollable>
          <template #trigger>
            <n-badge :value="downloads.length" :offset="[6, -8]" :processing="true">
              <n-icon><download-icon /></n-icon>
            </n-badge>
          </template>
          <DownloadContainer :downloads="downloads" />
        </n-popover>
      </n-float-button>
      <n-float-button @click="handleRefresh">
        <n-popover placement="left" trigger="hover" scrollable>
          <template #trigger>
            <n-icon><refresh-icon /></n-icon>
          </template>
          <div>立即刷新订阅</div>
        </n-popover>
      </n-float-button>
      <n-float-button @click="handleClearAll">
        <n-popover placement="left" trigger="hover" scrollable>
          <template #trigger>
            <n-icon><remove-icon /></n-icon>
          </template>
          <div>清除下载队列中所有的任务</div>
        </n-popover>
      </n-float-button>
    
    </n-float-button-group>
  </div>
</template>


<style scoped>
.media-view {
  padding: 1rem;
  height: 100%;
}

.media-box {
  display: grid;
  grid-column-gap: 60px;
  grid-row-gap: 20px;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
}

.img-title {
  font-size: 1rem;
  font-weight: bold;
  margin: 0;
}

.n-card-header {
  padding: 0;
}

.button-group {
  position: fixed;
  right: 1rem;
  top: 80px;
}

</style>