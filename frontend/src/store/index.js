import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

import home from "./modules/home";
import jobs from "./modules/jobs";
import logs from "./modules/logs";
import data from "./modules/data";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // menu
    menus: [
      { title: "home", icon: "mdi-home-variant", route: "/" },
      { title: "Jobs", icon: "mdi-rocket", route: "/jobs" },
      { title: "Logs", icon: "mdi-clipboard-edit", route: "/logs" },
      { title: "Data", icon: "mdi-database", route: "/data" },
    ],
  },

  getters: {
    getMenus: (state) => {
      return state.menus;
    },
  },
  mutations: {},
  actions: {},
  modules: {
    home,
    jobs,
    logs,
    data,
  },
});
