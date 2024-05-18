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
    },
    Button: {
        colorHoverPrimary: "#66d8ff",
        borderHoverPrimary: "1px solid #4dd2ff",
        borderFocusPrimary: "1px solid #4dd2ff",
        colorFocusPrimary: "#00abe6",
        colorPressedPrimary: "#00abe6",
    }
}

export default blueTheme;