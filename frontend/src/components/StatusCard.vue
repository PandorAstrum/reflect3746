<template>
  <v-card class max-width="344" outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">{{ properties.header }}</div>
        <v-list-item-title class="headline mb-1">
          {{
          properties.name
          }}
        </v-list-item-title>
        <v-list-item-subtitle>{{ properties.inner }}</v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar size="20" :color="properties.status"></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn text @click="properties.btn.action">{{ properties.btn.text }}</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "StatusCard",
  props: ["properties"],
};
</script>

<style lang="scss" scoped></style>
