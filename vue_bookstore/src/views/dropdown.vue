<template>
    <span class="dropdown" :class="{shown: state}">
      <a href="#" @click.prevent="toggleDropdown" class="dropdown-toggle">toggle menu</a>
            <div class="dropdown-menu" v-show="state">
                <ul class="list-unstyled">
                    <slot></slot>
                </ul>
            </div>
        <transition/>
    </span>
</template>

<script>
export default {
  name: 'dropdown',
  data () {
    return {
      state: false
    }
  },
  methods: {
    toggleDropdown (e) {
      this.state = !this.state
    },
    close (e) {
      if (!this.$el.contains(e.target)) {
        this.state = false
      }
    }
  },
  mounted () {
    document.addEventListener('click', this.close)
  },
  beforeDestroy () {
    document.removeEventListener('click',this.close)
  }
}
</script>
<style scoped>
span{
  margin-top: 200px;
}
</style>