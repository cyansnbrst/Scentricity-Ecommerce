<template>
  <div class="home">
    <section class="hero">
      <div class="hero-content">
        <h2>Welcome to Scentricity</h2>
        <p>Find your perfect scent with us.</p>
        <router-link to="/shop" class="btn">Shop Now</router-link>
      </div>
    </section>
  </div>
</template>

<style scoped>
.hero {
  background-image: url('hero-bg.jpg');
  background-size: cover;
  background-position: center;
  height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-content {
  text-align: center;
  color: #fff; /* белый текст на фоне изображения */
}

.btn {
  background-color: #8046a2; /* темно-сиреневый */
  color: #fff; /* белый текст */
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #5a2d6b; /* темно-сиреневый при наведении */
}

.home {
  margin: -20px;
}
</style>
