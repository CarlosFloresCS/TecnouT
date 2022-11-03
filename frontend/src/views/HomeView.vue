<template>
  <div class="app">
    <home-navigation></home-navigation>
    <home-main></home-main>
    <home-footer></home-footer>
  </div>
</template>

<script>
import HomeFooter from "../components/HomeFooter.vue";
import HomeMain from "../components/HomeMain.vue";
import HomeNavigation from "../components/HomeNavigation.vue";
export default {
  components: { HomeNavigation, HomeFooter, HomeMain },
  name: "App",
};
</script>

<style lang="scss" scoped>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: "Raleway", sans-serif;
  font-weight: 400;
}
.app {
  min-height: 100vh;
  position: relative;
  background-color: #f1f1f1;
}
.container {
  padding: 0 20px;
  max-width: 1140px;
  margin: 0 auto;
}
</style>
