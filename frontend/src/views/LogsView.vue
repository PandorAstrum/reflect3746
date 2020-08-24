<template>
  <div>
    <h1>List of scrapper</h1>
    <div class="mx-2 my-2">
      <v-btn large color="primary">Add New</v-btn>
      <v-btn large>Reload</v-btn>
    </div>
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Scraper Name</th>
            <th class="text-left">Applicable Domain</th>
            <th class="text-left">Scraper Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in scraperlist" :key="item.name">
            <td>{{ item.name }}</td>
            <td>{{ item.domain }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: "LogsView",
  data() {
    return {
      scraperlist: [{ name: "default", domain: "all" }],
    };
  },
};
</script>

<style lang="scss" scoped></style>
