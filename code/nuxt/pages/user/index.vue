<template>
  <pre> {{ data }} </pre>
</template>

<script>
import axios from 'axios'
export default {
  layout: 'red-black',
  components: {

  },
  async asyncData (context) {
    // called every time before loading the component
    if (context.isServer) {
      // let { data } = await axios.get('http://django-wp/api/')
      return { data: 'SERVER' }
    } else {
      let { data } = await axios.get('http://localhost/api/')
      return { data: data }
    }
  },
  fetch () {
    // The fetch method is used to fill the store before rendering the page
  },
  head () {
    return {
      title: 'Users'
    }
    // Set Meta Tags for this Page
  },
  data () {
  }
  // and more functionality to discover
}
</script>

<style>
.red {
  color: red;
}
</style>
