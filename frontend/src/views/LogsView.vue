<template>
  <div>
    <h1>List of scrapper</h1>
    <div class="mx-2 my-2">
      <v-btn block color="secondary" @click="reload">Reload</v-btn>
    </div>
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Website</th>
            <th class="text-left">Results ID</th>
            <th class="text-left">Spider Name</th>
            <th class="text-left">Timestamp</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in getLogList" :key="item._id">
            <td>{{ item.domain }}</td>
            <td>
              <a href="#" @click.prevent="callData($event, item.job_id)">{{ item.job_id }}</a>
            </td>
            <td>{{ item.spidername }}</td>
            <td>{{ item.timestamp | dateFormater }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "LogsView",
  data() {
    return {
      scraperlist: [{ name: "default", domain: "all" }],
    };
  },
  created() {
    this.$store.dispatch("fetchAllLogs");
  },
  computed: {
    ...mapGetters(["getLogList"]),
    ...mapActions(["fetchAllLogs"]),
  },
  methods: {
    reload() {
      this.fetchAllLogs;
    },
    callData(event, _id) {
      this.$store.commit("setResultsID", _id);
      this.$router.push("/data");
    },
  },
};
</script>

<style lang="scss" scoped></style>
