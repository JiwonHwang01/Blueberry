import { createRouter, createWebHistory } from 'vue-router';
import Signup from '@/components/AccountSignup.vue';
import Login from '@/components/AccountLogin.vue';

const routes = [
    { path: '/home', redirect:'/' },
    { path: '/login', component: Login },
    { path: '/signup', component: Signup },
  ];
  
const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  export default router;

