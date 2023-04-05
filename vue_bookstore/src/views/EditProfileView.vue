<template>
    <Header2 :_current_category="'Category'" :_categories="categories" />
    <div class="comming-soon">
       Comming soon
    </div>
    <div v-if="user" class="register-form-container">

        <div class="form-header">
            <h4 class="title" style="padding-bottom: 20px;"><strong>Edit profile</strong></h4>
        </div>
        <form @submit.prevent="edit_submit">
            <div class="form-body">
                <div class="column-1">
                    <label class="row" for="fullname">Full Name</label>
                    <label class="row" for="email">Email</label>
                    <label class="row" for="password">New password</label>
                    <label class="row" for="cfpassword">Confirm Password</label>
                    <label class="row" for="birthday">Birthday</label>
                </div>
                <div class="column-2">
                    <input class="row" id="fullname" type="text" v-bind:placeholder="user.full_name" v-model="full_name">
                    <input class="row" id="email" type="email" v-bind:placeholder="user.email" v-model="email">
                    <input class="row" id="password" type="password" placeholder="minimum 8 characters and 1 number"
                        v-model="password">
                    <input class="row" id="cfpassword" type="password" placeholder="Retype the password"
                        v-model="cfpassword">
                    <input class="row" id="birthday" type="date" v-model="user.birthday">

                </div>

            </div>




            <div class="alert alert-danger" v-if="errors.length" v-for="error in errors" :key="error">
                <strong>Fail!</strong> {{ error }}
            </div>
            <div class="form-footer">
                <a href="/">Cancel</a>

                <button class="btn">
                    <h6><strong>Save</strong></h6>
                </button>
            </div>
        </form>
    </div>
    <div v-if="!user" class="register-form-container" style="padding-bottom: 500px;">
        <div class="form-header">
            <h4 class="title" style="padding-bottom: 20px;"><strong>Please login to edit your profile</strong></h4>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import Header2 from '../components/Header-2.vue'
import { toast } from 'bulma-toast'
import { mapGetters } from 'vuex'

export default {
    name: 'EditProfileView',
    data() {
        return {
            categories: [],


            full_name: '',
            email: '',
            password: '',
            cfpassword: '',
            birthday: '',

            errors: [],
        }
    },
    components: {
        Header2,
    },
    computed: {
        ...mapGetters(['user']),

    },
    mounted() {
        document.title = 'Edit profile'
        this.get_categories()

    },


    methods: {




        passwor_check(password) {
            var expression = /^(?=.*[0-9]).{9,}/
            if (this.password.match(expression)) {
                return true
            } else {
                return false
            }
        },



        edit_submit() {
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

            if (!this.errors.length) {
                const formData = {
                    full_name: this.full_name,
                    email: this.email,
                    password: this.password,
                    birthday: this.birthday,
                }

                axios
                    .post('api/register', formData)
                    .then(response => {

                        toast({
                            message: response.data['message'],
                            type: 'is-success',
                            duration: 3000,
                            dismissible: true,
                            pauseOnHover: true,
                        })


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