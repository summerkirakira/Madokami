import { type GlobalThemeOverrides } from "naive-ui";


const blueTheme: GlobalThemeOverrides = {
    common: {
        primaryColor: "#4dd2ff"
    },
    Input: {
        borderHover: "1px solid #4dd2ff",
        borderFocus: "1px solid #4dd2ff",
    },
    Switch: {
        railColorActive: "#4dd2ff",
    }
}

export default blueTheme;