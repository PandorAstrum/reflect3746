<template>
  <v-card class="" max-width="344" outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">{{ Headtext }}</div>
        <v-list-item-title class="headline mb-1">{{
          Cardfor
        }}</v-list-item-title>
        <v-list-item-subtitle>{{ Innertext }}</v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar
        tile
        size="40"
        radius="50"
        :color="Currstatus"
      ></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn text>Refresh</v-btn>
      <v-btn text>Disconnect</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "StatusCard",
  props: ["Cardfor", "Headtext", "Innertext", "Currstatus"],
};
</script>

<style lang="scss" scoped></style>
