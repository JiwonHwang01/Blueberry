<template>
  <div id="app">
    <Header />
    <Content>
    <router-view />
    </Content>
    <Footer />
  </div>
</template>


<script>
import Header from './components/MainHeader.vue';
import Content from './components/MainContent.vue';
import Footer from './components/MainFooter.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'App',

  components: {
    Header,
    Content,
    Footer,
  },

  data: () => ({
    isAuthenticated: false,
  }),
  
  computed: {
    ...mapGetters(['user']),
    username() {
      return this.user ? this.user.username : '';
    },
  },
  
}
</script>
