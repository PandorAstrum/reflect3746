import axios from "axios";

let state = {
  inProgress: false,
  isCompleted: false,
  spiderSelection: [],
};
let mutations = {
  setInProgress: (state, status) => {
    state.inProgress = status;
  },
  setIsCompleted: (state, status) => {
    state.isCompleted = status;
  },
  setSpiderSelection: (state, list) => {
    state.spiderSelection = list;
  },
};

let actions = {
  spiderList: async ({ commit }) => {
    await axios
      .get("http://127.0.0.1:5000/api/v1/spider")
      .then((response) => {
        if (response.data.error == "Not Connected") {
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
  },
  runSpider: async ({ commit }, params) => {
    commit("setInProgress", true);
    await axios
      .post("http://127.0.0.1:5000/api/v1/run", params)
      .then((response) => {})
      .catch((error) => {
        console.log(error);
      });
  },
};
let getters = {
  getInProgress: (state) => {
    return state.inProgress;
  },
  getIsCompleted: (state) => {
    return state.isCompleted;
  },
  getSpiderSelection: (state) => {
    return state.spiderSelection;
  },
};

export default {
  state,
  mutations,
  actions,
  getters,
};
