<template>
  <h1 class="red">Hello {{ name }}!</h1>
</template>

<script>
export default {
  components: {

  },
  asyncData (context) {
    // called every time before loading the component
    console.info(context)
    return { name: 'World', title: 'T' }
  },
  fetch () {
    // The fetch method is used to fill the store before rendering the page
  },
  head () {
    return {
      title: 'Users'
    }
    // Set Meta Tags for this Page
  }
  // and more functionality to discover
}
</script>

<style>
.red {
  color: red;
}
</style>
