<template>
  <v-container>
    <form>
      <v-row>
        <v-col cols="1" class="mx-auto my-auto">
          <v-subheader>WEBSITE</v-subheader>
        </v-col>
        <v-col cols="11">
          <v-text-field
            v-model="website"
            :error-messages="websiteErrors"
            label="URL"
            required
            @input="$v.website.$touch()"
            @blur="$v.website.$touch()"
          ></v-text-field>
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
            :error-messages="selectErrors"
            label="Select"
            required
            @change="$v.select.$touch()"
            @blur="$v.select.$touch()"
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
          </v-row>
          <v-row>
            <v-switch class="mx-4" v-model="downloadDelay" label="Delay"></v-switch>
            <v-text-field v-model="delay" hint="enter seconds" :disabled="!downloadDelay"></v-text-field>
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
      <v-btn
        block
        large
        color="secondary"
        :loading="getInProgress"
        :disabled="getInProgress"
        @click="runSpider"
      >Run</v-btn>
    </form>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import { validationMixin } from "vuelidate";
import { required, url } from "vuelidate/lib/validators";
export default {
  name: "JobsView",
  mixins: [validationMixin],
  validations: {
    website: { required, url },
    select: { required },
  },
  data() {
    return {
      website: "",
      select: null,
      siteMap: false,
      downloadDelay: false,
      delay: 1,
      customProxie: false,
    };
  },
  mounted() {
    this.$store.dispatch("spiderList");
  },
  methods: {
    runSpider() {
      this.$v.$touch();
      if (this.$v.$invalid) {
      } else {
        // build form data
        let params = {
          spider_kwargs: {
            baseurl: this.website,
            spider_name: this.select,
          },
          spider_settings: {
            sitemap: this.siteMap,
            delay: this.delay,
          },
        };

        function extractHostname(url) {
          var hostname;
          //find & remove protocol (http, ftp, etc.) and get hostname

          if (url.indexOf("//") > -1) {
            hostname = url.split("/")[2];
          } else {
            hostname = url.split("/")[0];
          }

          //find & remove port number
          hostname = hostname.split(":")[0];
          //find & remove "?"
          hostname = hostname.split("?")[0];

          return hostname;
        }
        this.$store.commit("setHostName", extractHostname(this.website));

        this.$store.dispatch("runSpider", params); // call actions pass obj as param
        this.$router.push("/data");
      }
    },
  },
  computed: {
    ...mapGetters(["getSpiderSelection", "getInProgress"]),
    selectErrors() {
      const errors = [];
      if (!this.$v.select.$dirty) return errors;
      !this.$v.select.required && errors.push("Please select a spider");
      return errors;
    },
    websiteErrors() {
      const errors = [];
      if (!this.$v.website.$dirty) return errors;
      !this.$v.website.url &&
        errors.push("Not a valid url (e.g: https://example.com)");
      !this.$v.website.required && errors.push("Please provide an url");
      return errors;
    },
  },
};
</script>

<style lang="scss" scoped></style>
