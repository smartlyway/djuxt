<template>
  <v-app standalonec class="grey lighten-3">
    <main>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-flex xs12 sm6 md4 fill-height>
            <v-card>
              <v-card-title class="primary white--text">
                {{ $t('login.card-title') }}
              </v-card-title>

              <v-layout justify-center>

                <v-flex xs10 class="mt-4">
                  <v-text-field :label="$t('login.email')"></v-text-field>
                  <v-text-field :label="$t('login.password')"></v-text-field>
                </v-flex>

              </v-layout>

              <v-layout justify-end>
                <v-btn light class="primary white--text mr-3">
                  {{ $t('login.login') }}
                </v-btn>
              </v-layout>

            </v-card>
          </v-flex>
        </v-layout>
        <!--v-router-->
      </v-container>
    </main>
  </v-app>
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
