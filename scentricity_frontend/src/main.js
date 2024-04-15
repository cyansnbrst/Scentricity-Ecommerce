import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from "./store";


// const token = localStorage.getItem('token');
// if (token) {
//     store.commit('setAuthToken', token);
// }

createApp(App).use(router).use(store).mount('#app')
