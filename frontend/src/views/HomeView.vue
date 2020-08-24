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
  created() {
    this.$store.dispatch("refServer");
    this.$store.dispatch("refDatabase");
  },
  methods: {
    ...mapActions(["refServer", "refDatabase", "stopJobs"]),
    gotoLogs() {
      // route to logs
      this.$router.push("/logs");
    },
    gotoJobs() {
      // rote to jobs
      this.$router.push("/jobs");
    },
  },
  computed: {
    ...mapGetters(["getServerStatus", "getDatabaseStatus", "getJobsRunning"]),
    cards() {
      let _cards = [
        {
          name: "Server",
          status: this.getServerStatus ? "green lighten-1" : "red lighten-1",
          inner: this.getServerStatus
            ? "Running on port 5000"
            : "Not Connected",
          header: "STATUS",
          btn: [{ text: "REFRESH", action: this.refServer }],
        },
        {
          name: "Database",
          status: this.getDatabaseStatus ? "green lighten-1" : "red lighten-1",
          inner: this.getDatabaseStatus ? "SQLITE Connected" : "Not Connected",
          header: "STATUS",
          btn: [{ text: "REFRESH", action: this.refDatabase }],
        },
        {
          name: "Running",
          status: this.getJobsRunning ? "green lighten-1" : "grey lighten-1",
          inner: this.getJobsRunning ? "" : "None",
          header: "JOBS",
          btn: this.getJobsRunning
            ? [{ text: "STOP", action: this.stopJobs }]
            : [{ text: "CREATE JOB", action: this.gotoJobs }],
        },
        {
          name: "Logs",
          status: "",
          inner: "All scraped data and errors",
          header: "STATUS",
          btn: [{ text: "GO TO LOGS", action: this.gotoLogs }],
        },
      ];
      return _cards;
    },
  },
};
</script>
