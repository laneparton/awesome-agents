/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        midnightBlue: '#1c2836',
        navyBlue: '#212f40',
        slateBlue: '#2f435b',
        lightBlue: '#9bacc4',
        lightOrange: '#f7961c',
        darkerOrange: '#ef8908',
        faintBlue: '#2a3c51',
      },
    },
  },
  plugins: [],
}
