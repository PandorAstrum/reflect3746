<template>
  <v-card>
    <v-card-title>
      <v-btn block dark @click="loadall">Load All</v-btn>
      <v-spacer></v-spacer>Results
    </v-card-title>

    <v-data-table
      :headers="headers"
      :items="results"
      item-key="name"
      sort-by="name"
      group-by="website"
      class="elevation-1"
    >
      <template v-slot:item.name="{ item }">
        <a :href="item.name">{{ item.name }}</a>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
export default {
  name: "DataTable1",
  data() {
    return {
      headers: [
        {
          text: "Scrapped Data",
          align: "start",
          value: "name",
          groupable: false,
        },
        { text: "Website", value: "website", align: "right" },
        { text: "Category", value: "category", align: "right" },
      ],
      results: [
        {
          name: "https://legal3.com",
          website: "unity3d.com",
          category: "terms",
        },
        {
          name: "https://legal.com",
          website: "unity3d.com",
          category: "privacy",
        },
        {
          name: "https://legal2.com",
          website: "unity3d.com",
          category: "policy",
        },
      ],

      search: "",
    };
  },
  methods: {
    loadall() {
      console.log("load all scrapped item from database");
    },
  },
};
</script>

<style lang="scss" scoped></style>
