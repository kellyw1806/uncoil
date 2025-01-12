/** @type {import("tailwindcss").Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        "lusitana": ["Lusitana", "serif"],
        "cedarville": ["CedarvilleCursive", "cursive"],
      },
      colors: {
        "beige": "#f0ddb8",
        "latte": "#c78b49",
        "wood": "#e6ab5c",
        "ocean": "#1d4257",
      }
    },
  },
  plugins: [],
}

