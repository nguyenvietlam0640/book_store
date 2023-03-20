import { createStore } from 'vuex'

export default createStore({
  state: {
    is_loading: true,
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
    },
    is_loading: (state) => {
      return state.is_loading
    }
  },
  mutations: {
    set_loading(state, status) {
      state.is_loading = status
    },
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

    decrease_item(state, id) {
      const exists = state.cart.items.filter(i => i.book.id === id)
      if (exists.length && exists[0].quantity > 0) {
        if (exists[0].quantity == 1) {
          if (confirm(`remove "${exists[0].book.title}" from cart ?`)) {
            state.cart.items = state.cart.items.filter(item => item !== exists[0])
          }
          else {
            return
          }
        }
        else {
          exists[0].quantity = parseInt(exists[0].quantity) - 1
        }
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },

    increase_item(state, id) {
      const exists = state.cart.items.filter(i => i.book.id === id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + 1
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

    },
    empty_cart(state) {
      const cart = {
        items: []
      }
      state.cart = cart
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    delete_item(state, id) {
      const exists = state.cart.items.filter(i => i.book.id === id)
      if (exists.length) {
        if (confirm(`remove "${exists[0].book.title}" from cart ?`)) {
          state.cart.items = state.cart.items.filter(item => item !== exists[0])
          localStorage.setItem('cart', JSON.stringify(state.cart))
        }

      }

    },
  },
  actions: {
    set_loading(context, status) {
      context.commit('set_loading', status)
    },
    user(context, user) {
      context.commit('user', user)
    },
    initalize_cart(context) {
      context.commit('initalize_cart')
    },
    add_to_cart(context, item) {
      context.commit('add_to_cart', item)
    },
    empty_cart(context) {
      context.commit('empty_cart')
    },
    decrease_item(context, id) {
      context.commit('decrease_item', id)
    },
    increase_item(context, id) {
      context.commit('increase_item', id)
    },
    delete_item(context, id) {
      context.commit('delete_item', id)
    }


  },
  modules: {
  }
})
