<script lang="ts">
import { NCard, NButton, NSpace, NAvatar, NSwitch, NIcon, NInput, NModal, c } from 'naive-ui';
import { useThemeStore } from '@/stores/theme';
import { Sunny as LightIcon, Moon as DarkIcon } from '@vicons/ionicons5';
import { useUserStore } from '@/stores/user';
import { useMessageStore } from '@/stores/message';
import { userUpdate } from '@/services/userService';
import { restartApp } from '@/services/appService';

export default {
  emits: [
    'update:settings'
  ],
  components: {
    NCard,
    NButton,
    NSpace,
    NAvatar,
    NSwitch,
    LightIcon,
    DarkIcon,
    NIcon,
    NInput,
    NModal
  },
  setup() {
    const themeStore = useThemeStore()
    const userStore = useUserStore()
    const messageStore = useMessageStore()
    return {
      themeStore,
      userStore,
      messageStore
    }
  },
  data() {
    return {
      themes: [
        {
          name: 'Pink',
          value: 'pink',
          color: '#ff80aa'
        },
        {
          name: 'Blue',
          value: 'blue',
          color: '#33cbff'
        },
        {
          name: 'Green',
          value: 'green',
          color: '#5cd65c'
        }
      ],
      showCreateUserModal: false,
      newUsername: '',
      newPassword: '',
      newPasswordAgain: ''
    }
  },
  methods: {
    async emitUpdateSettings() {
      this.$emit('update:settings')
    },
    async updateUser() {
      if (this.newUsername === "") {
        this.messageStore.setMessage("用户名不能为空", "error")
        return
      }
      if (this.newPassword === "") {
        this.messageStore.setMessage("密码不能为空", "error")
        return
      }
      if (this.newPassword !== this.newPasswordAgain) {
        this.messageStore.setMessage("两次输入的密码不一致", "error")
        return
      }
      let { data } = await userUpdate(this.newUsername, this.newPassword)
      if (data.success) {
        this.messageStore.setMessage("用户更新成功, 请重新登陆", "success")
        this.showCreateUserModal = false
        this.userStore.logout()
        this.$router.push("/login")
      } else {
        this.messageStore.setMessage(data.message!, "error")
      }
    
    },
    logoutUser() {
      this.userStore.logout()
      this.messageStore.setMessage("已退出登录", "success")
      this.$router.push("/login")
    },
    async restartBackend() {
      try{
        await restartApp()
      } catch (e) {
        
      }
      this.messageStore.setMessage("Madokami后端已重启", "success")
      setTimeout(() => {
        location.reload()
      }, 2000)
    }
  },
  watch: {
    'themeStore.dark': {
      handler: function (val) {
        this.themeStore.setDark(val)
      },
      immediate: true
    }
  }
}

</script>
<template>
    <NCard size="medium" title="通用设置">
        <template #header-extra>
            <NSpace justify="end">
                <NButton type="error" size="small" @click="restartBackend">重启</NButton>
                <NButton type="primary" size="small" @click="emitUpdateSettings">保存</NButton>
            </NSpace>
            
        </template>
        <NCard size="small" title="主题设置">
          <template #header-extra>
            <NSwitch v-model:value="themeStore.dark">
              <template #checked-icon>
                <NIcon>
                  <DarkIcon />
                </NIcon>
              </template>
              <template #unchecked-icon>
                <NIcon>
                  <LightIcon />
                </NIcon>
              </template>
            </NSwitch>
          </template>
            <NSpace>
                <div v-for="theme in themes" :key="theme.name">
                    <NAvatar :style="{ backgroundColor: theme.color }" @click="themeStore.setTheme(theme.value)"/>
                    <!-- <p>{{ theme.name }}</p> -->
                </div>
            </NSpace>
        </NCard>
        <NCard size="small" title="账号设置" style="margin-top: 10px;">
          <NSpace justify="start">
            <NButton type="primary" @click="showCreateUserModal = true">更新用户</NButton>
            <NButton @click="logoutUser">退出登录</NButton>
          </NSpace>
        </NCard>
    </NCard>
    <NModal class="modal" v-model:show="showCreateUserModal">
      <NCard size="small" title="更新用户">
        <div class="input-container">
          <NInput placeholder="用户名" v-model:value="newUsername"/>
          <NInput placeholder="密码" type="password" v-model:value="newPassword"/>
          <NInput placeholder="请再次输入密码" type="password" v-model:value="newPasswordAgain"/>
        </div>
        <template #action>
          <NSpace justify="end">
            <NButton @click="showCreateUserModal = false">取消</NButton>
            <NButton type="primary" @click="updateUser">创建</NButton>
          </NSpace>
        </template>
      </NCard>
    </NModal>

</template>

<style scoped>
.modal {
  width: 300px;
}
.input-container {
  width: 100%;
  display: grid;
  row-gap: 5px;
}

</style>