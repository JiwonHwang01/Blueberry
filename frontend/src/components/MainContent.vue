<template>
    <div>
        <div v-if="!isAuthenticated">
          <router-link v-if="!showForm"  to="/signup" @click="showForm = true">가입</router-link>
          <router-link v-if="!showForm" to="/login" @click="showForm = true">로그인</router-link>
        </div>
        <a v-else @click="logout">로그아웃</a>
    </div>
    
    <main>
        <p v-if="isAuthenticated">Welcome, {{ user }}!</p>
        <slot></slot>
    </main>
</template>

<script>
export default {
  data() {
    return {
      showForm: false,
    };
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    user() {
      return this.$store.getters.user;
    }
  },
  methods: {
    logout() {
      this.showForm=true
      this.$store.dispatch('logout');
      this.$router.push('/home');
    }
  }
  
};
</script>

<style scoped>
/* Content와 관련된 스타일을 여기에 추가 */
main {
  padding: 20px;
  background-color: #f9f9f9;
  min-height: calc(100vh - 60px); /* Header와 Footer 높이를 제외한 영역 */
}
</style>