import { defineUserConfig } from "vuepress";
import theme from "./theme.js";

export default defineUserConfig({
  base: "/madokami/",

  lang: "zh-CN",
  title: "Madokami用户指南",
  description: "五分钟上手Madokami",

  theme,

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
