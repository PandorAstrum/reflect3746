<template>
  <v-card>
    <v-select v-model="select" :items="items" label="Select"></v-select>
    <v-card-title>
      Results
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-btn>Load All</v-btn>
    <v-data-table
      :headers="headers"
      :items="results"
      :search="search"
    ></v-data-table>
  </v-card>
</template>

<script>
export default {
  name: "DataTable1",
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Website",
          align: "start",
          sortable: false,
          value: "website",
        },
        { text: "Terms", value: "termsurl" },
        { text: "Privacy", value: "privacyurl" },
        { text: "Cookie", value: "cookieurl" },
      ],
      results: [
        {
          website: "google",
          termsurl: "https://google.com/terms",
          privacyurl: "https://google.com/privacy",
          cookieurl: "https://google.com/cookie",
        },
        {
          website: "facebook",
          termsurl: "https://google.com/terms",
          privacyurl: "https://google.com/terms",
          cookieurl: "https://google.com/terms",
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped></style>
