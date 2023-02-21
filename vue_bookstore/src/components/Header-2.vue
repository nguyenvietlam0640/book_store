<template>
    <div class="header-2">
        <div class="search-group">
            <div class="search-bar-container">
                <div class="search-bar">
                    <input id="search-input" type="search" placeholder="autor, title">
                    <div class="btn" v-on:click.prevent="all_categories_dropdown_show">
                        <div>all&nbsp;categories</div><img src="../assets/img/icon/black-dropdown.png">
                    </div>
                    <ul class="all-categories-dropdown-menu" v-on:click="all_categories_dropdown_show" :class="{ shown: all_categories_dropdown_menu }"
                        v-show="all_categories_dropdown_menu">
                        <li class="menu-list" v-for="category in _categories" v-bind:key="category.id">
                            <a v-on:click="_pass_category(category.name, category.id)">{{ category.name }}</a>
                        </li>
                    </ul>
                </div>
                <a v-on:click="_search(_id_to_search)"><img src="../assets/img/icon/search.png"></a>
            </div>

            <div class="category-dropdown">
                <button class="btn" v-on:click.prevent="category_dropdown_show">
                    <!---->
                    <div class="category-title">{{ _current_category }}</div>
                    <img src="../assets/img/icon/white-dropdown.png">
                </button>
                <ul class="category-dropdown-menu" :class="{ shown: category_dropdown_menu }" v-show="category_dropdown_menu">
                    <li class="menu-list" v-for="category in _categories" v-bind:key="category.id">

                        <a v-bind:href="category.get_absolute_url+`/${books_per_page}/1`">{{ category.name }}<span>({{
                            category.get_books_total
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
</template>





<script>
import { useRoute } from 'vue-router'
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
            category_dropdown_menu: false,
            all_categories_dropdown_menu: false
        }
    },
    mounted() {
        var route = useRoute()
        this.books_per_page = route.params.books_per_page
        document.addEventListener('click', this.close)

    },
    beforeDestroy() {
        document.removeEventListener('click', this.close)
    },
    methods: {
        all_categories_dropdown_show(e) {
            this.all_categories_dropdown_menu = !this.all_categories_dropdown_menu

        },
        category_dropdown_show(e) {
            this.category_dropdown_menu = !this.category_dropdown_menu
        },
        close(e) {
            if (!this.$el.contains(e.target)) {
                this.all_categories_dropdown_menu = false
                this.category_dropdown_menu = false
            }
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