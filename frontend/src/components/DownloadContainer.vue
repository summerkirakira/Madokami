<script lang="ts">

import DownloadItem from './DownloadItem.vue';
import { type DownloadData } from '@/client';
import { getDownloads } from '@/services/downloadService';


export default {
    props: {
        downloads: {
            type: Object as () => DownloadData[],
            required: true,
        },
    },
    components: {
        DownloadItem,
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
<DownloadItem v-for="d in downloads" :key="d.id" :data="d" />
</template>

<style scoped>

</style>