<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="3" v-for="(card, index) in cards" :key="index">
        <StatusCard :properties="card"></StatusCard>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import axios from "axios";
import StatusCard from "../components/StatusCard";

export default {
  name: "HomeView",
  components: {
    StatusCard,
  },
  data() {
    return {
      serverStatus: false,
    };
  },
  mounted() {
    this.$store.dispatch("refServer");
    this.$store.dispatch("refDatabase");
  },
  methods: {
    ...mapActions(["refServer", "refDatabase", "stopJobs"]),
    gotoLogs() {
      this.$router.push("/logs"); // route to logs
    },
    gotoJobs() {
      this.$router.push("/jobs"); // rote to jobs
    },
  },
  computed: {
    ...mapGetters([
      "getServerStatus",
      "getServerHost",
      "getDatabaseStatus",
      "getDatabaseObj",
      "getInProgress",
    ]),
    cards() {
      let _cards = [
        {
          name: "Server",
          status: this.getServerStatus ? "green lighten-1" : "red lighten-1",
          inner: this.getServerStatus
            ? `Running on port ${this.getServerHost}`
            : "Not Connected",
          header: "STATUS",
          btn: { text: "REFRESH", action: this.refServer },
        },
        {
          name: "Database",
          status: this.getDatabaseStatus ? "green lighten-1" : "red lighten-1",
          inner: this.getDatabaseStatus
            ? `${this.getDatabaseObj.nodes}`
            : "Not Connected",
          header: "STATUS",
          btn: { text: "REFRESH", action: this.refDatabase },
        },
        {
          name: "Running",
          status: this.getInProgress ? "green lighten-1" : "grey lighten-1",
          inner: this.getInProgress ? "In Progress" : "None",
          header: "JOBS",
          btn: this.getInProgress
            ? {}
            : { text: "CREATE JOB", action: this.gotoJobs },
        },
        {
          name: "Logs",
          status: "",
          inner: "All scraped data and errors",
          header: "STATUS",
          btn: { text: "GO TO LOGS", action: this.gotoLogs },
        },
      ];
      return _cards;
    },
  },
};
</script>
