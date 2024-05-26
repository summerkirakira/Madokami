import { sidebar } from "vuepress-theme-hope";

export default sidebar({
  "/": [
    // "",
    // "portfolio",
    {
      text: "快速上手",
      icon: "laptop-code",
      prefix: "startup/",
      link: "startup/",
      children: "structure",
    },
    {
      text: "扩展插件",
      icon: "palette",
      prefix: "plugin_guide/",
      link: "plugin_guide/",
      children: "structure",
    }
  ],
});
