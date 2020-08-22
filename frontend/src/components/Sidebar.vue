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

    <v-list dense>
      <v-list-item
        v-for="item in items"
        :key="item.title"
        link
        router
        :to="item.routeto"
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
  <!-- <v-card>
    <v-navigation-drawer v-model="drawer" :mini-variant.sync="mini" permanent>
      
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/85.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-title>John Leider</v-list-item-title>

        
      </v-list-item>

      <v-divider></v-divider>

      
    </v-navigation-drawer>
  </v-card> -->
</template>

<script>
export default {
  name: "Sidebar",
  data() {
    return {
      drawer: true,
      items: [
        { title: "Home", icon: "mdi-home-variant", routeto: "/" },
        { title: "Scraper", icon: "mdi-magnet", routeto: "/scraper" },
        { title: "Jobs", icon: "mdi-rocket", routeto: "/jobs" },
        { title: "Data", icon: "mdi-database", routeto: "/data" },
      ],
      mini: true,
    };
  },
};
</script>
