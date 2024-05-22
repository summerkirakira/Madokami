<script lang="ts">
import { getLogs } from '@/services/logService';
import { NLog, NCard, type LogInst } from 'naive-ui';
import { ref } from 'vue';


const logInstRef = ref<LogInst | null>(null);

export default {
  components: {
    NLog,
    NCard
  },
  mounted() {
    this.fetchLogs();
    this.repeatRefresh();
  },
  data() {
    return {
      logs: [] as string[]
    }
  },
  methods: {
    async fetchLogs() {
      let logResponse = await getLogs();
      if(logResponse.data.success == false) {
        return;
      }
      this.logs = logResponse.data.data!;
    },
    async refresh() {
      await this.fetchLogs();
    },
    repeatRefresh() {
      window.setInterval(() => {
        this.refresh();
      }, 5000);
    }
  },
  computed: {
    
  },
  setup() {
    return {
      logInstRef
    }
  },
  watch: {
    logs() {
      this.$nextTick(() => {
        if (logInstRef.value) {
          console.log(logInstRef)
          logInstRef.value?.scrollTo({ position: 'bottom', silent: true })
        }
      });
    }
  }
}

</script>


<template>
  <n-card title="日志" style="width: 100%">
    <n-log ref="logInst" :lines="logs" style="height: 80vh;" language="naive-log" />
  </n-card>
</template>


<style scoped>


</style>