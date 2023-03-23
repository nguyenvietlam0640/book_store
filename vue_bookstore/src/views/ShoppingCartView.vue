<template>
    <div class="con">
        <div class="header-2">
            <div style="width: inherit; height: 75px;"></div>
        </div>


        <div class="shopping-cart-container">
            <div class="header">
                <h4 class="title"><strong>Shopping Cart</strong></h4>
                <a href="/past_orders">View past orders</a>
            </div>
            <div v-if="!cart.items.length" class="cart-table">
                <h2 class="empty-message">
                    <hr>
                    <strong>Shopping cart is empty</strong>
                    <hr>
                </h2>

            </div>
            <div v-if="cart.items.length" class="cart-table">
                <div class="describle-row">
                    <div class="column-1">
                        <h5>Product Detail</h5>
                    </div>
                    <div class="column-2">
                        <h5>Quantity</h5>
                    </div>
                    <div class="column-3">
                        <h5>Price</h5>
                    </div>

                </div>
                <div class="items-row" v-for="(item, index) in cart.items" :key="index">
                    <div class="column-1">
                        <h5 class="title">{{ item.book.title }}<br><span>{{ item.book.author }}</span></h5>

                    </div>
                    <div class="column-2">
                        <div class="quantity">
                            <h4>{{ item.quantity }}</h4>
                        </div>
                        <div class="adjustable-arrow">
                            <div><i v-on:click="increase(item.book.id)" class="fa-solid fa-angle-up"></i></div>
                            <div><i v-on:click="decrease(item.book.id)" class="fa-solid fa-angle-down"></i></div>
                        </div>
                        <img v-on:click="delete_item(item.book.id)" class="delete-icon"
                            src="../assets/img/icon/delete-icon.png">
                    </div>
                    <div class="column-3">
                        <h4 class="price"><strong>${{ item.book.unit_price }}</strong>

                        </h4>
                    </div>
                </div>
                <div class="subtotal-row">
                    <div class="column-1"></div>
                    <div class="column-2">
                        <h3 class="title">SUBTOTAL</h3>
                    </div>
                    <div class="column-3">
                        <h4 class="price"><strong>${{ get_cart_total_price }}</strong></h4>
                    </div>
                </div>
                <hr>
                <div class="delivery-row">
                    <div class="column-1"></div>
                    <div class="column-2">

                        <h3 class="title">delivery</h3>


                    </div>
                    <div class="column-3">

                        <h4 class="price"><strong>$5</strong></h4>


                    </div>
                </div>
                <div class="total-row">
                    <div class="column-1"></div>
                    <div class="column-2">
                        <h3 class="title">TOTAL</h3>
                    </div>
                    <div class="column-3">
                        <h2 class="price"><strong>${{ (parseFloat(get_cart_total_price) + 5).toFixed(2) }}</strong></h2>
                    </div>

                </div>
            </div>
            <div class="footer">
                <a href="/">Continue Shopping</a>



                <button v-on:click="create_checkout_session" v-if="cart.items.length" class="btn">Checkout</button>

            </div>


        </div>
    </div>
</template>
<script>

import axios from 'axios'

import { mapGetters } from 'vuex'
export default {

    name: 'ShoppingCartView',
    data() {
        return {
            hello: 'haha',
            categories: [],
            email: '',
            errors: []
        }
    },
    computed: {
        ...mapGetters(['cart']),
        get_cart_total_length() {
            let total_length = 0
            for (let i = 0; i < this.cart.items.length; i++) {
                total_length += this.cart.items[i].quantity
            }
            return total_length
        },
        get_cart_total_price() {

            let total_price = 0
            for (let i = 0; i < this.cart.items.length; i++) {
                total_price += this.cart.items[i].book.unit_price * parseInt(this.cart.items[i].quantity)
            }
            return total_price === 0 ? total_price : total_price.toFixed(2)
        }
    },
    created() {
        this.$store.dispatch('initalize_cart')

    },
    mounted() {

    },
    methods: {
        create_checkout_session() {
            axios
                .post('/create_checkout_session', this.cart)
                .then(response => {
                    window.location.href = response.data.checkout_session_url
                })
                .catch(error => {
                    console.log(error)
                })
        },
        decrease(id) {
            this.$store.dispatch('decrease_item', id)
        },
        increase(id) {
            this.$store.dispatch('increase_item', id)
        },
        delete_item(id) {
            this.$store.dispatch('delete_item', id)
        }
    }
}
</script>