<template>
  <div class="my-orders-container">
    <h2 class="orders-title">My Orders</h2>
    <div v-if="orders" class="orders-list">
      <div v-for="order in orders" :key="order.id" class="order-item">
        <div class="order-info">
          <p class="info-value">Order №{{ order.id }}</p>
          <p class="info-value">{{ formatTimestamp(order.created) }}</p>
        </div>
        <div class="order-info">
          <p class="info-label">Total:</p>
          <p class="info-value">{{ order.total }}</p>
        </div>
      </div>
    </div>
    <div v-else>
      <p class="no-orders">No orders found</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      orders: null
    }
  },
  mounted() {
    this.loadOrders();
  },
  methods: {
    formatTimestamp(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleString();
    },
    async loadOrders() {
      await fetch(`${this.$store.getters.getServerUrl}/order/my_orders/`, {
        method: 'GET',
        headers: {
          'Authorization': `Token ${this.$store.state.authToken}`
        }
      }).then(response => response.json())
          .then(data => {
            this.orders = data;
          })
          .catch(error => {
            console.error('Error fetching orders:', error);
          });
    },
  }
}
</script>

<style scoped>
.my-orders-container {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
}

.orders-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.orders-list {
  display: flex;
  flex-direction: column;
}

.order-item {
  border-bottom: 1px solid #ccc;
  padding: 20px 0;
}

.order-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.info-label {
  font-weight: bold;
  margin-right: 10px;
}

.info-value {
  font-size: 16px;
}

.no-orders {
  font-size: 18px;
  text-align: center;
  margin-top: 20px;
  color: #666;
}

</style>