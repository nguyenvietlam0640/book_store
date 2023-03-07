<template>
    <Header2 :_current_category="'Category'" :_categories="categories" />

    <div class="forgot-form-container">
        <div class="forgot-form-header">
            <h4 class="title"><strong>Forgot Password</strong></h4>
            <p class="des">Please, introduce the email that you used to create your account and we will send you a link to
                recover your password.</p>
        </div>
        <form @submit.prevent="forgot_password_submit">
            <div class="forgot-form-body">
                <div class="column-1">
                    <label class="row" for="Email">Email</label>
                </div>
                <div class="column-2">
                    <input class="row" id="Email" type="email" placeholder="@" v-model="email">
                </div>
            </div>
            <div class="alert alert-danger" v-if="errors.length" v-for="error in errors" :key="error">
                <strong>Email!</strong> {{ error }}
            </div>
            <div class="forgot-form-footer">
                <a href="/">Cancel</a>

                <button class="btn">
                    <h6><strong>Send</strong></h6>
                </button>
            </div>
        </form>

    </div>
</template>


<script>
import Header2 from '@/components/Header-2.vue';
import axios from 'axios';
import { toast } from 'bulma-toast'
export default {

    name: 'ForgotPassView',
    data() {
        return {
            categories: [],
            email: '',
            errors: []
        }
    },
    components: {
        Header2,
    },
    mounted() {
        this.get_categories()
    },
    methods: {
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
        forgot_password_submit() {
            this.errors = []
            axios
                .post('/api/reset_password', { email: this.email })
                .then(response => {
                    console.log(response.data)
                    toast({
                        message: response.data.message,
                        type: 'is-success',
                        duration: 3000,
                        dismissible: true,
                        pauseOnHover: true,
                    })
                })
                .catch(error => {
                    this.errors.push(error.response.data.message)
                })
        }
    },
}
</script>