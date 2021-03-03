const colors = require("tailwindcss/colors");

module.exports = {
  purge: {
    // enabled: false,
    content: ["src/**/*.{html,vue,js}", "src/*.{html,vue,js}"]
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    colors: {
      black: colors.black,
      white: colors.white,
      gray: colors.trueGray,
      orange: {
        50: "#fff6e5",
        100: "#ffedcc",
        200: "#ffdb99",
        300: "#ffc966",
        400: "#ffb733",
        500: "#ffa500",
        600: "#cc8400",
        700: "#996300",
        800: "#664200",
        900: "#664200"
      },
      boxShadow: {
        "sm": "box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)",
        "DEFAULT": "box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)",
        "md": "box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23)",
        "lg": "box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22)",
        "xl": "box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22)",
      },
      elevation: {
        0: "rgba(255, 255, 255, 0)",
        1: "rgba(255, 255, 255, 0.05)",
        2: "rgba(255, 255, 255, 0.07)",
        3: "rgba(255, 255, 255, 0.08)",
        4: "rgba(255, 255, 255, 0.09)",
        6: "rgba(255, 255, 255, 0.11)",
        8: "rgba(255, 255, 255, 0.12)",
        16: "rgba(255, 255, 255, 0.14)",
        24: "rgba(255, 255, 255, 0.16)"
      },
      red: {
        200: "#ffa290"
      },
      blue: {
        200: "#6fcdff"
      },
      green: {
        200: "#cdff7c"
      }
    },
    screens: {
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1280px"
      // '2xl': '1536px',
    },
    minWidth: {
      '60': '20rem',
      '64': '21rem',
    },
    columnWidth: {
      sm: "120px",
      md: "240px",
      lg: "360px",
      xl: "480px"
    },
    extend: {
      colors: {
        gray: {
          950: "#121212"
        }
      },
      fontFamily: {
        sans: ["Gilroy"]
      },
    }
  },
  variants: {
    extend: {
      backgroundColor: ["odd"],
      zIndex: ["hover"]
    }
  },
  plugins: [require("tailwindcss-multi-column")()]
};
