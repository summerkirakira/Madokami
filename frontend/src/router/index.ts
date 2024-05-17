import { createRouter, createWebHistory } from "vue-router";
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
      meta: {
        title: "登录",
      },
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
          meta: {
            title: "我的订阅",
          },
        },
        {
          name: "media",
          path: 'media',
          component: () => import("../views/MediaView.vue"),
          meta: {
            title: "媒体库",
          },
        },
        {
          name: "settings",
          path: "settings",
          component: () => import("../views/SettingsView.vue"),
          meta: {
            title: "设置",
          },
        },
        {
          name: "logs",
          path: "logs",
          component: () => import("../views/LogView.vue"),
          meta: {
            title: "日志",
          },
        }
      ]
    }
  ],
});

const userStore = useUserStore(pinia);

router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title} - Madokami`;
  if (to.path === "/") {
    next({ name: "media" });
    return;
  }
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
