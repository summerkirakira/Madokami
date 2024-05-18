<script lang="ts">

import DownloadItem from './DownloadItem.vue';
import { type DownloadData } from '@/client';
import { NScrollbar } from 'naive-ui';


export default {
    props: {
        downloads: {
            type: Object as () => DownloadData[],
            required: true,
        },
    },
    components: {
        DownloadItem,
        NScrollbar
    },
    mounted() {
        
    },
    unmounted() {
        // Stop the loop
        this.needRefresh = false;
    },
    data() {
        return {
            needRefresh: false,
        };
    },
    methods: {
        
    }
};

</script>

<template>
    <n-scrollbar style="max-height: 300px">
        <div>
            <DownloadItem v-if="downloads.length > 0" v-for="d in downloads" :key="d.id" :data="d" />
            <p v-else>正在进行的下载项会显示在这里</p>
        </div>
    </n-scrollbar>
</template>

<style scoped>

</style>