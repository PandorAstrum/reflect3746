import axios from "axios";

let state = {
  logList: [],
  resultsID: null,
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
  fetchAllLogs: async ({ commit }) => {
    await axios
      .get("http://127.0.0.1:5000/api/v1/logs")
      .then((response) => {
        commit("setLogList", response.data);
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
