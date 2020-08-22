<template>
  <v-container>
    <v-form>
      <v-row>
        <v-col cols="1" class="mx-auto my-auto"
          ><v-subheader>WEBSITE</v-subheader></v-col
        >
        <v-col cols="11">
          <v-text-field
            v-model="firstname"
            :rules="nameRules"
            :counter="10"
            label="URL"
            required
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="1" class="mx-auto my-auto">
          <v-subheader>SPIDER</v-subheader></v-col
        >
        <v-col cols="11">
          <v-select
            v-model="select"
            :items="items"
            :rules="[(v) => !!v || 'Please Select a spider or create new']"
            label="Select"
            required
          ></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="1" class="mx-auto"
          ><v-subheader>OPTIONS</v-subheader></v-col
        >
        <v-col cols="11">
          <v-row>
            <v-switch
              class="mx-4"
              v-model="switch1"
              label="Crawl all links"
              disabled
            ></v-switch>
            <v-switch
              class="mx-4"
              v-model="switch2"
              label="Sitemap search (If available)"
            ></v-switch>
            <v-switch class="mx-4" v-model="switch3" label="Dynamic"></v-switch>
            <v-switch
              class="mx-4"
              v-model="switch4"
              label="Use proxies"
            ></v-switch>
          </v-row>

          <v-text-field
            label="proxies"
            hint="enter multiple with commas"
            :disabled="!switch4"
          ></v-text-field
        ></v-col>
      </v-row>

      <v-btn block large>Run</v-btn>
    </v-form>
  </v-container>
</template>

<script>
export default {
  name: "JobsView",
  data() {
    return {
      select: null,
      items: ["Spider 1", "Spider 2", "Spider 3", "Spider 4"],
      switch1: true,
      switch2: true,
      switch3: true,
      switch4: true,
    };
  },
};
</script>

<style lang="scss" scoped></style>
