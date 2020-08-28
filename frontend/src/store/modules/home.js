import axios from "axios";

let state = {
  serverStatus: false,
  serverHost: "",
  databaseStatus: false,
  databaseObj: {},
};
let mutations = {
  setServerStatus: (state, status) => {
    state.serverStatus = status;
  },
  setDatabaseStatus: (state, status) => {
    state.databaseStatus = status;
  },
  setServerHost: (state, t) => {
    state.serverHost = t;
  },
  setDatabaseObj: (state, obj) => {
    state.databaseObj = obj;
  },
};

let actions = {
  refServer: async ({ commit, state }) => {
    if (state.serverHost === "") {
      await axios
        .get("http://127.0.0.1:5000/api/v1/server_status")
        .then((response) => {
          if (response.data.Status === 200) {
            commit("setServerStatus", true);
            commit("setServerHost", response.data.host);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  refDatabase: async ({ commit, state }) => {
    if (Object.keys(state.databaseObj).length === 0) {
      await axios
        .get("http://127.0.0.1:5000/api/v1/database_status")
        .then((response) => {
          if (response.data.Status === 200) {
            commit("setDatabaseStatus", true);
            commit("setDatabaseObj", response.data);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  forceRefreshServer: async ({ commit }) => {
    commit("setServerStatus", false);
    commit("setServerHost", "");
    await axios
      .get("http://127.0.0.1:5000/api/v1/server_status")
      .then((response) => {
        if (response.data.Status === 200) {
          commit("setServerStatus", true);
          commit("setServerHost", response.data.host);
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
  forceRefreshDatabase: async ({ commit }) => {
    commit("setDatabaseStatus", false);
    commit("setDatabaseObj", {});
    await axios
      .get("http://127.0.0.1:5000/api/v1/database_status")
      .then((response) => {
        if (response.data.Status === 200) {
          commit("setDatabaseStatus", true);
          commit("setDatabaseObj", response.data);
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
let getters = {
  getServerStatus: (state) => {
    return state.serverStatus;
  },
  getServerHost: (state) => {
    return state.serverHost;
  },
  getDatabaseStatus: (state) => {
    return state.databaseStatus;
  },
  getDatabaseObj: (state) => {
    return state.databaseObj;
  },
};

export default {
  state,
  mutations,
  actions,
  getters,
};
