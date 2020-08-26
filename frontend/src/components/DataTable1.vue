<template>
  <v-card>
    <v-card-title>
      <v-btn block color="secondary" @click="loadall">Load All</v-btn>
      <v-spacer></v-spacer>
    </v-card-title>

    <v-data-table
      :headers="headers"
      :items="results"
      item-key="results"
      sort-by="results"
      group-by="website"
      class="elevation-1"
      :loading="getInProgress"
      loading-text="Loading... Please wait"
    >
      <template v-slot:item.results="{ item }">
        <a :href="item.results">{{ item.results }}</a>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "DataTable1",
  data() {
    return {
      headers: [
        {
          text: "Scrapped Data",
          align: "left",
          value: "results",
          groupable: false,
        },
      ],
    };
  },
  mounted() {
    this.$store.dispatch("fetchResults");
  },
  methods: {
    loadall() {
      this.$store.dispatch("fetchAllResults");
    },
  },
  computed: {
    ...mapGetters(["getInProgress", "getResultList"]),
    results() {
      let _r = this.getResultList;

      if (_r != null && _r.length > 0) {
        let _final = [];
        for (var i in _r) {
          let _results = _r[i].results.urls;
          let _domain = _r[i].domain;
          for (var _u in _results) {
            let _obj = {};
            _obj["website"] = _domain;
            _obj["results"] = _results[_u];
            _final.push(_obj);
          }
        }
        return _final;
      }
    },
  },
};
</script>

<style lang="scss" scoped></style>
