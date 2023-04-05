<template>
    <div class="header-2">
        <div style="width: inherit; height: 75px;"></div>
    </div>
    <div class="login-container">

        <h4 class="title"><strong>Login</strong></h4>
        <div class="form">
            <form @submit.prevent="login_submit_login_page" class="upper-form">
                <input v-model="email_login_page" id="email" type="email" placeholder="Email">
                <div class="py-2"><input v-model="password_login_page" id="password" type="password" placeholder="Password">
                </div>
                <div class="alert alert-danger" v-if="errors.length" v-for="error in errors" :key="error">
                    <strong>Login fail!</strong> {{ error }} <a v-if="send_email_link"
                        v-on:click="send_activate_email()">send
                        now</a>
                </div>
                <div class="navigation">
                    <a href="/forgot_password">Forgot Password</a>
                    <button class="btn">
                        <div v-if="!button_loading">Send</div><i v-if="button_loading"
                            class="fa-solid fa-spinner fa-spin"></i>
                    </button>
                </div>
                <hr>
                <div class="login-via-fb-icon"><a href="https://www.facebook.com"><img
                            src="../assets/img/icon/login-via-fb.png"></a>
                </div>
            </form>
            <div class="lower-form">
                <p><span>Are you not registered yet?</span><br>
                    In just few steps you can have easy
                    access of unlimited selecction of books</p>
                <hr>
                <div class="register-link"><router-link to="/register">Register</router-link><img
                        src="../assets/img/icon/yellow-dropdown.png"></div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name: 'LoginView',
    data() {
        return {
            button_loading: false,
            email_login_page: '',
            password_login_page: '',
            errors: [],
            send_email_link: false,
        }
    },

    methods: {
        async login_submit_login_page() {
            this.button_loading = true
            this.errors = []
            
            await axios
                .post('api/login', {
                    email: this.email_login_page,
                    password: this.password_login_page
                })
                .then(response => {
                    toast({
                        message: 'Login successfully',
                        type: 'is-success',
                        duration: 3000,
                        dismissible: true,
                        pauseOnHover: true,
                    })
                    localStorage.setItem('jwt', response.data.jwt)
                    window.location.href = '/'
                })
                .catch(error => {
                    this.send_email_link = false
                    this.errors.push(error.response.data['message'])
                    if (error.response.data['message'] == 'Your account was not activated, please check your email for confirming. In case there is notthing was sent') {
                        this.send_email_link = true
                    }
                })
            this.button_loading = false
        },
        send_activate_email() {
            this.send_email_link = false
            axios
                .post('api/send_activate_email', { email: this.email_login_page })
                .then(response => {
                    toast({
                        message: 'Email Sent successfully',
                        type: 'is-success',
                        duration: 3000,
                        dismissible: true,
                        pauseOnHover: true,

                    })
                })
                .catch(error => {
                    this.errors.push(error.response.data['message'])
                })
        },
        logout() {
            localStorage.removeItem('jwt')
            window.location.href = this.$route.fullPath
        },

    }
}

</script>