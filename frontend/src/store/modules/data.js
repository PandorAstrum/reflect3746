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
  fetchResultsByID: async ({ commit, rootState }) => {
    if (rootState.jobs.inProgress === false) {
      if (rootState.logs.resultsID !== "") {
        await axios
          .get(
            `http://127.0.0.1:5000/api/v1/results/${rootState.logs.resultsID}`
          )
          .then((response) => {
            if (response.status === 200) {
              commit("setResultList", []);
              commit("setResultList", response.data);
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    }
    commit("setResultsID", "");
  },

  fetchResultsInterval: async ({ commit, rootState, dispatch }) => {
    if (rootState.jobs.inProgress === true) {
      let _timer = setInterval(() => {
        axios
          .get("http://127.0.0.1:5000/api/v1/results")
          .then((response) => {
            if (response.data.Status === 200) {
              commit("setInProgress", false, { root: true });
              if (rootState.jobs.inProgress === false) {
                clearInterval(_timer);
                dispatch("updateLogs", null, { root: true });
                let _domain = rootState.jobs.hostName;
                let _obj = { domain: "", results: { urls: [] } };
                for (var item in response.data.records) {
                  _obj["results"]["urls"].push(
                    response.data.records[item].urls
                  );
                }
                _obj["domain"] = _domain;
                let _records = [];
                _records.push(_obj);

                commit("setResultList", _records);
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
        if (response.status === 200) {
          commit("setResultList", response.data);
        }
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
