<template>
    <Header2 :_current_category="'Category'" :_categories="categories" />

    <div v-if="!user" class="forgot-form-container" style="margin-bottom: 500px;">
        <div class="forgot-form-header">
            <h4 class="title"><strong>{{ message }}</strong></h4>
        </div>
    </div>
    <div v-if="user" class="forgot-form-container" style="margin-bottom: 500px;">
        <div class="forgot-form-header">
            <h4 class="title"><strong>You had activated your account</strong></h4>
        </div>
    </div>
</template>


<script>
import Header2 from '@/components/Header-2.vue';
import axios from 'axios';
import { toast } from 'bulma-toast'
import { mapGetters } from 'vuex'
export default {

    name: 'ActivateView',
    data() {
        return {
            categories: [],
            
            errors: [],
            token: '',
            message: '',
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
        this.activate(this.token)
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
        activate(token) {
            this.errors = []
            axios
                .post('/api/activate', {token: token})
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
                    
                    this.message = (error.response.data.message)
                })
        }
    },
}

</script>