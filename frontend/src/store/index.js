import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    menus: [
      { title: "home", icon: "mdi-home-variant", route: "/" },
      { title: "Jobs", icon: "mdi-rocket", route: "/jobs" },
      { title: "Logs", icon: "mdi-clipboard-edit", route: "/logs" },
      { title: "Data", icon: "mdi-database", route: "/data" },
    ],
    serverStatus: false,
    databaseStatus: false,
  },

  getters: {
    getServerStatus: (state) => {
      return state.serverStatus;
    },
    getDatabaseStatus: (state) => {
      return state.databaseStatus;
    },
    getMenus: (state) => {
      return state.menus;
    },
  },

  mutations: {
    setServerStatus: (state, status) => {
      state.serverStatus = status;
    },
    setDatabaseStatus: (state, status) => {
      state.databaseStatus = status;
    },
  },

  actions: {
    refServer: async ({ commit }) => {
      await axios
        .get("http://127.0.0.1:5000/api/v1.0/server")
        .then((response) => {
          if (response.data == "ok") {
            commit("setServerStatus", true);
          }
        })
        .catch((error) => {
          commit("setServerStatus", false);
          console.log(error);
        });
    },
    refDatabase: async ({ commit }) => {
      await axios
        .get("http://127.0.0.1:5000/api/v1.0/database")
        .then((response) => {
          if (response.data == "ok") {
            commit("setDatabaseStatus", true);
          }
        })
        .catch((error) => {
          commit("setDatabaseStatus", false);
          console.log(error);
        });
    },
  },
  modules: {},
});
