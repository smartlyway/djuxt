module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'starter',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', content: 'djuxt' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: 'favicon.ico' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons', type: 'text/css' }
    ]
  },
  css: [
    '~/static/css/vuetify.min.css'
  ],
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#3B8070' },
  build: {
    /*
    ** Run ESLINT on save
    */
    extend (config, ctx) {
      if (ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    },
    filenames: {
      manifest: 'manifest.[hash].js',
      vendor: 'vendor.bundle.[hash].js',
      app: 'djuxt.bundle.[chunkhash].js'
    },
    publicPath: '/static/',
    vendor: [
      'vue-i18n',
      'axios'
    ]
  },
  plugins: [
    '~plugins/vuetify',
    '~plugins/axios',
    '~/plugins/i18n.js'
  ]
}
