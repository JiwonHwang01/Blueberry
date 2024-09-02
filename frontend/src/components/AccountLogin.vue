<template>
  <div>
    <form v-if="!isAuthenticated" @submit.prevent="login">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  </div>
</template>


<script>
import axios from 'axios';

axios.defaults.withXSRFToken = true; 
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';


export default {
  name: "AccountLogin",
  data() {
    return {
      username: '',
      password: ''
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
    login() {
    const credentials = {
      username: this.username,
      password: this.password
    };

    this.$store.dispatch('login', credentials);
    },
  }
}
</script>
