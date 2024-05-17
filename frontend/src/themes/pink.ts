import { type GlobalThemeOverrides } from "naive-ui";


const pinkTheme: GlobalThemeOverrides = {
    common: {
        primaryColor: "#ff80aa"
    },
    Input: {
        borderHover: "1px solid #ff80aa",
        borderFocus: "1px solid #ff80aa",
    },
    Switch: {
        railColorActive: "#ff80aa",
    }
}

export default pinkTheme;