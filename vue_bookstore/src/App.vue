<template>
  <header>
    <div class="header-1">
      <div class="label">
          <a href="/">
              <h1><strong>bookstore<span>.com</span></strong></h1>
          </a>
      </div>

      <div class="option">
          <button data-bs-toggle="dropdown">
              login
              <img src="./assets/img/icon/black-dropdown.png">
          </button>
          <div class="dropdown-menu">
              <form class="upper-form">
                  <input id="login-email" type="email" placeholder="Email">
                  <div class="py-2"><input id="login-password" type="password" placeholder="Password"></div>
                  
                  <div class="navigation">
                      <a href="#">Forgot Password</a>
                      <div class="btn">Send</div>
                  </div>
                  <hr>
                  <a class="login-via-fb-icon" href="#"><img src="./assets/img/icon/login-via-fb.png"></a>
              </form>
              <div class="lower-form">
                  <p><span>Are you not registered yet?</span><br>
                  In just few steps you can have easy
                  access of unlimited selecction of books</p>
                  <hr>
                  <div class="register-link"><a href="#">Register</a><img src="./assets/img/icon/yellow-dropdown.png"></div>
              </div>
          </div>
          <a class="px-3 text-decoration-none" style="color: black;" href="#">register</a>
      </div>
    </div>
</header>

  <router-view/>

    
  <footer>
      <div class="footer-1">
          <div>
              <div><h4><strong>Do you want to sell your books?</strong></h4></div>
              <div style="padding-top: 15px;"><p>join BookStore.com today!</p></div>
          </div>
          <div>
              <h4><strong>Follow&nbsp;us</strong></h4>
              <div class="footer-social-icon">
              <a href="https://www.facebook.com" target="_blank"><i class="fa-brands fa-square-facebook"></i></a>
              <a class="px-2" href="https://www.twitter.com" target="_blank"><i class="fa-brands fa-square-twitter"></i></a>
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

export default {
  name: 'App',
  data(){
      return {

      }
  },

  components: {

  },
  mounted() {
    
  },
    methods: {
        
    }
}
</script>
