<template>
  <span class="dynamic-element">
    <div class="toolbar">
      <div class="toolbar-flex">
        <!--ToolbarWidget reloj-->
        <ToolbarWidget
          imgIcon="https://img.icons8.com/dusk/55/null/alarm-clock--v1.png"
          widgetLabel="Timer"
        ></ToolbarWidget>
        <!--ToolbarWidget foro-->
        <ToolbarWidget
          imgIcon="https://img.icons8.com/dusk/55/null/form.png"
          widgetLabel="Foro"
        ></ToolbarWidget>
        <!--ToolbarWidget calendario-->
        <ToolbarWidget
          imgIcon="https://img.icons8.com/dusk/55/null/calendar--v1.png"
          widgetLabel="Calendario"
        ></ToolbarWidget>
        <!--ToolbarWidget to-do-->
        <ToolbarWidget
          imgIcon="https://img.icons8.com/dusk/55/null/checklist.png"
          widgetLabel="To do"
        ></ToolbarWidget>
        <!--ToolbarWidget musica-->
        <ToolbarWidget
          imgIcon="https://img.icons8.com/dusk/55/null/google-play-music.png"
          widgetLabel="Música"
        ></ToolbarWidget>
      </div>
    </div>
  </span>
</template>

<script>
import ToolbarWidget from "./ToolbarWidget.vue";
export default {
  name: "DynamicElement",
  components: { ToolbarWidget },
};
</script>

<style scoped>
* {
  position: fixed;
  height: auto;
  width: auto;
  left: 25px;
  transition: all 0.3s ease-out;
  z-index: 101;
  background: #fcfcfc;
  border-radius: 10px;
  width: 55px;
}

.toolbar {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  height: auto;
  top: 5vh;
  margin-top: 15vh;
  z-index: 5000;
  font-size: 10px;
}
.toolbar-flex {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0 12px;
  margin-top: 10px;
}
</style>
