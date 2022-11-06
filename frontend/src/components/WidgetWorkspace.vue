<template>
  <span id="widgetWorkspace">
    <div id="widgetCanvas" class="workspace">
      <!-- Aqui va dynamic element, todo,reloj,etc como elementos--->
      <DynamicElement></DynamicElement>
      <!--Widget Timer-->
      <WidgetUndefined widget="Timer"></WidgetUndefined>
    </div>
  </span>
</template>

<script>
import DynamicElement from "./DynamicElement.vue";
import WidgetUndefined from "./WidgetUndefined.vue";
export default {
  name: "ToolbarWidget",
  components: { DynamicElement, WidgetUndefined },
};
</script>

<style scoped>
#widgetWorkspace {
  z-index: 100;
}

span {
  user-select: text;
}

#widgetCanvas {
  z-index: 100;
}

.workspace {
  background: transparent;
}

div {
  display: block;
}
</style>
