<template>

    <div class="header-2">
        <div class="search-group">
            <div class="search-bar-container">
                <div class="search-bar">
                    <input id="search-input" type="search" placeholder="autor, title">
                    <div class="btn">
                        <div>all&nbsp;categories</div><img src="../assets/img/icon/black-dropdown.png">
                    </div>
                </div>
                <a href="/login"><img src="../assets/img/icon/search.png"></a>
            </div>

            <div class="category-dropdown">
                <button class="btn" v-on:click="category_dropdown_menu_show = !category_dropdown_menu_show">
                    <!---->
                    <div class="category-title">{{ current_category.name }}</div>
                    <img src="../assets/img/icon/white-dropdown.png">
                </button>
                <ul class="category-dropdown-menu" v-if="category_dropdown_menu_show">
                    <li class="menu-list" v-for="category in categories" v-bind:key="category.id">

                        <a v-bind:href="category.get_absolute_url">{{ category.name }}<span>({{
                            category.get_number_of_books
                        }})</span></a>
                    </li>
                </ul>
            </div>
        </div>
    
        <div class="basket-dropdown">
            <div class="btn">
                <div class="basket-content">
                    <img src="../assets/img/icon/basket.png">
                    <h5 class="px-2">basket($0)</h5>
                </div>
                <div class="quantity">
                    <h3><strong>0</strong></h3>
                </div>

                <img src="../assets/img/icon/white-dropdown.png">
            </div>
        </div>
    </div>

    <div class="shelf-container">
        <div class="shelf-header">
            <div>
                <h5 class="shelf-label"><strong>{{ current_category.name }}</strong></h5>
            </div>
            <div class="page-changer">
                <a class="vertical-right" href="#">&#60;&#60;Previous</a>&nbsp;Page: 1 of 2&nbsp;<a
                    class="vertical-left" href="#">Next&#62;&#62;</a>
            </div>
        </div>
        <div class="book-shelf">
            <div class="book-card" v-for="book in books" v-bind:key="book.id">
                
                <img class="book-img" :src="book.get_image">
                <div class="book-card-header">
                    <h5 class="book-title">{{ book.title }}</h5>
                    <h6 class="book-autor">by {{ book.author }}</h6>
                    <p class="book-des"> {{ book.des }}</p>
                    <a class="book-des" href="#">more details</a>
                    
                </div>
                <div class="book-card-footer">
                    <h5 class="book-price"><strong>${{ book.unit_price }}</strong></h5>
                    <div class="btn">
                        <h5 style="padding-top: 5px;">Add</h5>
                        <img src="../assets/img/icon/basket.png">
                    </div>
                </div>
                
            </div>
        </div>

        <div class="shelf-footer">

            <div class="page-changer">
                <a class="vertical-right" href="#">&#60;&#60;Previous</a>&nbsp;Page: 1 of 2&nbsp;<a
                    class="vertical-left" href="#">Next&#62;&#62;</a>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

import axios from 'axios'
import { useRoute } from 'vue-router'

export default {
    name: 'HomeView',
    data() {
        return {

            books: [],
            current_number_of_books: 5,

            categories: [],
            category_slug: '',
            current_category: {},

            category_dropdown_menu_show: false,
            
        }
    },

    components: {

    },
    mounted() {
        var route = useRoute()
        this.category_slug = route.params.category_slug
        this.get_books_as_category()
        this.get_current_category()
        this.get_categories()
        console.log(this.current_number_of_books)
    },
    methods: {

        book_at_first_on_row(number_book_per_row){
            if(this.current_number_of_books%number_book_per_row==1){
                return true
            }
            else{
                return false
            }
        },

        get_books_as_category() {
            axios
                .get(`/api/view_book_as_category/${this.category_slug}`)
                .then(response => {
                    this.books = response.data
                })
                .catch(error => {
                    console.log(error)
                })

        },
        get_current_category() {
            axios
                .get(`/api/view_category/${this.category_slug}`)
                .then(response => {
                    this.current_category = response.data[0]
                })
                .catch(error => {
                    console.log(error)
                })
        },
        get_categories(){
            axios 
                .get('/api/view_categories')
                .then(response=>{
                    this.categories = response.data
                
                })
                .catch(error=>{
                    console.log(error)
                })
        },
    },
    
    
}
</script>
