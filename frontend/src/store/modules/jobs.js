import axios from "axios";

let state = {
  inProgress: false,
  isCompleted: false,
  spiderSelection: [],
  hostName: "",
};
let mutations = {
  setInProgress: (state, status) => {
    state.inProgress = status;
  },
  setSpiderSelection: (state, list) => {
    state.spiderSelection = list;
  },
  setIsCompleted: (state, status) => {
    state.isCompleted = false;
  },
  setHostName: (state, inputs) => {
    state.hostName = inputs;
  },
};

let actions = {
  spiderList: async ({ commit, state }) => {
    if (!state.spiderSelection.length) {
      await axios
        .get("http://127.0.0.1:5000/api/v1/spider")
        .then((response) => {
          if (response.data.Status === 404) {
            return;
          }
          let _temp = [];
          for (var k of response.data) {
            _temp.push(k.name);
          }
          commit("setSpiderSelection", _temp);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  runSpider: async ({ commit, dispatch }, params) => {
    await axios
      .post("http://127.0.0.1:5000/api/v1/run", params)
      .then((response) => {
        if (response.status === 200) {
          commit("setInProgress", true);
          commit("setResultList", [], { root: true });
          dispatch("fetchResultsInterval", null, { root: true });
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
let getters = {
  getInProgress: (state) => {
    return state.inProgress;
  },
  getSpiderSelection: (state) => {
    return state.spiderSelection;
  },
  getIsCompleted: (state) => {
    return state.isCompleted;
  },
};

export default {
  state,
  mutations,
  actions,
  getters,
};
