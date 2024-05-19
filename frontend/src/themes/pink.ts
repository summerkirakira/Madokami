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

        borderHover: "1px solid #ff80aa",
        borderFocus: "1px solid #ff80aa",
        textColorHover: "#ff99bb",
        textColorFocus: "#ff99bb",
    },
    Menu: {
        itemTextColorHorizontal: "#ff80aa",
        itemTextColorHoverHorizontal: "#ff99bb",
        itemIconColorHoverHorizontal: "#ff99bb",
    }
}

export default pinkTheme;