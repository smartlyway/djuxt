<template>
  <v-layout row wrap>
    <v-flex sm12>
      <v-card class="pa-1 mb-2">
        <v-text-field
        label="Search..."
        single-line
        append-icon="search"
        hide-details
        v-model="search"
      >

        </v-text-field>
      </v-card>
    </v-flex>
    <v-flex sm12 md6 v-for="company in filteredCompanies" :key="company.title">

      <v-card class="mb-2">
        <v-card-title primary-title>
          <div>
            <h3 class="headline mb-0">{{ company.name }}</h3>
            <div> {{ company.nif }}</div>
          </div>
        </v-card-title>

        <v-list two-line>

          <!--  PHONE  -->

          <v-list-tile>

            <v-list-tile-action>
              <v-icon class="orange--text text--darken-2">phone</v-icon>
            </v-list-tile-action>

            <v-list-tile-content>

              <v-list-tile-title> {{ company.phone }} </v-list-tile-title>
              <v-list-tile-sub-title>Phone</v-list-tile-sub-title>

            </v-list-tile-content>

          </v-list-tile>

          <!--  ADDRESS  -->

          <v-list-tile>

            <v-list-tile-action>
              <v-icon class="orange--text text--darken-2">location_on</v-icon>
            </v-list-tile-action>

            <v-list-tile-content>

              <v-list-tile-title>

                {{ formatAddress(company.address) }}

              </v-list-tile-title>

              <v-list-tile-sub-title>Location</v-list-tile-sub-title>
            </v-list-tile-content>

          </v-list-tile>

          <!--  ACTIVITY  -->

          <v-list-tile>

            <v-list-tile-action>
              <v-icon class="orange--text text--darken-2">work</v-icon>
            </v-list-tile-action>

            <v-list-tile-content>

              <v-list-tile-title>

                {{ company.activity }}

              </v-list-tile-title>

              <v-list-tile-sub-title>Activity</v-list-tile-sub-title>
            </v-list-tile-content>

          </v-list-tile>

           <!--  TYPE  -->

          <v-list-tile>

            <v-chip dark v-tooltip:top="{ html: company.type.package[0].name }"
                    class="green white--text">{{ company.type.name }}</v-chip>

             <v-chip v-for="pack in company.type.package" :key="pack.name"
                     label outline class="red red--text"> {{ pack.name }}</v-chip>

          </v-list-tile>

        </v-list>


      </v-card>
    </v-flex>
     <v-btn fixed fab bottom right class="green">
         <v-icon class="white--text">add</v-icon>
       </v-btn>
  </v-layout>

</template>

<script>
  import axios from 'axios'
  export default{
    layout: 'red-black',
    async asyncData (context) {
      // called every time before loading the component
      if (context.isServer) {
        let {data} = await axios.get('http://django-wp/api/company/all/')
        return { companies: data, search: '' }
      } else {
        let {data} = await axios.get('http://localhost/api/company/all/')
        return { comapnies: data, search: '' }
      }
    },
    methods: {
      formatAddress: function (address) {
        try {
          return address.country + ', ' + address.region + ', ' + address.locality + ', ' + address.steet + ', ' + address.number
        } catch (e) {
          return 'NO ADDRESS'
        }
      }
    },
    computed: {
      filteredCompanies () {
        return this.companies.filter((company) => {
          return company.name.toLowerCase().indexOf(this.search.toLowerCase()) >= 0
        })
      }
    },
    head () {
      return {
        title: 'Companies'
      }
      // Set Meta Tags for this Page
    }
  }
</script>
