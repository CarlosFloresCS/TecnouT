<template>
  <span class="widget-icon">
    <img :src="imgIcon" />
  </span>
  <span class="widget-label">{{ widgetLabel }}</span>
</template>

<script>
export default {
  name: "ToolbarWIdget",
  props: ["imgIcon", "widgetLabel"],
};
</script>

<style scoped>
* {
  margin-bottom: 11px;
  border-radius: 7px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  cursor: pointer;
  border: none;
  font-size: 10px;
  box-sizing: border-box;
}
.widget-icon {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;
  user-select: text;
  pointer-events: none;
  stroke-width: 2;
}

.widget-label {
  user-select: text;
  margin-top: -10px;
}
</style>
