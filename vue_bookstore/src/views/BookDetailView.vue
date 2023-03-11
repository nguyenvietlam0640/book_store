<template>
    <Header2 :_current_category="'Category'" :_categories="categories" />

    <div class="book-detail-container">
        <img class="book-photo" v-bind:src="book.get_image">
        <div class="info-container">
            <h2 class="title">{{ book.title }}</h2>
            <div class="author">{{ book.author }}</div>
            <div class="Evaluate">
                <img class="rating-star" src="../assets/img/icon/high-star.png">
                <img class="rating-star" src="../assets/img/icon/high-star.png">
                <img class="rating-star" src="../assets/img/icon/low-star.png">
                <img class="rating-star" src="../assets/img/icon/low-star.png">
                <img class="rating-star" src="../assets/img/icon/low-star.png">
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
                <h1 class="current-price">${{ book.unit_price }}</h1>
                <h3 class="discount">Save: 20%</h3>
                <h3 class="original-price"> before $orprice</h3>
            </div>
            <button class="btn">Add
                <img class="basket-img" src="../assets/img/icon/basket.png">
            </button>
        </div>




    </div>

    <div class="add-comment-container">
        <div class="header">
            <h4 class="title"> Add your comment:</h4>
            <img src="../assets/img/icon/yellow-dropdown.png">
        </div>
        <div class="rating">
            <div>
                <img class="rating-star" src="../assets/img/icon/low-star.png">
                <img class="rating-star" src="../assets/img/icon/low-star.png">
                <img class="rating-star" src="../assets/img/icon/low-star.png">
                <img class="rating-star" src="../assets/img/icon/low-star.png">
                <img class="rating-star" src="../assets/img/icon/low-star.png">
            </div>
            <!-- problem in here -->
        </div>
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
</template>


<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
import Header2 from '../components/Header-2.vue'


export default {
    name: 'BookDetailView',
    data() {
        return {
            categories: [],
            book: {},
            comments: [],
            content: '',
            rating: '',
            errors: [],
            able_to_comment: false,
            thanks_for_comment: false,

        }
    },
    components: {
        Header2,
    },

    async mounted() {
        const category_slug = this.$route.params.category_slug
        const book_slug = this.$route.params.book_slug
        await this.get_categories()
        await this.get_book_detail(category_slug, book_slug)

        document.title = `BookStore | ${this.book.title}`
        await this.get_all_comments(book_slug)
        this.check_able_to_comment()

    },

    computed: {
        ...mapGetters(['user'])
    },

    methods: {
        check_able_to_comment() {
            if (this.user) {
                this.able_to_comment = true
            }
            else {
                this.able_to_comment = false
            }

        },
        async post_comment() {

            if (!this.able_to_comment) {
                alert('You must login to comment')
            }
            else if (!this.rating) {
                console.log('rate please')
            }
            else if (this.able_to_comment && this.rating) {
                const data = {
                    rating: this.rating,
                    content: this.content
                }
                await axios
                    .post(`api/post_comment/${this.$route.params.book_slug}/${this.user.id}`, data)
                    .then(response => {
                        console.log(response.data)
                        this.get_all_comments(this.$route.params.book_slug)
                        this.thanks_for_comment = true
                    })
                    .catch(error => {
                        console.log(error.response.data)
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
                    console.log(this.book)
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