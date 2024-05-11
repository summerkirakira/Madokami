<script lang="ts">
import { useMessageStore } from '@/stores/message'
import { NMessageProvider } from "naive-ui";
import { useMessage } from 'naive-ui'

export default {
    setup() {
    let messageStore = useMessageStore()
    const message = useMessage()

    messageStore.$subscribe((mutation, state) => {
      if (state.type === 'nfo') {
        message.info(state.message)
      } else if (state.type === 'success') {
        message.success(state.message)
      } else if (state.type === 'warning') {
        message.warning(state.message)
      } else if (state.type === 'error') {
        message.error(state.message)
      }
    })
  },
  components: {
    NMessageProvider
  }
}
</script>
<template>
  
</template>