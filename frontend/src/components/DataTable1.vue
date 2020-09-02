<template>
  <v-card>
    <v-card-title>
      <v-btn block color="secondary" @click="loadall" :disabled="getInProgress">Load All</v-btn>
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
      loading-text="Scraping... Please wait"
    >
      <template v-slot:item.urls="{ item }">
        <a :href="item.urls">{{ item.urls }}</a>
        <div v-show="false">{{item.ids}}</div>
        <v-btn icon @click="appearDialog($event, item.ids, item.urls)">
          <v-icon>mdi-lead-pencil</v-icon>
        </v-btn>

        <v-btn icon @click="remove">
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </template>
    </v-data-table>
    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="headline grey lighten-2">Edit</v-card-title>
        <v-text-field autofocus v-model="modified_entry"></v-text-field>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="edit($event, selected_ids, modified_entry)">Okay</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "DataTable1",
  data() {
    return {
      dialog: false,
      old_entry: "",
      modified_entry: "",
      selected_ids: "",
      headers: [
        {
          text: "Scrapped Data",
          align: "left",
          value: "urls",
          groupable: true,
        },
      ],
      // results: [
      //   {
      //     website: "epicgames.com",
      //     urls: "https://www.epicgames.com/site/en-US/tos",
      //     ids: "5f4990f7bc8ced173b18cbf4",
      //   },
      //   {
      //     website: "epicgames.com",
      //     urls: "https://www.epicgames.com/site/en-US/privacypolicy",
      //     ids: "5f4990f7bc8ced173b18cbf4",
      //   },
      // ],
    };
  },
  methods: {
    loadall() {
      this.$store.dispatch("fetchAllResults");
    },
    appearDialog(event, ids, entry) {
      this.old_entry = entry;
      this.modified_entry = entry;
      this.selected_ids = ids;
      return (this.dialog = !this.dialog);
    },
    edit(event, ids, new_entry) {
      this.dialog = false;
      // TODO: call action to mutation mongodb with selected ids and selected urls
      this.$store.dispatch("mutateDoc", {
        _id: this.selected_ids,
        old_entry: this.old_entry,
        modified_entry: new_entry,
      });
    },
    remove(event, ids, urls) {
      alert(`ids: ${ids} and urls ${urls}`);
      // TODO: call action to mutation mongodb with selected ids and selected urls
    },
  },
  computed: {
    ...mapGetters(["getInProgress", "getResultList"]),

    // TODO:
    results() {
      let _r = this.getResultList;
      let _final = [];
      for (var i in _r) {
        let _urls = _r[i].urls;
        let _domain = _r[i].domain;
        let _ids = _r[i]._id;
        for (var _u in _urls) {
          let _obj = {};
          _obj["website"] = _domain;
          _obj["urls"] = _urls[_u];
          _obj["ids"] = _ids;
          _final.push(_obj);
        }
      }
      return _final;
    },
  },
};
</script>

<style lang="scss" scoped></style>
