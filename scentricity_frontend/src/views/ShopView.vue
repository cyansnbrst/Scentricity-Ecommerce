<template>
  <div class="product-container">
    <ProductCard v-for="product in productList" :key="product.id" :product="product"/>
  </div>
</template>

<script>
import ProductCard from "@/components/ProductCard.vue";

export default {
  data() {
    return {
      productList: [],
    }
  },
  components: {
    ProductCard
  },
  created() {
    this.loadProductList();
  },
  watch: {
    '$route.query': {
      handler: 'loadProductList',
      immediate: true
    }
  },
  methods: {
    async loadProductList() {
      try {
        let url = `${this.$store.getters.getServerUrl}/products/`;
        const { param, value } = this.$route.query;
        if (param && value) {
          url += `?${param}=${value}`;
        }
        this.productList = await (await fetch(url)).json();
      } catch (error) {
        console.error('Error loading product list:', error);
      }
    }
  }
};
</script>


<style scoped>
.product-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>