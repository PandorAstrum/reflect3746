import axios from "axios";

let state = {
  logList: [],
  resultsID: "",
};
let mutations = {
  setLogList: (state, _list) => {
    state.logList = _list;
  },
  setResultsID: (state, val) => {
    state.resultsID = val;
  },
};

let actions = {
  fetchAllLogs: async ({ commit, state }) => {
    if (state.logList.length <= 0) {
      await axios
        .get("http://127.0.0.1:5000/api/v1/logs")
        .then((response) => {
          if (response.status === 200) commit("setLogList", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  updateLogs: async ({ commit, state }) => {
    commit("setLogList", []);
    await axios
      .get("http://127.0.0.1:5000/api/v1/logs")
      .then((response) => {
        if (response.status === 200) commit("setLogList", response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
let getters = {
  getLogList: (state) => {
    return state.logList;
  },
  getResultsID: (state) => {
    return state.resultsID;
  },
};

export default {
  state,
  mutations,
  actions,
  getters,
};
