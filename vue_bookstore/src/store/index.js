import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    cart: {
      items: []
    }
  },
  getters: {
    user: (state) => {
      return state.user
    },
    cart: (state) => {
      return state.cart
    }
  },
  mutations: {
    user(state, user) {
      state.user = user
    },
    initalize_cart(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      }
      else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },
    add_to_cart(state, item) {
      const exists = state.cart.items.filter(i => i.book.id === item.book.id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      }
      else {
        state.cart.items.push(item)
      }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    empty_cart(state){
      const cart = {
        items: []
      }
      state.cart = cart
      localStorage.setItem('cart', JSON.stringify(state.cart))
    }

  },
  actions: {
    user(context, user) {
      context.commit('user', user)
    },
    initalize_cart(context) {
      context.commit('initalize_cart')
    },
    add_to_cart(context, item) {
      context.commit('add_to_cart', item)
    },
    empty_cart(context){
      context.commit('empty_cart')
    }


  },
  modules: {
  }
})
