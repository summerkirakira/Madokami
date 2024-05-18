import { type GlobalThemeOverrides } from "naive-ui";


const pinkTheme: GlobalThemeOverrides = {
    common: {
        primaryColor: "#ff80aa",
    },
    Input: {
        borderHover: "1px solid #ff80aa",
        borderFocus: "1px solid #ff80aa",
    },
    Switch: {
        railColorActive: "#ff80aa",
    },
    Button: {
        colorHoverPrimary: "#ff99bb",
        borderHoverPrimary: "1px solid #ff80aa",
        borderFocusPrimary: "1px solid #ff80aa",
        colorFocusPrimary: "#ff99bb",
        colorPressedPrimary: "#ff6699",

    }
}

export default pinkTheme;