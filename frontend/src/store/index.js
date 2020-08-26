import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

import home from "./modules/home";
import jobs from "./modules/jobs";

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
    siteMap: false,
    dynamicJS: false,
    customProxie: false,
    proxiList: [],
    customAgents: false,
    userAgents: "",
  },

  getters: {
    getMenus: (state) => {
      return state.menus;
    },

    getSiteMap: (state) => {
      return state.siteMap;
    },
    getDynamicJS: (state) => {
      return state.dynamicJS;
    },
    getcustomProxie: (state) => {
      return state.customProxie;
    },
    getProxiList: (state) => {
      return state.proxiList;
    },
    getCustomAgents: (state) => {
      return state.customAgents;
    },
    getUserAgents: (state) => {
      return state.userAgents;
    },
  },

  mutations: {},

  actions: {
    startJobs: async ({ commit, state }) => {},
    stopJobs: async ({ commit }) => {},
  },
  modules: {
    home,
    jobs,
  },
});
