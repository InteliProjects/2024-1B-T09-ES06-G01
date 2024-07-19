// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  css: [
    '~/assets/css/variables.scss',
    '~/assets/css/global.scss',
  ],

  modules: ['nuxt-swiper'],

  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL || 'http://localhost:80',
    }
  },
})