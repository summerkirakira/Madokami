<script lang="ts">
import { NIcon, NAutoComplete, NDynamicTags } from 'naive-ui';
import { SearchOutline as SearchIcon } from '@vicons/ionicons5';
import { getSearchResult } from '@/services/mikanService';
import { type SearchItem } from '@/client';
import { type SelectOption, NTag } from 'naive-ui'
import { defineComponent, ref, computed, h, type VNodeChild } from 'vue'
import loading from 'naive-ui/es/_internal/loading';

export default {
  emits: ['search-result'],
  components: {
    NAutoComplete,
    SearchIcon,
    NIcon,
    NTag,
    NDynamicTags
  },
  methods: {
    postMessage(name: string, value: string) {
      // console.log('postMessage', name, value);
      this.$emit('search-result', {
        type: 'add',
        data: {
          name,
          value
        }
      });
    },
    async searchMikan(query: string) {
      const result = await getSearchResult(query);
      return result;
    },
    renderPrefferedTag(tag: string, index: number) {
        return h(
          NTag,
          {
            type: index < 3 ? 'success' : 'error',
            disabled: index > 3,
            closable: true,
            onClose: () => {
              this.prefferedTags.splice(index, 1)
            }
          },
          {
            default: () => tag
          }
        )
      },
      renderExcludedTag(tag: string, index: number) {
        return h(
          NTag,
          {
            type: index < 3 ? 'error' : 'success',
            disabled: index > 3,
            closable: true,
            onClose: () => {
              this.excludedTags.splice(index, 1)
            }
          },
          {
            default: () => tag
          }
        )
      },
      postCurrentData() {
        if (this.currentSelectedValue === "") {
          return;
        }
        const [name, url, groupType] = this.currentSelectedValue.split('#');
          if (!this.prefferedTags.includes(groupType)){
            this.prefferedTags.push(groupType);
          }
          this.postMessage(name, `${url}#${this.extraString}`);

      },
      onItemSelect(value: string){
        const [name, url, groupType] = value.split('#');
        if (!this.prefferedTags.includes(groupType)){
          this.prefferedTags.push(groupType);
        }
        this.currentSelectedValue = value;
        this.postMessage(name, `${url}#${this.extraString}`);
      }
  },
  data() {
    return {
      searchResult: [] as SearchItem[],
      searchValue: '',
      isLoading: false,
      currentSelectedValue: "" as string,
    };
  },
  computed: {
    searchOptions() {
      let itemMap = new Map<string, SearchItem>();
      let itemCountMap = new Map<string, number>();
      this.searchResult.forEach((item) => {
        const key = `${item.bangumi_name}-${item.bangumi_id}-${item.subtitle_group_id}-${item.group_type}`
        itemMap.set(key, item);
        if (itemCountMap.has(key)) {
          itemCountMap.set(key, itemCountMap.get(key)! + 1);
        } else {
          itemCountMap.set(key, 1);
        }

      });
      return Array.from(itemMap.values()).map((item) => {
        return {
          label: item.bangumi_name,
          value: `${item.bangumi_name}#https://mikanani.me/RSS/Bangumi?bangumiId=${item.bangumi_id}&subgroupid=${item.subtitle_group_id}#${item.group_type}`,
          item: item,
          count: itemCountMap.get(`${item.bangumi_name}-${item.bangumi_id}-${item.subtitle_group_id}-${item.group_type}`)!
        };
      });
    },
    extraString(): string {
      return `${this.prefferedTags.join(',')}|${this.excludedTags.join(',')}`;
    }
  },
  setup() {
    return {
      lastSearchTimestamp: 0,
      renderLabel: (option: {label: string, value: string, item: SearchItem, count: number}): VNodeChild => [
        option.label as string,
        ' ',
        h(NTag, { size: 'small', type: 'info' }, { default: () => option.item.subtitle_group_name }),
        ' ',
        h(NTag, { size: 'small', type: 'success' }, { default: () => option.item.group_type }),
        ' ',
        h(NTag, { size: 'small', type: 'warning' }, { default: () => `共${option.count}集` }),
      ],
      prefferedTags: ref(['1080p']),
      excludedTags: ref(['720p']),
    }
  },
  watch: {
    searchValue(newValue, oldValue) {
      if (Date.now() - this.lastSearchTimestamp < 2000) {
        return;
      }
      this.isLoading = true;
      this.searchMikan(newValue).then((result) => {
        this.searchResult = result.data.data!;
        this.isLoading = false;
      });
      // console.log(this.searchResult);
    },
    prefferedTags: {
      handler(newValue, oldValue) {
        this.postCurrentData();
      },
      deep: true
    },
    excludedTags: {
      handler(newValue, oldValue) {
        this.postCurrentData();
      },
      deep: true
    }
  },

}
</script>
<template>
  <n-auto-complete 
  :loading="isLoading"
  v-model:value="searchValue"
  :placeholder="'搜索番剧'"
  :options="searchOptions"
  :on-select="onItemSelect"
  :render-label="renderLabel">
    <template #prefix>
        <n-icon>
            <SearchIcon />
        </n-icon>
    </template>
</n-auto-complete>
<h3>优先关键字</h3>
<n-dynamic-tags v-model:value="prefferedTags" :render-tag="renderPrefferedTag" />
<h3>排除关键字</h3>
<n-dynamic-tags v-model:value="excludedTags" :render-tag="renderExcludedTag" />
</template>

<style scoped>
h3 {
  margin-top: 20px;
  margin-bottom: 10px;
  font-weight: bold;
  font-size: 16px;
}
</style>