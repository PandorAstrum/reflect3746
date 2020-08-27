import axios from "axios";

let state = {
  resultList: [],
};
let mutations = {
  setResultList: (state, _list) => {
    state.resultList = _list;
  },
};

let actions = {
  fetchResults: async ({ commit, rootState }) => {
    if (!!rootState.logs.resultsID || !rootState.logs.resultsID.length) {
      await axios
        .get(`http://127.0.0.1:5000/api/v1/results/${rootState.logs.resultsID}`)
        .then((response) => {
          commit("setResultList", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    } else {
    }

    if (rootState.jobs.inProgress === true) {
      commit("setResultList", []);
      let _timer = setInterval(() => {
        axios
          .get("http://127.0.0.1:5000/api/v1/results")
          .then((response) => {
            if (response.data.Status == 200) {
              console.log("scraping complete ");

              commit("setInProgress", false, { root: true });
              commit("setResultList", response.data.records);

              if (rootState.jobs.inProgress === false) {
                clearInterval(_timer);
              }
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }, 5000);
    }
  },

  fetchAllResults: async ({ commit }) => {
    commit("setResultList", []);
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
