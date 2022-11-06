<template>
  <div class="condicional" v-if="widgetTimer">
    <div class="widget-header light">
      <div class="widget-header-content">
        <div class="cabecera">
          <span class="titulo"> {{ widget }}</span>
        </div>
      </div>
      <span class="close-widget-button">
        <div class="lifeat-button action light">
          <button type="button">
            <span class="visual"
              ><img
                src="https://img.icons8.com/fluency-systems-regular/48/null/cancel.png"
            /></span>
          </button>
        </div>
      </span>
    </div>
    <div class="widget-content">
      <WidgetTimer></WidgetTimer>
    </div>
  </div>
</template>

<script>
import WidgetTimer from "./WidgetTimer.vue";
export default {
  name: "WidgetUndefined",
  data() {
    return {
      widgetTimer: false,
      widgetForo: false,
      widgetCalender: false,
      widgetToDo: false,
      widgetMusic: false,
    };
  },
  props: ["widget"],
  components: { WidgetTimer },
  created() {
    switch (this.widget) {
      case "Timer":
        this.widgetTimer = true;
        break;
      case "Foro":
        this.widgetForo = true;
        break;
      case "Calender":
        this.widgetCalender = true;
        break;
      case "ToDo":
        this.widgetToDo = true;
        break;
      case "Music":
        this.widgetMusic = true;
        break;
      default:
        break;
    }
  },
};
</script>

<style scoped>
* {
  display: flex;
  z-index: 102;
  left: 340px;
  top: 146.75px;
  width: 360px;
  height: auto;
  min-width: 360px;
  min-height: 150px;
  max-height: 960px;
  max-width: 974px;
  position: fixed;
  border-radius: 7px;
  box-shadow: 0 0 4px rgb(131 131 131 / 25%);
  flex-direction: column;
  justify-content: flex-start;
  align-items: stretch;
  overflow: hidden;
  margin: 0;
  box-sizing: border-box;
  user-select: text;

  display: flex;
  z-index: 104;
  left: 436px;
  top: 196.75px;
  width: 360px;
  height: auto;
  min-width: 360px;
  min-height: 150px;
  max-height: 961px;
  max-width: 975px;
}

.widget-header.light {
  color: #4e4e4e;
}

.widget-header {
  flex-grow: 0;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #dfdfdf;
  margin: 0;
  box-sizing: border-box;
}

.widget-header-content {
  font-size: 16px;
  margin: 8px 22px;
  height: auto;
  width: auto;
}

.cabecera {
  display: flex;
  flex-direction: row;
  -webkit-box-pack: start;
  justify-content: flex-start;
  -webkit-box-align: center;
  align-items: center;
}

.close-widget-button {
  position: relative;
  float: right;
  cursor: pointer;
  margin: 0;
  box-sizing: border-box;
}

.lifeat-button {
  min-height: unset;
}

.lifeat-button.light {
  color: #4e4e4e;
  background: #fcfcfc;
  border-color: #e9e9e9;
}

.lifeat-button {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  height: auto;
  max-height: 36px;
  width: inherit;
  padding: 6px 10px;
  border-radius: 7px;
}

.lifeat-button button {
  border: 0;
  padding: 0 5px;
  font-size: 16px;
  font-family: "CircularStd";
}

button {
  user-select: text;
  appearance: auto;
  writing-mode: horizontal-tb !important;
  text-rendering: auto;
  letter-spacing: normal;
  word-spacing: normal;
  line-height: normal;
  text-transform: none;
  text-indent: 0px;
  text-shadow: none;
  display: inline-block;
  text-align: center;
  align-items: flex-start;
}

.widget-content {
  flex-grow: 100;
  overflow-y: scroll;
  height: fit-content;
  font-family: "CircularStd";
  font-size: 16px;
  display: flex;
  flex-direction: column;
}
</style>
