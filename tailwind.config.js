/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/templates/**/*.{html,js}"],
  theme: {
    extend: {
      transitionProperty: {
        'DEFAULT': 'backgroundColor, borderColor, color, fill, stroke, opacity, boxShadow, transform',
        'opacity': 'opacity',
        'color': 'backgroundColor, borderColor, color, fill, stroke'
      },
      fontFamily: {
        'mono': ['Courier New', 'monospace']
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

