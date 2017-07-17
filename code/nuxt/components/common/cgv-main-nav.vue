<template>

   <v-navigation-drawer
      class="pb-0"
      permanent
      mini-variant
      absolute
      height="100%"
      clipped
      enable-resize-watcher
      v-model="isOpen"
    >
      <v-list dense>
        <v-list-tile v-for="item in menu" :key="item.text" nuxt :to="item.path">
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>

            <v-list-tile-content>
              <v-list-tile-title>{{ item.text }}</v-list-tile-title>
            </v-list-tile-content>
        </v-list-tile>

      </v-list>

    </v-navigation-drawer>


</template>


<script>
export default {
  props: ['isOpen'],
  data () {
    return {
      _isOpen: this.isOpen,
      menu: [
        { icon: 'home', text: 'Users', path: '/' },
        { icon: 'trending_up', text: 'Users', path: '/user' },
        { icon: 'trending_up', text: 'Companies', path: '/companies' }
      ]
    }
  }
}
</script>
