import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

import home from "./modules/home";

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

    // status card items

    spiderSelection: [],
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
    getSpiderSelection: (state) => {
      return state.spiderSelection;
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

  mutations: {
    setSpiderSelection: (state, list) => {
      state.spiderSelection = list;
    },
  },

  actions: {
    spiderList: async ({ commit }) => {
      await axios
        .get("http://127.0.0.1:5000/api/v1/spider")
        .then((response) => {
          let _temp = [];
          for (var k of response.data) {
            _temp.push(k.name);
          }
          commit("setSpiderSelection", _temp);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    startJobs: async ({ commit, state }) => {},
    stopJobs: async ({ commit }) => {},
  },
  modules: {
    home,
  },
});
