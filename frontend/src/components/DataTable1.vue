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
      // results: [
      //   {
      //     results: "https://legal3.com",
      //     website: "unity3d.com",
      //   },
      //   {
      //     results: "https://legal.com",
      //     website: "unity3d.com",
      //   },
      //   {
      //     results: "https://legal2.com",
      //     website: "unity3d.com",
      //   },
      // ],
    };
  },
  mounted() {
    this.$store.dispatch("fetchResults");
  },
  methods: {
    loadall() {
      console.log("load all scrapped item from database");
    },
  },
  computed: {
    ...mapGetters(["getInProgress", "getResultObj"]),
    results() {
      let _r = this.getResultObj;

      if (_r != null) {
        let _results = _r.results.urls;
        let _domain = _r.domain;
        let _final = [];
        for (var i in _results) {
          let _obj = {};
          _obj["website"] = _domain;
          _obj["results"] = _results[i];
          _final.push(_obj);
        }
        return _final;
      }
    },
  },
};
</script>

<style lang="scss" scoped></style>
