<template>
  <div>
    <div class="cart">
      <div v-if="cart === null || cart.items.length===0" class="empty-cart">Cart is empty</div>
      <div v-else>
        <div class="cart-item cart-header">
          <div>Product</div>
          <div>Quantity</div>
          <div>Subtotal</div>
        </div>
        <div v-for="(item, index) in cart.items" :key="index" class="cart-item">
          <div v-if="item.details" class="item-details">
            <div class="product">
              <img :src="item.details.image" alt="product-image">
              <p class="product-name">{{ item.details ? item.details.name : '' }}</p>
            </div>
            <div class="amount">
              <span @click="deleteFromCart(item.details.id)" class="quantity-adjust">-</span>
              {{ item.quantity }}
              <span @click="addToCart(item.details.id)" class="quantity-adjust">+</span>
            </div>
            <div class="subtotal">{{ item.subtotal }}</div>
          </div>
          <div class="close" @click="deleteItem(item.details.id)">X</div>
        </div>
        <p class="total">Total: {{ cart.total_price }}</p>
        <div class="checkout-button-wrapper">
          <button @click="orderFromCart()" class="checkout-button">Checkout</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      cart: null
    }
  },
  mounted() {
    this.loadCart();
  },
  methods: {
    async loadCart() {
      await fetch(`${this.$store.getters.getServerUrl}/cart/`, {
        method: 'GET',
        headers: {
          'Authorization': `Token ${this.$store.state.authToken}`
        }
      }).then(response => response.json())
          .then(data => {
            this.cart = data;
            this.loadProductDetails(this.cart.items);
          })
          .catch(error => {
            console.error('Error fetching a cart:', error);
          });
    },
    async loadProductDetails(products) {
      const promises = products.map(item => {
        return fetch(`${this.$store.getters.getServerUrl}/products/${item.product}/`, {
          method: 'GET',
          headers: {
            'Authorization': `Token ${this.$store.state.authToken}`
          }
        }).then(response => {
          if (!response.ok) {
            throw new Error(`Error while loading a product: ${item.product}`);
          }
          return response.json();
        }).catch(error => {
          console.error('Error while loading a product:', error);
          return null;
        });
      });

      Promise.all(promises).then(productDetails => {
        productDetails.forEach((details, index) => {
          if (details !== null) {
            products[index].details = details;
          }
        });
      });
    },
    async addToCart(product_id) {
      await this.$store.dispatch('changeCart', {product_id, action: "add"});
      await this.loadCart();
    },
    async deleteFromCart(product_id) {
      await this.$store.dispatch('changeCart', {product_id, action: "delete"});
      await this.loadCart();
    },
    async deleteItem(product_id) {
      await fetch(
          `${this.$store.getters.getServerUrl}/cart/delete/${product_id}/`, {
            method: 'DELETE',
            headers: {
              'Authorization': `Token ${this.$store.state.authToken}`
            }
          }).then(response => response);
      await this.loadCart();
    },
    async orderFromCart() {
      try {
        const response = await fetch(
            `${this.$store.getters.getServerUrl}/payment/create_checkout_session/`, {
              method: 'POST',
              headers: {
                'Authorization': `Token ${this.$store.state.authToken}`
              }
            });
        if (response.ok)
          window.location.href = (await response.json()).url;
        else
          console.error('Ошибка при выполнении запроса:', response.status);
      } catch (error) {
        console.error('Ошибка при выполнении запроса:', error);
      }
    }

  },
};
</script>


<style scoped>
.cart {
  width: 800px;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.empty-cart {
  text-align: center;
  font-size: 18px;
}

.cart-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #eee;
  border-radius: 5px;
}

.item-details {
  flex: 2;
  display: flex;
}

.item-details div {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-basis: 33.33%;
}

.item-details img {
  width: 80px;
  height: 80px;
  margin-right: 10px;
  border-radius: 5px;
}

.product-name {
  margin: 0;
  font-size: 12pt;
}

.amount,
.subtotal {
  margin: 0 10px;
}

.total {
  margin-top: 20px;
  font-weight: bold;
  text-align: right;
  font-size: 20px;
}

.cart-header {
  font-weight: bold;
}

.cart-header > div {
  flex: 1;
  text-align: center;
}

.cart-header img {
  display: none;
}

.close {
  text-align: center;
  cursor: pointer;
  width: 20px;
}

.checkout-button-wrapper {
  display: flex;

}
.checkout-button {
  background-color: #007bff;
  margin-left: auto;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.checkout-button:hover {
  background-color: #0056b3;
}

.quantity-adjust {
  cursor: pointer;
}
</style>