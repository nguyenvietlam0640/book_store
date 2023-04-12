<template>
    <div class="header-2">
        <div class="search-group">
            <div class="search-bar-container">
                <div class="search-bar">
                    <input id="search-input" type="search" placeholder="autor, title">
                    <div class="btn" data-bs-toggle="dropdown">
                        <div>all&nbsp;categories</div><img src="../assets/img/icon/black-dropdown.png">
                    </div>
                    <ul class="dropdown-menu dropdown-menu-end">
                        <li class="menu-list" v-for="category in _categories" v-bind:key="category.id">
                            <a v-on:click="_pass_category(category.name, category.id)">{{ category.name }}</a>
                        </li>
                    </ul>
                </div>
                <img v-on:click="_search(_id_to_search)" src="../assets/img/icon/search.png">
            </div>

            <div class="category-dropdown">
                <button class="btn" data-bs-toggle="dropdown">
                    <!---->
                    <div class="category-title">{{ _current_category }}</div>
                    <img src="../assets/img/icon/white-dropdown.png">
                </button>
                <ul class="dropdown-menu">
                    <li class="menu-list" v-for="category in _categories" v-bind:key="category.id">

                        <a v-bind:href="category.get_absolute_url + `/${books_per_page}/1`">{{ category.name }}<span>({{
                            category.get_books_total
                        }})</span></a>
                    </li>
                </ul>
            </div>
        </div>

        <div class="basket-dropdown">
            <div class="btn" data-bs-toggle="dropdown" data-bs-auto-close="outside">
                <div class="basket-content">
                    <img src="../assets/img/icon/basket.png">
                    <h5 class="px-2">basket(${{ get_cart_total_price }})</h5>
                </div>
                <div class="quantity">
                    <h3><strong>{{ get_cart_total_length }}</strong></h3>
                </div>

                <img src="../assets/img/icon/white-dropdown.png">
            </div>
            <!-- problem -->

            <!-- problem -->
            <div class="dropdown-menu">
                <div v-if="!cart.items.length">
                    <div class="total">
                        <div>cart is empty</div>
                    </div>
                    <div class="footer-container">
                        <a v-on:click="view_past_orders">View part orders</a>
                    </div>
                    
                </div>
                <div v-if="cart.items.length">
                    <div class="item-card" v-for="(item, index) in cart.items" :key="index">
                        <div class="book-title">
                            {{ item.book.title }}
                        </div>
                        <div class="quantity">
                            {{ item.quantity }}
                        </div>
                        <div class="unit-price">
                            ${{ item.book.unit_price.toFixed(2) }}
                        </div>
                        <div class="quantity-button">
                            <i v-on:click="decrease(item.book.id)" class="fa-solid fa-minus"></i>
                            <i v-on:click="increase(item.book.id)" class="fa-solid fa-plus"></i>
                        </div>
                    </div>

                    <div class="total">
                        <div class="title">Total</div>
                        <div class="quantity">{{ get_cart_total_length }}</div>
                        <div class="price">${{ get_cart_total_price }}</div>
                    </div>

                    <div class="footer-container">
                        <div class="basket-button">
                            <button v-on:click="go_to_cart()">
                                Go to cart
                            </button>
                            <button v-on:click="empty_cart">Empty Cart</button>
                        </div>
                        <a v-on:click="view_past_orders">View past orders</a>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>





<script>
import { useRoute } from 'vue-router'
import { mapGetters } from 'vuex'
export default {
    name: 'Header2',
    props: {
        _current_category: String,
        _categories: Array,
    },
    data() {
        return {

            _id_to_search: null,
            books_per_page: 0,

        }
    },

    mounted() {
        var route = useRoute()
        this.books_per_page = route.params.books_per_page == null ? 8 : route.params.books_per_page

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
    methods: {
        view_past_orders() {
            if (this.user) {
                window.location.href = '/past_orders'
            }
            else {
                alert('login to view your past orders')
            }

        },
        go_to_cart() {
            window.location.href = '/shopping_cart'
        },
        empty_cart() {
            if (confirm('This action will empty your shopping cart')) {
                this.$store.dispatch('empty_cart')
            }
        },
        decrease(id) {
            this.$store.dispatch('decrease_item', id)
        },
        increase(id) {
            this.$store.dispatch('increase_item', id)
        },


        _pass_category(name, id) {
            document.querySelector('#search-input').placeholder = `Search in ${name}`
            this._id_to_search = id
        },
        _search(id, input) {
            var input = document.querySelector('#search-input').value
            if (input == '') {
                alert('requirement keyword')
            }
            else {
                window.location.href = `/search/${this.books_per_page}/1?id=${id}&input=${input}`
            }
        }
    },
}
</script>