<template>
    <div class="shelf-container">
        <div class="shelf-header">
            <div>
                <h5 class="shelf-label"><strong>{{ _current_category }}</strong></h5>
            </div>
            <div class="page-changer">
                <a v-bind:class="{ 'go-previous-page-non-active': !backward, 'go-previous-page-active': backward }"
                    v-on:click="go_backward()">&#60;&#60;Previous</a>&nbsp;Page: {{ current_page }} of
                {{ _page_total }}&nbsp;<a
                    v-bind:class="{ 'go-next-page-non-active': !forward, 'go-next-page-active': forward }"
                    v-on:click="go_forward()">Next&#62;&#62;</a>
            </div>
        </div>
        <div class="book-shelf">

            <div class="book-card" v-for="book in _books" v-bind:key="book.id">
                <a v-bind:href="book.get_absolute_url">
                    <img class="book-img" :src="book.get_image">
                </a>
                <div class="book-card-header">
                    <h5 class="book-title"> <a v-bind:href="book.get_absolute_url">{{ book.title }}</a></h5>
                    <h6 class="book-autor">by {{ book.author }}</h6>
                    <p class="book-des"> {{ book.des }}</p>
                    <a v-bind:href="book.get_absolute_url">more details</a>

                </div>
                <div class="book-card-footer">
                    <h5 class="book-price"><strong>${{ book.unit_price }}</strong></h5>
                    <div v-on:click="add_to_cart(book)" class="btn">
                        <h5 style="padding-top: 5px;">Add</h5>
                        <img src="../assets/img/icon/basket.png">
                    </div>
                </div>

            </div>

        </div>

        <div class="shelf-footer">

            <div class="page-changer">
                <a v-bind:class="{ 'go-previous-page-non-active': !backward, 'go-previous-page-active': backward }"
                    v-on:click="go_backward()">&#60;&#60;Previous</a>&nbsp;Page: {{ current_page }} of
                {{ _page_total }}&nbsp;<a
                    v-bind:class="{ 'go-next-page-non-active': !forward, 'go-next-page-active': forward }"
                    v-on:click="go_forward()">Next&#62;&#62;</a>
            </div>
        </div>
    </div>
</template>


<script>

import { useRoute } from 'vue-router'
import { mapGetters } from 'vuex'
export default {
    name: 'BookShelf',
    props: {
        _current_category: String,
        _books: Array,
        _page_total: Number
    },
    data() {
        return {
            current_page: 0,
            input: false,
            backward: null,
            forward: null,

        }
    },
    async mounted() {
        var route = useRoute()
        this.current_page = route.params.page
        this.input = this.$route.query.input
        this.id = this.$route.query.id
        this.backward_status()
        setTimeout(() => {
            this.forward_status()
        }, 1000);
        

    },
    computed:{
        ...mapGetters(['cart'])
    },
    methods: {
        add_to_cart(book){
            const item = {
                book: book,
                quantity: 1
            }
            this.$store.dispatch('add_to_cart', item)
            console.log(this.cart.items.length)
        },
        backward_status() {
            if (this.current_page == 1) {
                this.backward = false
            }
            else {
                this.backward = true
            }

        },
        forward_status() {
            if (this.current_page == parseInt(this._page_total)) {
                this.forward = false

            }
            else {
                this.forward = true
            }
        },
        go_backward() {
            if (this.current_page == 1) {

            }
            else {
                this.current_page = this.current_page - 1
                this.change_page()
            }

        },
        go_forward() {
            if (this.current_page == parseInt(this._page_total)) {

            }

            else {
                this.current_page = parseInt(this.current_page) + 1
                this.change_page()
            }
        },
        change_page() {
            let params = this.$route.params
            params['page'] = this.current_page

            console.log(this.input)
            console.log(this.id)
            if (this.input) {
                if (this.id == null) {
                    window.location.href = this.current_page + `?id=null&input=${this.input}`
                }
                else {
                    window.location.href = this.current_page + `?id=${this.id}&input=${this.input}`
                }

            }
            else {
                window.location.href = this.current_page
            }
        }
    }
}

</script>