<template>
    <Header2 :_current_category="'Category'" :_categories="categories" />
    <div v-if="!fail" class="success-container">
        <div class="border">
            <div class="success-icon"><i class="fa-regular fa-circle-check"></i></div>
            <h4 class="success-title">Your puschare has been successed</h4>
        </div>
        <div class="past-orders"><a href="/view_past_orders">view past orders</a></div>
    </div>

    <div v-if="fail" class="success-container">
        <div class="border">
            <div class="fail-icon"><i class="fa-sharp fa-regular fa-circle-xmark"></i></div>
            <h3 class="fail-title">{{ message }}</h3>
        </div>
        <div class="past-orders"><a href="/past_orders">view past orders</a></div>
    </div>
</template>


<script>
import axios from 'axios';
import Header2 from '@/components/Header-2.vue';

export default {
    name: 'SuccessView',
    data() {
        return {
            categories: [],
            fail: false,
            message: 'invalid token'
        }
    },
    components: {
        Header2,
    },

    async mounted() {
        const token = this.$route.query.order
        await this.get_categories()
        await this.check_order_session(token)
    },
    methods: {
        async check_order_session(token) {
            if (token) {
                await axios
                    .post('/api/check_order_session', { token: token })
                    .then(response => {
                        this.fail = false
                        this.message = response.data
                        this.$store.dispatch('empty_cart')
                    })
                    .catch(error => {
                        this.fail = true
                        this.message = error.response.data.message
                    })
            }
            else {
                this.fail = true
            }
        },
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
    },
}
</script>