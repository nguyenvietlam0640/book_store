<template>
  <Header2 :_current_category="'Category'" :_categories="categories" />
  <BookShelf :_current_category="`we found ${book_total} results sorted in most relavant order`" :_books="books"
    :_page_total="page_total" />
  />
</template>



<script>
// @ is an alias to /src

import axios from 'axios'
import Header2 from '../components/Header-2.vue'
import BookShelf from '../components/BookShelf.vue'
import { useRoute } from 'vue-router'
export default {
  name: 'SearchView',
  data() {
    return {

      books: [],
      book_total: 0,
      categories: [],

      page_total: 0,
      books_per_page: 0,
      current_page: 1

    }
  },

  components: {
    Header2,
    BookShelf,
  },
  mounted() {
    var route = useRoute()
    this.books_per_page = route.params.books_per_page
    this.current_page = route.params.page
    this.get_categories()
    this.get_search_result(this.$route.query.id, this.$route.query.input)


  },
  methods: {
    get_page_total(number_of_books, books_per_page) {
      if (number_of_books % books_per_page == 0) {
        this.page_total = parseInt(number_of_books / books_per_page)
      }
      else {
        this.page_total = parseInt(number_of_books / books_per_page) + 1
      }
    },

    get_categories() {
      axios
        .get('/api/view_categories')
        .then(response => {
          this.categories = response.data

        })
        .catch(error => {
          console.log(error)
        })
    },
    get_search_result(id, input) {
      axios
        .get(`/api/search_results/${this.books_per_page}/${this.current_page}?id=${id}&input=${input}`)
        .then(response => {
          this.book_total = response.data[0]
          this.books = response.data[1]
          
          this.get_page_total(this.book_total, this.books_per_page)
        })
        .catch(error => {
          console.log(error)
        })
    },

  },

}
</script>