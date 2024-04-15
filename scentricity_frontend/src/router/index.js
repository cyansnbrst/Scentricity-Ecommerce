import {createRouter, createWebHashHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from "@/views/AboutView.vue";
import ShopView from "@/views/ShopView.vue";
import ProductDetailView from "@/views/ProductDetailView.vue";
import AccountView from "@/views/AccountView.vue";
import CheckoutResultView from "@/views/CheckoutResultView.vue";
import OrdersView from "@/views/OrdersView.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        component: AboutView
    },
    {
        path: '/shop',
        name: 'shop',
        component: ShopView,
        props: route => ({param: route.query.param, value: route.query.value})
    },
    {
        path: '/product/:id',
        name: 'product-detail',
        component: ProductDetailView
    },
    {
        path: '/account',
        name: 'account',
        component: AccountView
    },
    {
        path: '/checkout',
        name: 'checkout',
        component: CheckoutResultView,
    },
    {
        path: '/orders',
        name: 'orders',
        component: OrdersView,
    }

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
