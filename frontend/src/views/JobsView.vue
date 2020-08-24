<template>
  <v-container>
    <v-form>
      <v-row>
        <v-col cols="1" class="mx-auto my-auto">
          <v-subheader>WEBSITE</v-subheader>
        </v-col>
        <v-col cols="11">
          <v-text-field v-model="url" :counter="10" label="URL" required></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="1" class="mx-auto my-auto">
          <v-subheader>SPIDER</v-subheader>
        </v-col>
        <v-col cols="11">
          <v-select
            v-model="select"
            :items="getSpiderSelection"
            :rules="[(v) => !!v || 'Please Select a spider or create new']"
            label="Select"
            required
          ></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="1" class="mx-auto">
          <v-subheader>SETTINGS</v-subheader>
        </v-col>
        <v-col cols="11">
          <v-row>
            <v-switch class="mx-4" v-model="siteMap" label="Sitemap (If exist)"></v-switch>
            <v-switch class="mx-4" v-model="dynamicJS" label="DynamicJS"></v-switch>
          </v-row>
          <v-row>
            <v-switch class="mx-4" v-model="customAgents" label="Custom User Agents"></v-switch>
            <v-text-field
              label="User-Agents"
              hint="enter multiple with commas"
              :disabled="!customAgents"
            ></v-text-field>
          </v-row>
          <v-row>
            <v-switch class="mx-4" v-model="customProxie" label="Custom Proxy"></v-switch>
            <v-text-field
              label="proxies"
              hint="enter multiple with commas"
              :disabled="!customProxie"
            ></v-text-field>
          </v-row>
        </v-col>
      </v-row>

      <v-btn block large @click="buildSelection">Run</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "JobsView",
  data() {
    return {
      url: "",
      select: null,
      siteMap: false,
      dynamicJS: false,
      customProxie: false,
      customAgents: false,
    };
  },
  mounted() {
    this.$store.dispatch("spiderList");
  },
  methods: {
    buildSelection: () => {
      let s = this.ss;
      console.log(s);
    },
  },
  computed: {
    ...mapGetters([
      "getSiteMap",
      "getDynamicJS",
      "getcustomProxie",
      "getCustomAgents",
      "getSpiderSelection",
    ]),
  },
};
</script>

<style lang="scss" scoped></style>
