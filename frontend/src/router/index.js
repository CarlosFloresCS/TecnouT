import { createRouter, createWebHistory } from "vue-router";
//import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/sign_in",
      name: "sig_in",
      component: () => import("../views/SignInView.vue"),
    },
    {
      path: "/sign_up",
      name: "sig_up",
      component: () => import("../views/SignUpView.vue"),
    },
    {
      path: "/inicio",
      name: "inicio",
      component: () => import("../components/InicioVentana.vue"),
    },
  ],
});

export default router;
