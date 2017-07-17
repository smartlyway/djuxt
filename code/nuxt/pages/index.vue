<template>
  <h1> mmmm </h1>
</template>

<script>

export default {
  layout: 'red-black',
  components: {

  },
  asyncData (context) {

  },
  fetch () {

  },
  head () {
    return {
      title: 'Inicio'
    }
  },
  data: () => ({
    drawer: true,
    items: [
        { icon: 'trending_up', text: 'Most Popular' },
        { icon: 'subscriptions', text: 'Subscriptions' },
        { icon: 'history', text: 'History' },
        { icon: 'featured_play_list', text: 'Playlists' },
        { icon: 'watch_later', text: 'Watch Later' }
    ],
    items2: [
        { picture: 28, text: 'Joseph' },
        { picture: 38, text: 'Apple' },
        { picture: 48, text: 'Xbox Ahoy' },
        { picture: 58, text: 'Nokia' },
        { picture: 78, text: 'MKBHD' }
    ]
  })
}

</script>

<style>

</style>
