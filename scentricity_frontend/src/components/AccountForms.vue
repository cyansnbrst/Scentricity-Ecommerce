<template>
  <div class="auth-form">
    <h2 v-if="isRegister" class="auth-title">Registration</h2>
    <h2 v-else class="auth-title">Login</h2>
    <input v-model="username" type="text" class="auth-input" placeholder="Username">
    <input v-model="password" type="password" class="auth-input" placeholder="Password">
    <div v-if="isRegister" class="auth-button-container">
      <button @click="registerUser" class="auth-button">Register</button>
    </div>
    <div v-else class="auth-button-container">
      <button @click="loginUser" class="auth-button">Login</button>
    </div>
    <div v-if="successMessage" class="auth-message success">
      <p>{{ successMessage }}</p>
    </div>
    <div v-else-if="errorMessage" class="auth-message error">
      <p>{{ Object.keys(errorMessage)[0] }}: {{ Object.values(errorMessage)[0][0] }}</p>
    </div>
    <p class="auth-link">
      {{ isRegister ? "Already have an account?" : "Don't have an account yet?" }}
      <span @click="toggleForm" class="auth-toggle">{{ isRegister ? "Login" : "Register" }}</span>
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isRegister: false,
      username: '',
      password: '',
      errorMessage: '',
      successMessage: ''
    };
  },
  methods: {
    async registerUser() {
      try {
        const response = await fetch(`${this.$store.getters.getServerUrl}/auth/users/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          })
        });
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(JSON.stringify(errorData));
        } else {
          this.successMessage = 'You have successfully registered. You can now log in.';
        }
      } catch (error) {
        console.error('Error:', error);
        this.errorMessage = JSON.parse(error.message);
      }
    },
    async loginUser() {
      try {
        const response = await fetch(`${this.$store.getters.getServerUrl}/auth/token/login/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          })
        });
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(JSON.stringify(errorData));
        } else {
          this.successMessage = 'You have successfully logged in';
          const data = await response.json();
          await this.$store.commit('setAuthToken', data.auth_token);
          await localStorage.setItem('token', data.auth_token);
        }
      } catch (error) {
        console.error('Error:', error);
        this.errorMessage = JSON.parse(error.message);
      }
    },
    toggleForm() {
      this.isRegister = !this.isRegister;
      this.errorMessage = '';
      this.successMessage = '';
    }
  }
};
</script>

<style scoped>
.auth-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 50px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.auth-title {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
}

.auth-input {
  width: 95%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.auth-button-container {
  text-align: center;
}

.auth-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.auth-button:hover {
  background-color: #0056b3;
}

.auth-message {
  padding: 10px;
  margin-top: 10px;
  border-radius: 5px;
}

.success {
  background-color: #d4edda;
  color: #155724;
  border-color: #c3e6cb;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
  border-color: #f5c6cb;
}

.auth-link {
  text-align: center;
  margin-top: 20px;
}

.auth-toggle {
  color: #007bff;
  cursor: pointer;
}

.auth-toggle:hover {
  text-decoration: underline;
}

</style>
