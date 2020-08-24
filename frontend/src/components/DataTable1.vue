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
    <v-data-table :headers="headers" :items="results" :search="search">
      <template v-slot:item.termsurl="{ item }">
        <v-chip :color="getColor(item.termsurl)" dark>
          <a :href="item.termsurl">{{ item.termsurl }}</a>
        </v-chip>
      </template>
      <template v-slot:item.privacyurl="{ item }">
        <v-chip :color="getColor(item.privacyurl)" dark>
          <a :href="item.privacyurl">{{ item.privacyurl }}</a>
        </v-chip>
      </template>
      <template v-slot:item.cookieurl="{ item }">
        <v-chip :color="getColor(item.cookieurl)" dark>
          <a :href="item.cookieurl">{{ item.cookieurl }}</a>
        </v-chip>
      </template>
    </v-data-table>
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
          termsurl: "https://policies.google.com/terms?hl=en-BD&fg=1",
          privacyurl: "https://policies.google.com/privacy?hl=en-BD&fg=1",
          cookieurl: "N/A",
        },
        {
          website: "facebook",
          termsurl: "https://www.facebook.com/legal/terms",
          privacyurl: "https://www.facebook.com/privacy/explanation",
          cookieurl: "https://www.facebook.com/policies/cookies/",
        },
      ],
    };
  },
  methods: {
    getColor(url) {
      if (url != "N/A") return "green lighten-4";
      else return "red lighten-4";
    },
  },
};
</script>

<style lang="scss" scoped></style>
