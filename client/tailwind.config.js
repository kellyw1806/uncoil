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
        "inknut": ["InknutAntiqua"],
      },
      colors: {
        "beige": "#f0ddb8",
        "latte": "#c78b49",
        "wood": "#e6ab5c",
        "ocean": "#1d4257",
        "sawdust": "#dfbc9c",
        "oak": "#aa733c",
        "spruce": "#96673a",
        "pinenut": "#86938e",
        "darkoak": "#44443C",
      }
    },
  },
  plugins: [],
}

