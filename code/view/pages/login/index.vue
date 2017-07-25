<template>
  <v-container fluid class="color">
    <v-card>
      <v-card-title primary>
        HOLA
      </v-card-title>
    </v-card>
  </v-container>
</template>

<script>
  export default {

    head () {
      return {
        title: this.$t('login.title'),
        meta: [
          {hid: 'djuxt', name: 'djuxt', content: 'djuxt - Login'}
        ]
      }
    }

  }
</script>

<style>

</style>
