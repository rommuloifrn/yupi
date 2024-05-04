/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['../core/templates/core/**/*.{html, js}'],
  theme: {
    extend: {},
  },
  plugins: [
    require("@catppuccin/tailwindcss")({
      defaultFlavour: "latte",
    })
  ],
}

