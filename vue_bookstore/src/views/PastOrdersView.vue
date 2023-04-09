<template>
    <Header2 :_current_category="'Category'" :_categories="categories" />
    <div v-if="orders.length && !is_loading" class="past-orders-container">
        <div class="header">
            <h4 class="title"><strong>Past Orders</strong></h4>
        </div>
        <div v-for="order in orders" :key="order.order.id" class="order-card">
            <div class="order-infomation">
                <div>
                    <div class="order-placed">Order placed</div>
                    <div class="date">{{ order.order.order_date }}</div>
                </div>
                <div>
                    <div class="recipient">Recipent: {{ user.full_name }}</div>
                    <div class="total">Total: <span>$ {{ order.order.total_amount }}</span></div>
                </div>
            </div>
            <div class="order-lines">
                <div v-for="order_line in order.order_lines" :key="order_line.id" class="order-line">
                    <div v-on:click="view_book_detail(order_line.get_url)" class="title">
                        {{ order_line.get_book_title }}<span class="author"> by {{ order_line.get_book_author }}</span>
                    </div>
                    <div class="quantity">x{{ order_line.quantity }}</div>
                    <div class="total">${{ order_line.unit_price }}</div>
                </div>
            </div>
        </div>
    </div>
    <div v-if="!orders.length && !is_loading" class="past-orders-container">
        <div class="header">
            <h4 class="title"><strong>Past Orders</strong></h4>
        </div>
        <div class="order-card">
            <h3 class="no-order">--- No order yet ---</h3>
        </div>
    </div>
</template>


<script>
import Header2 from '@/components/Header-2.vue';
import axios from 'axios';
import { mapGetters } from 'vuex';
export default {
    name: 'PastOdersView',
    data() {
        return {
            categories: [],
            orders: []
        }
    },
    components: {
        Header2,
    },
    computed: {
        ...mapGetters(['user']),
        ...mapGetters(['is_loading'])
    },
    async mounted() {
        await this.$store.dispatch('set_loading', true)
        await this.get_categories()
        await this.get_past_orders()
        await this.$store.dispatch('set_loading', false)
    },
    methods: {
        async get_categories() {
            await axios
                .get('/api/view_categories')
                .then(response => {
                    this.categories = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async get_past_orders() {
            await axios
                .post('/api/past_orders', { user_id: this.user.id })
                .then(response => {
                    console.log(response.data)
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        view_book_detail(url) {
            window.location.href = `${url}`
        }
    },
}

</script>