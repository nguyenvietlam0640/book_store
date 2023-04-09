<template >
    <Header2 :_current_category="'Category'" :_categories="categories" />
    <div v-if="!is_loading">
        <div class="book-detail-container">
            <img class="book-photo" v-bind:src="book.get_image">
            <div class="info-container">
                <h2 class="title">{{ book.title }}</h2>
                <div class="author">{{ book.author }}</div>
                <div class="Evaluate">

                    <img v-for="i in book.get_total_rating_value" :key="i" class="rated-star"
                        src="../assets/img/icon/high-star.png">

                    <img v-for="i in rating_star_left" :key="i" class="rated-star" src="../assets/img/icon/low-star.png">
                    <h6 class="count-rate">({{ book.get_total_rating_count }})</h6>
                </div>
                <div class="des">
                    {{ book.des }}
                </div>
                <div class="publisher">
                    Publisher: {{ book.publisher }}
                </div>
                <div class="published-date">
                    Published date: {{ book.published_date }}
                </div>


            </div>
            <div class="add-item-container">
                <div class="price-container">
                    <h1 class="current-price">${{ book.unit_price.toFixed(2) }}</h1>
                    <h3 class="discount">Save: {{ book.discount }}%</h3>
                    <h3 class="original-price"> before ${{ book.price }}</h3>
                </div>
                <div v-on:click="add_to_cart(book)" class="btn">Add
                    <img class="basket-img" src="../assets/img/icon/basket.png">
                </div>
            </div>




        </div>
        <div v-if="thanks_for_comment" class="add-comment-container">
            <div class="header">
                <h4 class="title"> You have rated on this book.</h4>
                <img src="../assets/img/icon/yellow-dropdown.png">

            </div>
            <h5>--- Thanks for your rating ---</h5>
        </div>

        <div v-if="!thanks_for_comment" class="add-comment-container">
            <div class="header">
                <h4 class="title"> Add your comment:</h4>
                <img src="../assets/img/icon/yellow-dropdown.png">
            </div>

            <div class="rating">

                <img v-for="i in 5" :key="i" v-on:click="rate(i)" :class="`rating-star${i}`"
                    src="../assets/img/icon/low-star.png">
                <div class="alertt" v-if="errors.length" v-for="error in errors" :key="error">
                    *{{ error }}.
                </div>
            </div>

            <!-- problem in here -->

            <textarea v-model="content" id="comment"></textarea>
            <div class="footer">
                <a href="#">cancel</a>
                <button class="btn" v-on:click="post_comment">Send</button>
            </div>


        </div>
        <div class="comments-container">
            <h4 class="title">Comments: ({{ book.get_total_rating_count }})</h4>
            <h5 class="no-comment-title" v-if="comments.length == 0">No comment yet
                <hr>
            </h5>
            <div class="comment-card" v-for="comment in comments">

                <h5 class="user-name">{{ comment.created_by }}</h5>
                <div class="rating">{{ comment.rating }}/5 <img src="../assets/img/icon/high-star.png" alt="a rating star">
                </div>
                <p class="comment">{{ comment.content }} </p>
                <div class="day-post">{{ comment.created_at }}</div>
                <hr>
            </div>


        </div>
    </div>
</template>


<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
import Header2 from '../components/Header-2.vue'
import { toast } from 'bulma-toast'

export default {
    name: 'BookDetailView',
    data() {
        return {
            categories: [],
            book: {},

            comments: [],

            content: '',
            rating: '',

            rating_star_left: 0,

            errors: [],

            able_to_comment: false,
            thanks_for_comment: false,

        }
    },
    components: {
        Header2,
    },

    async mounted() {
        this.$store.dispatch('set_loading', true)
        const category_slug = this.$route.params.category_slug
        const book_slug = this.$route.params.book_slug
        await this.get_categories()
        await this.get_book_detail(category_slug, book_slug)

        document.title = `BookStore | ${this.book.title}`
        await this.get_all_comments(book_slug)
        this.check_able_to_comment()
        this.$store.dispatch('set_loading', false)

    },

    computed: {
        ...mapGetters(['user']),
        ...mapGetters(['is_loading'])
    },

    methods: {
        add_to_cart(book) {
            const item = {
                book: book,
                quantity: 1
            }
            this.$store.dispatch('add_to_cart', item)
            toast({
                message: 'book added to cart',
                type: 'is-success',
                duration: 3000,
                dismissible: true,
                pauseOnHover: true,
            })

        },
        reset_rating_star() {
            for (let i = 1; i <= 5; i++) {
                document.querySelector(`.rating .rating-star${i}`).src = require("../assets/img/icon/low-star.png")
            }
        },
        rate(high_star_index) {
            this.reset_rating_star()
            if (high_star_index == this.rating) {
                this.rating = ''
                return
            }

            for (let i = 1; i <= high_star_index; i++) {
                document.querySelector(`.rating .rating-star${i}`).src = require("../assets/img/icon/high-star.png")
            }
            this.rating = high_star_index

        },
        check_able_to_comment() {
            if (this.user) {
                this.able_to_comment = true
                this.check_unique_comment()
            }
            else {
                this.able_to_comment = false
            }

        },

        async check_unique_comment() {
            await axios
                .get(`api/post_comment/${this.$route.params.book_slug}/${this.user.id}`)
                .then(response => {
                    this.thanks_for_comment = !response.data.message
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async post_comment() {
            this.errors = []
            if (!this.able_to_comment) {
                alert('You must login to comment')
            }
            else if (!this.rating) {
                this.errors.push('You must rate before posting comment')
            }
            else if (this.able_to_comment && this.rating) {
                const data = {
                    rating: this.rating,
                    content: this.content
                }
                await axios
                    .post(`api/post_comment/${this.$route.params.book_slug}/${this.user.id}`, data)
                    .then(response => {
                        this.get_all_comments(this.$route.params.book_slug)
                        this.get_book_detail(this.$route.params.category_slug, this.$route.params.book_slug)

                        this.thanks_for_comment = true
                    })
                    .catch(error => {
                        if (error.response.data.non_field_errors) {
                            alert('You had comment in this book')
                        }
                        if (error.response.data.message) {
                            this.errors.push(error.response.data.message)
                        }
                    })
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
        async get_book_detail(category_slug, book_slug) {
            await axios
                .get(`api/category/${category_slug}/${book_slug}`)
                .then(response => {

                    this.book = response.data
                    this.rating_star_left = 5 - this.book.get_total_rating_value
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async get_all_comments(book_slug) {
            await axios
                .get(`api/view_all_comments/${book_slug}`)
                .then(response => {
                    this.comments = response.data
                    console.log(this.comments)
                })
                .catch(error => {
                    console.log(error.response.data['message'])
                })
        }
    },

}

</script>