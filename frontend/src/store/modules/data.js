import axios from "axios";

let state = {
  resultObj: null,
};
let mutations = {
  setResultObj: (state, obj) => {
    state.resultObj = obj;
  },
};

let actions = {
  fetchResults: async ({ commit, rootState }) => {
    console.log(rootState.logs.resultsID);
    if (rootState.logs.resultsID != null) {
      await axios
        .get(`http://127.0.0.1:5000/api/v1/results/${rootState.logs.resultsID}`)
        .then((response) => {
          commit("setResultObj", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
};
let getters = {
  getResultObj: (state) => {
    return state.resultObj;
  },
};

export default {
  state,
  mutations,
  actions,
  getters,
};
