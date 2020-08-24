<template>
  <v-navigation-drawer
    v-model="drawer"
    app
    color="grey lighten-2"
    :mini-variant.sync="mini"
    permanent
  >
    <v-list-item class="px-2">
      <v-btn icon @click.stop="mini = !mini">
        <v-icon v-if="mini">mdi-chevron-right</v-icon>
        <v-icon v-else>mdi-chevron-left</v-icon>
      </v-btn>
    </v-list-item>
    <v-divider></v-divider>

    <v-list>
      <v-list-item v-for="menu in getMenus" :key="menu.title" link router :to="menu.route">
        <v-list-item-icon>
          <v-icon>{{ menu.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ menu.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Sidebar",
  data() {
    return {
      drawer: true,
      menus: [],
      mini: true,
    };
  },
  // mounted: {
  //   this.menu = getMenus;
  // },
  computed: {
    ...mapGetters(["getMenus"]),
  },
};
</script>
