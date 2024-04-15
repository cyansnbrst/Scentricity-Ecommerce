<template>
  <div class="account-container">
    <template v-if="!isLoggedIn">
      <AccountForms></AccountForms>
    </template>
    <template v-else>
      <div class="profile-section">
        <Profile></Profile>
      </div>
      <div class="orders-section">
        <router-link to="/orders" class="link">My Orders</router-link>
      </div>
      <div class="cart-section">
        <Cart></Cart>
      </div>
    </template>
  </div>
</template>

<script>
import AccountForms from "@/components/AccountForms.vue";
import Cart from "@/components/Cart.vue";
import {mapGetters} from "vuex";
import ProductCard from "@/components/ProductCard.vue";
import Profile from "@/components/Profile.vue";

export default {
  components: {
    Profile,
    ProductCard,
    AccountForms,
    Cart
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  }
};
</script>

<style scoped>
.account-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.profile-section {
  margin-bottom: 20px;
}

.orders-section .link {
  color: #007bff;
  text-decoration: none;
}

.cart-section {
  margin-top: 20px;
}
</style>