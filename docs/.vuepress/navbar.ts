import { navbar } from "vuepress-theme-hope";

export default navbar([
  // "/",
  // "/portfolio",
  "/startup/",
  "/plugin_guide/",
  // {
  //   text: "插件",
  //   icon: "lightbulb",
  //   prefix: "/guide/",
  //   children: [
  //     {
  //       text: "蜜柑计划订阅",
  //       icon: "lightbulb",
  //       prefix: "/plugin_guide",
  //       children: [],
  //     },
  //     {
  //       text: "B站视频订阅",
  //       icon: "lightbulb",
  //       prefix: "foo/",
  //       children: [],
  //     },
  //   ],
  // },
  {
    text: "开发文档",
    icon: "book",
    link: "https://github.com/summerkirakira/Madokami",
  },
]);
