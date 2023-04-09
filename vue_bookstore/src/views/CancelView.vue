<template>
    <Header2 :_current_category="'Category'" :_categories="categories" />
    <div class="success-container">
        <div class="border">
            <div class="fail-icon"><i class="fa-sharp fa-regular fa-circle-xmark"></i></div>
            <h3 class="fail-title">Your checkout order has been cancelled</h3>
        </div>
        <div class="past-orders"><a v-on:click="view_past_orders">view past orders</a></div>
    </div>
</template>



<script>
import Header2 from '@/components/Header-2.vue';
import axios from 'axios';
export default {
    name: 'CancelView',
    data() {
        return {
            categories: [],
        }
    },
    components: {
        Header2,
    },
    mounted() {
        this.get_categories()
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
        view_past_orders() {
            if (this.user) {
                window.location.href = '/past_orders'
            }
            else {
                alert('login to view your past orders')
            }

        },
    },

}
</script>