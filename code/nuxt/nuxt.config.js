module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'starter',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', content: "Nuxt.js project" }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: 'favicon.ico' },
      { rel:'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700', type:'text/css'},
      { rel:'stylesheet', href: 'google/material-icons.css', type:'text/css'},
      { rel:'stylesheet', href: 'vuetify/vuetify.min.css', type:'text/css'}
    ]
  },
  plugins: ['~plugins/vuetify'],
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
    vendor: ['axios']
  }
}
