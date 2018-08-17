<template>
  <v-app>
    <v-navigation-drawer fixed clipped app v-model="drawer" floating>
      <v-list>
        <v-list-tile
          value="true"
          v-for="(item, i) in drawItems"
          :key="i"
          :to="{ path: item.url }"
        >
          <v-list-tile-action>
            <v-icon v-html="item.icon"></v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title v-text="item.title"></v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar 
      color="blue darken-3" 
      dark 
      app 
      :clipped-left="$vuetify.breakpoint.mdAndUp" 
      fixed
    >
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon >
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
    <v-content>
      <v-fade-transition mode="out-in">
        <router-view/>
      </v-fade-transition>
    </v-content>
    <v-footer :fixed="fixed" app>
      <span>&copy; 2018</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      drawer: true,
      fixed: false,
      drawItems: [
        {
          icon: 'bubble_chart',
          title: 'Inspire',
          url: '/index'
        },
        {
          icon: 'bubble_chart',
          title: 'Inspire',
          url: '/index'
        },
        {
          icon: 'bubble_chart',
          title: 'Inspire',
          url: '/index'
        },
        {
          icon: 'bubble_chart',
          title: 'Inspire',
          url: '/index'
        }
      ],
      title: 'V2ray.Fun'
    }
  },
  name: 'App'
}
</script>
