<template>
    <Header2 :_current_category="'Category'" :_categories="categories" />

    <div v-if="!user" class="forgot-form-container">
        <div class="forgot-form-header">
            <h4 class="title"><strong>Change Password</strong></h4>
            <p class="des">Please change your password.</p>
        </div>
        <form @submit.prevent="change_password_submit">
            <div class="forgot-form-body">
                <div class="column-1">
                    <label class="row" for="password">Password</label>
                    <label class="row" for="cfpassword">Confirm password</label>
                </div>
                <div class="column-2">
                    <input class="row" id="password" type="password"
                        placeholder="password must has minimum at least 8 characters and 1 number" v-model="password">
                    <input class="row" id="cfpassword" type="password" placeholder="retype your password"
                        v-model="cfpassword">
                </div>
            </div>
            <div class="alert alert-danger" v-if="errors.length" v-for="error in errors" :key="error">
                <strong>Fail!</strong> {{ error }}
            </div>
            <div class="forgot-form-footer">
                <a href="/">Cancel</a>

                <button class="btn">
                    <h6><strong>Send</strong></h6>
                </button>
            </div>
        </form>

    </div>
    <div v-if="user" class="forgot-form-container" style="margin-bottom: 500px;">
        <div class="forgot-form-header">
            <h4 class="title"><strong>You have Logged</strong></h4>
            <p class="des">Now, you can change password in your profile.</p>
        </div>
    </div>
</template>


<script>
import Header2 from '@/components/Header-2.vue';
import axios from 'axios';
import { toast } from 'bulma-toast'
import { mapGetters } from 'vuex'
export default {

    name: 'ChangePassView',
    data() {
        return {
            categories: [],
            password: '',
            cfpassword: '',
            errors: [],
            token: '',
        }
    },
    components: {
        Header2,
    },
    computed: {
        ...mapGetters(['user'])
    },
    mounted() {
        this.get_categories()
        this.token = this.$route.params.token

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
        passwor_check(password) {
            var expression = /^(?=.*[0-9]).{9,}/
            if (this.password.match(expression)) {
                return true
            } else {
                return false
            }
        },
        change_password_submit() {
            this.errors = []


            if (!this.passwor_check()) {
                this.errors.push('Invalid password, password must has minimum 8 characters and 1 number')
            }
            else if (this.password !== this.cfpassword) {
                this.errors.push('Password repeat does match')
            }


            if (!this.errors.length) {
                const formData = {
                    token: this.token,
                    password: this.password,
                }

                axios
                    .post('/api/change_password', formData)
                    .then(response => {
                        console.log(response.data)
                        toast({
                            message: response.data.message,
                            type: 'is-success',
                            duration: 3000,
                            dismissible: true,
                            pauseOnHover: true,
                        })
                        this.$router.push({ path: '/' })
                    })
                    .catch(error => {
                        this.errors.push(error.response.data.message)
                    })
            }
        },
    }
}
</script>