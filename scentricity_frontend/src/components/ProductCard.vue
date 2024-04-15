<template>
  <div class="product-card">
    <router-link :to="'/product/' + product.id">
      <img :src="product.image" alt="product-image">
    </router-link>
    <h3>{{ product.name }} by {{ product.brand.name }}</h3>
    <p class="price">Price: {{ product.price }}</p>
  </div>
</template>

<script>
export default {
  props: {
    product: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
.product-card {
  width: 280px;
  height: 350px;
  border-radius: 12px;
  padding: 20px;
  margin: 20px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease;
}

.product-card:hover {
  transform: scale(1.05);
}

.product-card img {
  width: 100%;
  height: 80%;
  object-fit: cover;
  border-radius: 8px;
}

.product-card h3 {
  font-size: 18px;
  margin-top: 10px;
  margin-bottom: 5px;
  color: #333;
}

.product-card p {
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}

.product-card p.price {
  font-weight: bold;
  margin-top: 0;
}
</style>
