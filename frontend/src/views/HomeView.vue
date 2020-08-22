<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="3" v-for="card in status" :key="card.cardfor">
        <StatusCard
          :Cardfor="card.cardfor"
          :Headtext="card.headtext"
          :Innertext="card.innertext"
          :Currstatus="card.currstatus"
        ></StatusCard>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import StatusCard from "../components/StatusCard";

export default {
  name: "HomeView",
  components: {
    StatusCard,
  },
  data() {
    return {
      status: [
        {
          cardfor: "Server",
          headtext: "STATUS",
          innertext: "Running on Node: Ariel",
          currstatus: "green",
        },
        {
          cardfor: "0",
          headtext: "JOBS",
          innertext: "Completed",
          currstatus: "grey",
        },
        {
          cardfor: "0",
          headtext: "JOBS",
          innertext: "Running",
          currstatus: "green",
        },
        {
          cardfor: "0",
          headtext: "JOBS",
          innertext: "Pending",
          currstatus: "yellow",
        },
        {
          cardfor: "0",
          headtext: "JOBS",
          innertext: "Error",
          currstatus: "red",
        },
      ],
    };
  },
  methods: {
    // axios call http://127.0.0.1:6800/daemonstatus.json
    //return back {"node_name": "Ariel", "status": "ok", "pending": 0, "running": 0, "finished": 0}
  },
};
</script>
