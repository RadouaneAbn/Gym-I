/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/**/*.{html,js}"],
  variants: {
    extend : {
      display: ['group-focus']
    },
  },
  theme: {
    extend: {
      animation: {
        blob: "blob 7s infinite"
      },
    keyframes: {
      blob: {
        "0%": {
          transform: "translate(0px, 0px) scale(1)",
        },
        "33%": {
          transform: "translate(20px, -20px) scale(1.1)",
        },
        "66%": {
          transform: "translate(-10px, 10px) scale(0.9)",
        },
        "100%": {
          transform: "translate(0px, 0px) scale(1)",
        },
      },
    }
    },
  },
  plugins: [],
}

