<script>
import LoginBox from '../components/LoginBox.vue';

export default {
  components: {
    LoginBox
  }
}

</script>

<template>

  <div class="about">
    <LoginBox class="full-width" msg="需要登录" />
  </div>
</template>

<style scoped>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
  .full-width {
    width: 100%;
  }
}

@media screen and (max-width: 1024px) {
  .about {
    display: flex;
  }
  .full-width {
    width: 100%;
    justify-content: center;
  }
  
}
</style>
