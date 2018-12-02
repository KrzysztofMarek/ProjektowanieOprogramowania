<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Sieć restauracji</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        to="/history"
      >
        <v-badge
          overlap
          color="red"
          right
        >
          <v-icon>history</v-icon>
        </v-badge>
      </v-btn>
      <v-btn
        flat
        to="/checkout"
      >
        <v-badge
          overlap
          color="red"
          right
        >
          <span slot="badge">{{ $store.state.order.length }}</span>
          <v-icon>shopping_basket</v-icon>
        </v-badge>
      </v-btn>
    </v-toolbar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      //
    }
  }
}
</script>
