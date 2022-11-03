<template>
  <div class="app">
    <RouterView></RouterView>
  </div>
</template>

<script>

import { RouterView } from "vue-router";
export default {
  name: "App",
  components: { RouterView },
};
</script>

<style lang="sass" scoped></style>
