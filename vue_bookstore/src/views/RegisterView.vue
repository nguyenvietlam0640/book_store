<template>
    <Header2 :_current_category="'Category'" :_categories="categories" />
    <div class="register-form-container">
        <div class="form-header">
            <h4 class="title"><strong>Register</strong></h4>
            <p class="des">Fill the register and be part of our comunity.</p>
        </div>
        <form @submit.prevent="register_submit">
            <div class="form-body">
                <div class="column-1">
                    <label class="row" for="fullname">Full Name</label>
                    <label class="row" for="email">Email</label>
                    <label class="row" for="password">Password</label>
                    <label class="row" for="cfpassword">Confirm Password</label>
                    <label class="row" for="birthday">Birthday</label>
                    <label class="row" for="captcha-input">Captcha</label>
                </div>
                <div class="column-2">
                    <input class="row" id="fullname" type="text" placeholder="Full name" v-model="full_name">
                    <input class="row" id="email" type="email" placeholder="@" v-model="email">
                    <input class="row" id="password" type="password" placeholder="minimum 8 characters and 1 number"
                        v-model="password">
                    <input class="row" id="cfpassword" type="password" placeholder="Retype the password"
                        v-model="cfpassword">
                    <input class="row" id="birthday" type="date" v-model="birthday">
                    <div class="row">
                        <div class="captcha">
                            <div class="preview"></div>
                            <input class="captcha-input" id="captcha-input" type="text" v-model="captcha">
                        </div>
                    </div>
                </div>
            </div>



            <div class="alert alert-danger" v-if="errors.length" v-for="error in errors" :key="error">
                <strong>Register Fail!</strong> {{ error }}
            </div>
            <div class="form-footer">
                <a href="/">Cancel</a>

                <button class="btn">
                    <h6><strong>Send</strong></h6>
                </button>
            </div>
        </form>
    </div>
</template>


<script>
import axios from 'axios'
import Header2 from '../components/Header-2.vue'
import { toast } from 'bulma-toast'

export default {
    name: 'RegisterView',
    data() {
        return {
            categories: [],
            font_captcha: ['cursive', 'sans-serif', 'serif', 'monospace'],
            captcha_value: '',


            full_name: '',
            email: '',
            password: '',
            cfpassword: '',
            birthday: '',
            captcha: '',

            errors: [],
        }
    },
    components: {
        Header2,
    },
    mounted() {
        document.title = 'Register'
        this.get_categories()
        this.generate_captcha()
        this.set_captcha()
    },

    methods: {
        generate_captcha() {
            let value = btoa(Math.random() * 1000000000)
            value = value.substring(0, 7)
            this.captcha_value = value

        },
        set_captcha() {
            let html = this.captcha_value.split('').map((char) => {
                const rotate = -20 + Math.trunc(Math.random() * 60)
                const font = Math.trunc(Math.random() * this.font_captcha.length)
                return `<span
                style="transform: rotate(${rotate}deg);
                font-family: ${this.font_captcha[font]}"
                >${char}</span>`
            }).join('')
            document.querySelector('.preview').innerHTML = html
        },

        passwor_check(password) {
            var expression = /^(?=.*[0-9]).{9,}/
            if (this.password.match(expression)) {
                return true
            } else {
                return false
            }
        },



        register_submit() {
            this.errors = []
            if (this.full_name === '') {
                this.errors.push('Full name is empty')
            }
            else if (this.email === '') {
                this.errors.push('Email is required')
            }
            else if (!this.passwor_check()) {
                this.errors.push('Invalid password, password must has minimum 8 characters and 1 number')
            }
            else if (this.password !== this.cfpassword) {
                this.errors.push('Password repeat does match')
            }
            else if (this.captcha !== this.captcha_value) {
                this.errors.push('Invalid captcha')
            }

            if (!this.errors.length) {
                const data = {
                    full_name: this.full_name,
                    email: this.email,
                    password: this.password,
                    birthday: this.birthday,
                }

                axios
                    .post('api/register', data)
                    .then(response => {

                        toast({
                            message: response.data['message'],
                            type: 'is-success',
                            duration: 3000,
                            dismissible: true,
                            pauseOnHover: true,
                        })
                        this.$router.push({path : '/'})

                    })
                    .catch(errors => {
                        const errors_message = errors.response.data
                        for (let key in errors_message) {
                            this.errors.push(`${key}: ${errors_message[key]}`)
                        }
                    })
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
    },

}


</script>