<template>
  <v-container>
    <v-row class="mx-3 my-3">
      <v-btn block color="secondary" @click="reload">Reload</v-btn>
    </v-row>
    <v-card>
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
    </v-card>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "LogsView",
  mounted() {
    this.$store.dispatch("fetchAllLogs");
  },
  computed: {
    ...mapGetters(["getLogList"]),
  },
  methods: {
    reload() {
      this.$store.dispatch("updateLogs");
    },
    callData(event, _id) {
      this.$store.commit("setResultsID", _id);
      this.$store.dispatch("fetchResultsByID");
      this.$router.push("/data");
    },
  },
};
</script>

<style lang="scss" scoped></style>
