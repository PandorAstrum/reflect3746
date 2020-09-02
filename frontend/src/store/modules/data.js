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

                if (response.data.urls.length > 0) {
                  dispatch("updateLogs", null, { root: true });
                  let _domain = rootState.jobs.hostName;
                  let _urls = response.data.urls;
                  let _id = response.data._id;

                  let _obj = { domain: _domain, urls: _urls, _id: _id };

                  let _records = [];
                  _records.push(_obj);
                  console.log(_records);

                  commit("setResultList", _records);
                } else {
                  alert("No data found");
                }
              }
            }
            if (response.data.Status === 400) {
              commit("setInProgress", false, { root: true });
              if (rootState.jobs.inProgress === false) {
                clearInterval(_timer);
                alert(response.data.msg);
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

  mutateDoc: async ({ commit }, params) => {
    await axios
      .post(`http://127.0.0.1:5000/api/v1/mutations`, params)
      .then((response) => {
        if (response.status === 200) {
          commit("setResultList", []);
          commit("setResultList", response.data);
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },

  deleteDoc: async ({ commit }, params) => {
    await axios
      .post(`http://127.0.0.1:5000/api/v1/deletion`, params)
      .then((response) => {
        if (response.status === 200) {
          commit("setResultList", []);
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
