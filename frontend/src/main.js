import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "./assets/reset.css";

const app = createApp(App);

import gAuthPlugin from "vue3-google-oauth2";
let gauthClientId =
  "906399975591-9lqdq3i69o5ils573denr6t0ng1qmk7r.apps.googleusercontent.com";

app.use(router);
app.use(gAuthPlugin, {
  clientId: gauthClientId,
  scope: "email",
  prompt: "consent",
  fetch_basic_profile: false,
});

app.mount("#app");
