<template>
    <header>
        <div class="header-1">
            <div class="label">
                <a href="/">
                    <h1><strong>bookstore<span>.com</span></strong></h1>
                </a>
            </div>
            <div v-if="user" class="logined-option">
                <button class="btn" data-bs-toggle="dropdown">
                    {{ user.full_name }}
                    <img src="./assets/img/icon/black-dropdown.png">
                </button>
                <ul class="dropdown-menu">
                    <li><a v-bind:href="`/${user.get_absolute_url}`">edit profile</a></li>
                    <!-- <hr> -->
                    <li><a v-on:click="logout()">log out</a></li>
                </ul>
                <div class="icon">
                    <i class="fa-sharp fa-solid fa-comment"></i>
                </div>

            </div>
            <div v-if="!user" class="option">
                <button data-bs-toggle="dropdown" data-bs-auto-close="outside">
                    login
                    <img src="./assets/img/icon/black-dropdown.png">
                </button>
                <div class="dropdown-menu">
                    <form @submit.prevent="login_submit" class="upper-form">
                        <input v-model="email" id="login-email" type="email" placeholder="Email">
                        <div class="py-2"><input v-model="password" id="login-password" type="password"
                                placeholder="Password"></div>
                        <div class="alert alert-danger" v-if="errors.length" v-for="error in errors" :key="error">
                            <strong>Login fail!</strong> {{ error }}<a v-if="send_email_link" v-on:click="send_activate_email()">active now</a>
                        </div>
                        <div class="navigation">
                            <a href="/forgot_password">Forgot Password</a>
                            <button class="btn">Send</button>
                        </div>
                        <hr>
                        <div class="login-via-fb-icon"><a href="https://www.facebook.com"><img
                                    src="./assets/img/icon/login-via-fb.png"></a>
                        </div>
                    </form>
                    <div class="lower-form">
                        <p><span>Are you not registered yet?</span><br>
                            In just few steps you can have easy
                            access of unlimited selecction of books</p>
                        <hr>
                        <div class="register-link"><router-link to="/register">Register</router-link><img
                                src="./assets/img/icon/yellow-dropdown.png"></div>
                    </div>
                </div>
                <router-link to="/register" class="px-3 text-decoration-none" style="color: black;">register</router-link>
            </div>
        </div>
    </header>

    <router-view />


    <footer>
        <div class="footer-1">
            <div>
                <div>
                    <h4><strong>Do you want to sell your books?</strong></h4>
                </div>
                <div style="padding-top: 15px;">
                    <p>join BookStore.com today!</p>
                </div>
            </div>
            <div>
                <h4><strong>Follow&nbsp;us</strong></h4>
                <div class="footer-social-icon">
                    <a href="https://www.facebook.com" target="_blank"><i class="fa-brands fa-square-facebook"></i></a>
                    <a class="px-2" href="https://www.twitter.com" target="_blank"><i
                            class="fa-brands fa-square-twitter"></i></a>
                    <a href="https://www.googleplus.com" target="_blank"><i class="fa-brands fa-square-google-plus"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-2">
            <p>Copyright @2013 BookStore is a registered trademark of BookStore Pte Ltd</p>
        </div>
    </footer>
</template>



<script>
// @ is an alias to /src
import axios from 'axios'
import { mapGetters } from 'vuex'
import { toast } from 'bulma-toast'

export default {
    name: 'App',
    data() {
        return {
            email: '',
            password: '',
            errors: [],
            send_email_link: false,
        }
    },
    computed: {
        ...mapGetters(['user'])
    },

    async created() {
        const response = await axios
            .get('api/user')
            .then(response => {
                this.$store.dispatch('user', response.data)
            })
            .catch(error => {
                console.log()
            })

    },

    methods: {

        login_submit() {
            this.errors = []
            axios
                .post('api/login', {
                    email: this.email,
                    password: this.password
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
                    if (error.response.data['message'] == 'Your account was not activated, please check your email for confirming') {
                        this.send_email_link = true
                    }
                })
        },
        send_activate_email() {
            axios
                .post('api/send_activate_email', { email: this.email })
                .then(response => {
                    toast({
                        message: 'Email Sent successfully',
                        type: 'is-success',
                        duration: 3000,
                        dismissible: true,
                        pauseOnHover: true,

                    })
                    this.send_email_link = false

                })
                .catch(error => {
                    this.errors.push(error.response.data['message'])
                })
        },
        logout() {
            localStorage.removeItem('jwt')
            window.location.href = '/'
        },

    }
}
</script>
