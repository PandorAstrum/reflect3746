<template>
  <v-app>
    <Sidebar></Sidebar>
    <Navbar></Navbar>
    <!-- Sizes your content based upon application components -->
    <v-main>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script>
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";

export default {
  name: "App",

  components: {
    Navbar,
    Sidebar,
  },

  data: () => ({
    drawer: false,
  }),
};
</script>
