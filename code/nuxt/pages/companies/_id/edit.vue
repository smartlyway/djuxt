<template>
  <v-layout row wrap>
    <v-flex sm12>

      <v-card>
        <v-card-title primary-title class="green white--text">
          <h3 class="headline mb-0 white--text">Editar empresa: {{ company.name }}</h3>
        </v-card-title>

        <div class="pa-5">
          <v-text-field name="name" label="Nombre" v-model="company.name" ></v-text-field>
          <v-text-field name="nif" label="NIF" v-model="company.nif" ></v-text-field>
          <v-text-field name="phone" label="Teléfono" v-model="company.phone" ></v-text-field>
          <v-text-field name="activity" label="Actividad" v-model="company.activity" ></v-text-field>
        </div>


        <v-card-actions>
          <v-btn flat class="green--text" @click.native="updateCompany">Guardar cambios</v-btn>
          <v-btn flat class="red--text" nuxt :to="'/companies'">Cancelar</v-btn>
        </v-card-actions>

      </v-card>
    </v-flex>

    <v-snackbar :timeout="snackbar.timeout" v-model="snackbar.active"
      :success="snackbar.context === 'success'"  :info="snackbar.context === 'info'"
      :warning="snackbar.context === 'warning'" :error="snackbar.context === 'error'">
      {{ snackbar.text }}
      <v-btn flat class="white--text" @click.native="snackbar.active = false">Close</v-btn>
    </v-snackbar>

  </v-layout>
</template>

<script>

  import axios from 'axios'
  // import router from 'vue-router'

  export default {
    layout: 'red-black',
    async asyncData (context) {
      var cData = {
        snackbar: {
          active: false,
          timeout: 6000,
          context: 'success',
          text: ''
        },
        params: context.params
      }
      if (context.isServer) {
        let {data} = await axios.get('http://django-wp/api/company/' + context.params.id + '/')
        cData['company'] = data
      } else {
        let {data} = await axios.get('http://localhost/api/company/' + context.params.id + '/')
        cData['company'] = data
      }
      return cData
    },
    methods: {
      updateCompany () {
        axios.put('http://localhost/api/company/' + this.params.id + '/', this.company).then((response) => {
          this.snackbar.text = 'Datos actualizados correctamente'
          this.snackbar.context = 'success'
          this.snackbar.active = true
          this.$router.push('/companies')
        }).catch((err) => {
          if (err) {
            this.snackbar.text = 'Error actualizando datos'
            this.snackbar.context = 'error'
            this.snackbar.active = true
          }
        })
      }

    },
    validate ({params}) {
      // Must be a number
      // return /^\d+$/.test(params.id)
      return true
    }
  }

</script>
