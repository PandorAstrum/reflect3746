import axios from "axios";

let state = {
  serverStatus: false,
  serverHost: "",
  databaseStatus: false,
  jobsRunning: false,
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
  setJobsRunning: (state, status) => {
    state.jobsRunning = status;
  },
};

let actions = {
  refServer: async ({ commit }) => {
    await axios
      .get("http://127.0.0.1:5000/api/v1/server_status")
      .then((response) => {
        if (response.data.status == 200) {
          commit("setServerStatus", true);
          commit("setServerHost", response.data.host);
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
  getJobsRunning: (state) => {
    return state.jobsRunning;
  },
};

export default {
  state,
  mutations,
  actions,
  getters,
};
