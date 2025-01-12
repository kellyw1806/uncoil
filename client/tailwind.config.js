/** @type {import("tailwindcss").Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        "merriweather": ["Merriweather", "serif"],
        "outfit": ["Outfit", "sans-serif"],
      },
      colors: {
        "primary": "#34d19e",
        "secondary": "#a58bfa"
      }
    },
  },
  plugins: [],
}

