import { defineStore } from "pinia";
import { type GlobalThemeOverrides } from "naive-ui";
import pinkTheme from "@/themes/pink";
import blueTheme from "@/themes/blue";
import greenTheme from "@/themes/green";


interface ThemeState {
  dark: boolean;
  theme: GlobalThemeOverrides;
  themeName: string;
}

function getTheme(key: string) {
    if (key === "pink") {
        return pinkTheme;
    } else if (key === "blue") {
        return blueTheme;
    } else if (key === "green") {
        return greenTheme;
    } else {
        return pinkTheme;
    }
}

function loadThemeFromLocalStorage(): ThemeState {
    let themeName = localStorage.getItem("theme");
    let isDark = localStorage.getItem("theme-dark");
    let theme = {
        dark: false,
        theme: pinkTheme,
        themeName: "pink",
      };
    if (isDark) {
        theme.dark = isDark === "true";
    }
    if (themeName) {
        theme.themeName = themeName;
        theme.theme = getTheme(themeName);
    }
    return theme;
    }
    

export const useThemeStore = defineStore("theme", {
  state: (): ThemeState => {
    return loadThemeFromLocalStorage();
  },
  actions: {
    setDark(dark: boolean) {
        this.dark = dark;
        localStorage.setItem("theme-dark", dark.toString());
    },
    setTheme(themeName: string) {
        this.themeName = themeName;
        this.theme = getTheme(themeName);
        localStorage.setItem("theme", themeName);
    }
  }
});