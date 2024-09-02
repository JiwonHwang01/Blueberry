import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import router from './router'
import axios from 'axios';
import store from './store';


loadFonts()

const app = createApp(App)
app.use(router)
app.use(vuetify)
app.use(store)
app.mount('#app')

axios.interceptors.response.use(
  response => response,
  async error => {
    if (error.response.status === 401) {
      try {
        await store.dispatch('refresh');
        error.config.headers['Authorization'] = `Bearer ${store.state.token}`;
        return axios.request(error.config);
      } catch (refreshError) {
        store.dispatch('logout');
      }
    }
    return Promise.reject(error);
  }
);
