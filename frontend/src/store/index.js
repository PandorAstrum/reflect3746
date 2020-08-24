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
    jobsRunning: false,
    spiderSelection: [],
    siteMap: false,
    dynamicJS: false,
    customProxie: false,
    proxiList: [],
    customAgents: false,
    userAgents: "",
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
    getSpiderSelection: (state) => {
      return state.spiderSelection;
    },
    getJobsRunning: (state) => {
      return state.jobsRunning;
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
    setServerStatus: (state, status) => {
      state.serverStatus = status;
    },
    setDatabaseStatus: (state, status) => {
      state.databaseStatus = status;
    },
    setJobsRunning: (state, status) => {
      state.jobsRunning = status;
    },
    setSpiderSelection: (state, list) => {
      state.spiderSelection = list;
    },
  },

  actions: {
    refServer: async ({ commit }) => {
      await axios
        .get("http://127.0.0.1:5000/api/v1/server_status")
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
        .get("http://127.0.0.1:5000/api/v1/database_status")
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
    startJobs: async ({ commit, state }) => {
      if (!state.jobsRunning) {
        // axios call to start the scraper
      }
    },
    stopJobs: async ({ commit }) => {},
  },
  modules: {},
});
