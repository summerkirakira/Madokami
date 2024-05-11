import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import { useUserStore } from "@/stores/user";
import MainView from "@/views/MainView.vue";



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
    },
    {
      path: "/library",
      name: "library",
      component: MainView,
      children: [
        {
          name: "subscriptions",
          path: "subscriptions",
          component: () => import("../views/SubscriptionView.vue"),
        },
        {
          name: "media",
          path: 'media',
          component: () => import("../views/MediaView.vue")
        }
      ]
    }
  ],
});

const userStore = useUserStore(pinia);

router.beforeEach((to, from, next) => {
  if (to.name !== "login" && !userStore.isLogin) {
    next({ name: "login" });
  } else {
    if (to.name === "home") {
      next({ name: "media" });
    } else {
      next();
    }
  }
});

export default router;
