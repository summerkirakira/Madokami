import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import { useUserStore } from "@/stores/user";
import pinia from "../stores"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginPage.vue"),
    },
    {
      path: "/",
      name: "home",
      component: HomeView,
    }
  ],
});

const userStore = useUserStore(pinia);

router.beforeEach((to, from, next) => {
  if (to.name !== "login" && !userStore.isLogin) {
    next({ name: "login" });
  } else {
    next();
  }
});

export default router;
