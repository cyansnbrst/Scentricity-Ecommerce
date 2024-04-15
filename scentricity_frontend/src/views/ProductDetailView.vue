<template>
  <div>
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <p>Successfully added to the cart!</p>
        <button @click="showModal = false">Close</button>
      </div>
    </div>
    <div v-if="product" class="product-detail">
      <div class="product-image">
        <img :src="product.image" alt="product-image">
      </div>
      <div class="product-info">
        <p class="product-category" @click="goToShop('category', product.category.id)">{{ product.category.name }}</p>
        <h2 class="product-name">{{ product.name }}</h2>
        <p class="product-brand" @click="goToShop('brand', product.brand.id)">by {{ product.brand.name }}</p>
        <p class="product-price">Price: ${{ product.price }}</p>
        <div class="additional-info">
          <template v-if="product.properties">
            <div v-for="property in product.properties" :key="property.property_name" class="property">
              <p class="property-name">{{ property.property_name }}:</p>
              <p class="property-value">{{ property.value_as_type }}</p>
            </div>
          </template>
        </div>
        <div v-if="isLoggedIn">
          <button @click="addToCart(product.id)">Add to Cart</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>

import {mapGetters} from "vuex";

export default {
  data() {
    return {
      product: null,
      showModal: false
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  created() {
    this.loadProductDetails();
  },
  methods: {
    async loadProductDetails() {
      const productId = this.$route.params.id;
      this.product = await fetch(
          `${this.$store.getters.getServerUrl}/products/${productId}/`
      ).then(response => response.json());
    },
    goToShop(param, value) {
      this.$router.push({path: '/shop', query: {param: param, value: value}});
    },
    addToCart(product_id) {
      this.$store.dispatch('changeCart', {product_id, action: "add"});
      this.showModal = true;
    }
  }
};
</script>

<style scoped>
.product-detail {
  display: flex;
  justify-content: center;
  align-items: center;
}

.product-image img {
  max-height: 450px;
}

.product-category {
  font-size: 14px;
  color: #666;
  cursor: pointer;
}

.product-category:hover,
.product-brand:hover {
  color: #007bff;
}

.product-name {
  font-size: 24px;
  margin: 10px 0;
}

.product-brand {
  font-size: 16px;
  cursor: pointer;
}

.product-price {
  font-size: 18px;
  margin-bottom: 20px;
}

.additional-info {
  margin-top: 20px;
}

.property {
  display: flex;
  margin-bottom: 10px;
}

.property-name {
  font-weight: bold;
  margin-right: 10px;
}

.property-value {
  color: #666;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.modal button {
  margin-top: 10px;
}
</style>
