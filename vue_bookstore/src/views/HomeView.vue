<template>
    <Header2 :_current_category="current_category.name" :_categories="categories" />

    <BookShelf :_current_category="current_category.name" :_books="books" :_page_total="page_total" />
</template>

<script>
// @ is an alias to /src

import axios from 'axios'
import { useRoute } from 'vue-router'
import Header2 from '../components/Header-2.vue'
import BookShelf from '../components/BookShelf.vue'
export default {
    name: 'HomeView',
    data() {
        return {

            books: [],

            categories: [],
            category_slug: '',
            current_category: {},

            current_page: 0,
            page_total: 0,
            books_per_page: 0
        }
    },

    components: {
        Header2,
        BookShelf,
    },

    async mounted() {
        var route = useRoute()
        this.category_slug = route.params.category_slug
        this.current_page = route.params.page
        this.books_per_page = route.params.books_per_page





        await this.get_books_as_category()
        await this.get_current_category()
        await this.get_categories()
        this.get_page_total(this.current_category.get_books_total, this.books_per_page)


    },

    methods: {
        get_page_total(number_of_books, books_per_page) {
            if (number_of_books % books_per_page == 0) {
                this.page_total = parseInt(number_of_books / books_per_page)
            }
            else {
                this.page_total = parseInt(number_of_books / books_per_page) + 1
            }
            console.log(this.page_total)
        },


        get_books_as_category() {
            return axios
                .get(`/api/view_book_as_category/${this.category_slug}/${this.books_per_page}/${this.current_page}`)
                .then(response => {
                    this.books = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },


        get_current_category() {
            return axios
                .get(`/api/view_category/${this.category_slug}`)
                .then(response => {
                    this.current_category = response.data[0]

                })
                .catch(error => {
                    console.log(error)
                })

        },
        get_categories() {
            return axios
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
