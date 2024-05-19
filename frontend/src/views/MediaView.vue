<script lang="ts">

import { type Media } from '@/client';
import { getMediaList } from '@/services/mediaService';
import { NCard, NEllipsis, NBadge, NFloatButton, NIcon, NFloatButtonGroup, NPopover, NModal, NImage, NSpace, NScrollbar, NTag, NDivider, NTime } from 'naive-ui';
import { 
  ArrowDownCircleOutline as DownloadIcon,
  SettingsOutline as SettingsIcon,
  RefreshOutline as RefreshIcon,
  RemoveCircleOutline as RemoveIcon,
  CheckmarkCircle as CheckmarkIcon,
  FileTrayFull as FileIcon,
  Time as TimeIcon
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
      showMediaDetail: false,
      selectedMedia: {} as Media,
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
    RemoveIcon,
    NModal,
    NImage,
    NSpace,
    NScrollbar,
    NTag,
    NDivider,
    CheckmarkIcon,
    FileIcon,
    NTime,
    TimeIcon
  },
  methods: {
    async fetchMedia() {
      this.media = (await getMediaList()).data.data!;
      console.log(this.media);
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
    getImgSrc(id: string) {
      if (import.meta.env.DEV){
        return `http://localhost:8000/v1/media/cover/${id}`;
      } else {
        return `/v1/media/cover/${id}`
      }
    },
    showMediaDetailModal(media: Media) {
      this.selectedMedia = media;
      this.showMediaDetail = true;
    },
    getEpisodeTitle(content: { title: string, episode: number }) {
      return `第${content.episode}集 ${content.title}`;
    }
  },
  computed: {
    sortedSelectedContents() {
      return this.selectedMedia.contents.sort((a, b) => a.episode - b.episode);
    }
  }
}

</script>


<template>
  <div class="media-view">
    <div class="media-box">
      <n-card v-for="m in media" :key="m.id" style="width: 200px" hoverable header-style="padding: 10px;" content-style="padding: 10px;" size="medium" @click="showMediaDetailModal(m)">
      <template #header>
        <n-ellipsis line-clamp="1">
        <p class="img-title">{{ m.title }}</p>
        </n-ellipsis>
      </template>
      <template #cover>
        <img :src="getImgSrc(m.id)" alt="media thumbnail" />
      </template>
      <!-- <p class="img-content">{{ `已下载${m.contents.length}集` }}</p> -->
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
  <n-modal v-model:show="showMediaDetail">
    <n-card title="媒体信息" size="medium" style="width: 600px">
      <template #header-extra>
        <n-tag type="warning" bordered>{{ `第${selectedMedia.season}季`}}</n-tag>
      </template>
      <n-space justify="center">
        <div>
          <n-image :src="getImgSrc(selectedMedia.id)" width="200"/>
          <p class="detail-title">{{ selectedMedia.title }}</p>
        </div>
        <div>
          <n-scrollbar style="height: 400px; width: 300px;">
            <n-popover v-for="content of sortedSelectedContents" :key="content.link" trigger="hover" placement="top-start">
              <template #trigger>
                <n-space justify="start">
                  <n-tag :bordered="false" type="success" class="media-detail-episode">{{ `第${content.episode}集` }}</n-tag>
                  <n-tag :bordered="false" type="info">{{ content.title }}</n-tag>
                </n-space>
              </template>
              <n-space justify="start">
                <n-tag round :bordered="false" type="success">
                已下载
                <template #icon>
                  <n-icon> <checkmark-icon /></n-icon>
                </template>
              </n-tag>
                <p class="popover-item-text">{{ content.link }}</p>
              </n-space>
              <n-divider />
              <n-space justify="start">
                <n-tag round :bordered="false" type="info">
                存储于
                <template #icon>
                  <n-icon> <FileIcon /> </n-icon>
                </template>
              </n-tag>
                <p class="popover-item-text">{{ content.path }}</p>
              </n-space>
              <n-divider />
              <n-space justify="start">
                <n-tag round :bordered="false" type="warning">
                下载于
                <template #icon>
                  <n-icon> <TimeIcon /> </n-icon>
                </template>
              </n-tag>
                <n-time class="popover-item-text" :time="content.add_time * 1000" format="yyyy年MM月dd日 hh:mm"/>
              </n-space>
            </n-popover>
          </n-scrollbar>
        </div>
      </n-space>
      
    </n-card>
  </n-modal>
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

.media-detail-episode {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.popover-item-text {
  max-width: 300px;
}

.detail-title {
  font-size: 1.3rem;
  font-weight: bold;
  margin-top: 1rem;
  max-width: 200px;
}


</style>