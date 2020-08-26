import axios from "axios";

let state = {
  resultList: null,
};
let mutations = {
  setResultList: (state, _list) => {
    state.resultList = _list;
  },
};

let actions = {
  fetchResults: async ({ commit, rootState }) => {
    console.log(rootState.logs.resultsID);
    if (rootState.logs.resultsID != null) {
      await axios
        .get(`http://127.0.0.1:5000/api/v1/results/${rootState.logs.resultsID}`)
        .then((response) => {
          commit("setResultList", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  fetchAllResults: async ({ commit }) => {
    await axios
      .get(`http://127.0.0.1:5000/api/v1/all`)
      .then((response) => {
        commit("setResultList", response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
let getters = {
  getResultList: (state) => {
    return state.resultList;
  },
};

export default {
  state,
  mutations,
  actions,
  getters,
};
