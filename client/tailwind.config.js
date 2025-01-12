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
        "lusitana-bold": ["Lusitana Bold", "serif"],
        "cedarville": ["CedarvilleCursive", "cursive"],
        "inknut": ["InknutAntiqua"],
      },
      colors: {
        "snow": "#d9d9d9",
        "beige": "#DADAC2",
        "sawdust": "#dfbc9c",
        "pinenut": "#86938e",
        "pinenut70": "#86938eb4",
        "darkoak": "#44443C",
      }
    },
  },
  plugins: [],
}

