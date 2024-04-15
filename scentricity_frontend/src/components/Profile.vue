<template>
  <div v-if="user" class="user-container">
    <h2>Hello, {{user.username}}! <button @click="logout" class="logout-button">Logout</button></h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: null
    }
  },
  created() {
    this.getUserInfo();
  },
  methods: {
    async getUserInfo() {
      this.user = await fetch(`${this.$store.getters.getServerUrl}/auth/users/me/`, {
        headers: {
          'Authorization': `Token ${this.$store.state.authToken}`
        }
      }).then(response => response.json());
      console.log(this.user);
    },
    logout() {
      fetch(`${this.$store.getters.getServerUrl}/auth/token/logout/`, {
        method: 'POST',
        headers: {
          'Authorization': `Token ${this.$store.state.authToken}`
        }
      });
      localStorage.removeItem('auth_token');
      this.$store.commit('clearAuthToken');
    }
  }
}
</script>

<style scoped>
.user-container {
  text-align: center;
  margin-top: 20px;
}

.logout-button {
  background-color: #dc3545;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.logout-button:hover {
  background-color: #c82333;
}
</style>