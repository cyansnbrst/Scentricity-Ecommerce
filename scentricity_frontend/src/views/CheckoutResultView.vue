<template>
  <div>
    <div v-if="successMessage">
      {{ successMessage }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      successMessage: ''
    }
    },
  created() {
    if (this.$route.query.canceled) {
      this.$router.push('/account');
    }
    else if (this.$route.query.success) {
      this.successMessage = 'Successful!';
      setTimeout(() => {
        this.$router.push('/orders');
      }, 2000);
    }
  }
}
</script>

<style scoped>

</style>