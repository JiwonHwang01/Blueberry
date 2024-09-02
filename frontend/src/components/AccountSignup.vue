<template>
    <div>
      <form @submit.prevent="signup">
        <div>
          <label for="username">사용자 이름</label>
          <input type="text" v-model="username" id="username" placeholder="Username" required />
          <p v-if="errors.username">{{ errors.username }}</p>
        </div>
        <div>
          <label for="password1">비밀번호</label>
          <input type="password" v-model="password1" id="password1" placeholder="Password" required />
        </div>
        <div>
          <label for="password2">비밀번호 확인</label>
          <input type="password" v-model="password2" id="password2" placeholder="Password Again" required />
          <p v-if="errors.password2">{{ errors.password2 }}</p>
        </div>
      <button type="submit">회원가입</button>
      </form>
    </div>
  </template>
  
  <script>
  
  export default {
    data() {
      return {
        username: '',
        password1: '',
        password2: '',
        errors: {},
      };
    },
    methods: {
      signup() {
        this.$store.dispatch('signup', {
          username: this.username,
          password1: this.password1,
          password2: this.password2,
        })
        .then(() => {
          this.$router.push('/home'); // 회원가입 후 메인 페이지로 이동
        })
        .catch(error => {
          if (error.response && error.response.data) {
            this.errors = error.response.data;
          }
        });
      },
    }
  }
  </script>