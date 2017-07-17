<template>

  <v-app standalone>

    <cgv-main-nav :is-open="drawer"/>

    <v-toolbar>
      <v-toolbar-title>
        <v-toolbar-side-icon @click.native.stop="drawer = !drawer"></v-toolbar-side-icon>
        <v-icon fa fa-fw class="ml-3">youtube</v-icon>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- <v-text-field
        label="Search..."
        single-line
        append-icon="search"
        dark
        hide-details
      ></v-text-field> -->
    </v-toolbar>

    <main>
      <v-container>

         <nuxt/>

      </v-container>
    </main>



  </v-app>

</template>

<script>
import cgvMainNav from '~components/common/cgv-main-nav.vue'

export default {
  components: {
    cgvMainNav
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
    drawer: false
  })
}

</script>
