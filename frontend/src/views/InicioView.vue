<template>
  <div class="app">
    <SpaceBackground class="background spaceBackground"></SpaceBackground>
    <WidgetWorkspace class="background widgetWorkspace"></WidgetWorkspace>
  </div>
</template>

<script>
import SpaceBackground from "../components/SpaceBackground.vue";
import WidgetWorkspace from "../components/WidgetWorkspace.vue";
export default {
  name: "InicioView",
  components: { SpaceBackground, WidgetWorkspace },
};
</script>

<style scoped>
.app {
  position: relative;
}

.background {
  position: relative;
}
.widgetWorkspace {
  z-index: 2;
}

.spaceBackground {
  z-index: 1;
}
</style>
