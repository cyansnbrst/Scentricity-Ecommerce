<template>
  <Nav/>
  <router-view/>
  <Footer/>
</template>

<style>
@import "assets/css/styles.css";
</style>

<script>
import Nav from "@/components/Nav.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: {Nav, Footer}
}
</script>
