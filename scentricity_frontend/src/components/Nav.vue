<template>
  <header class="header">
    <h1 class="logo">Scentricity</h1>
    <nav class="navbar">
      <ul class="nav-menu">
        <router-link to="/" class="nav-item">Home</router-link>
        <router-link to="/about" class="nav-item">About</router-link>
        <router-link to="/shop" class="nav-item" >Shop</router-link>
        <router-link to="/account" class="nav-item" >Account</router-link>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');

.header {
  background-color: #f0e6f3;
  color: #4d325f;
  padding: 20px;
  margin-top: 0;
  display: flex;
  justify-content: space-between;
}

.logo {
  font-family: 'Meow Script', cursive;
  margin: 0;
}

.nav-menu {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
}

.nav-item {
  padding: 10px;
  color: #4d325f;
  text-decoration: none;
}

.nav-item:hover {
  background-color: #d1bad1;
}

.router-link-active {
  font-weight: bold;
}
</style>
<script setup>
</script>