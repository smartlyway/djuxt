'use strict'

import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)


const _8e22e5b2 = () => import('/home/docker/code/app/pages/index.vue' /* webpackChunkName: "pages/index" */)

const _6e7ddf7e = () => import('/home/docker/code/app/pages/login/index.vue' /* webpackChunkName: "pages/login" */)



const scrollBehavior = (to, from, savedPosition) => {
  // savedPosition is only available for popstate navigations.
  if (savedPosition) {
    return savedPosition
  } else {
    let position = {}
    // if no children detected
    if (to.matched.length < 2) {
      // scroll to the top of the page
      position = { x: 0, y: 0 }
    }
    else if (to.matched.some((r) => r.components.default.options.scrollToTop)) {
      // if one of the children has scrollToTop option set to true
      position = { x: 0, y: 0 }
    }
    // if link has anchor,  scroll to anchor by returning the selector
    if (to.hash) {
      position = { selector: to.hash }
    }
    return position
  }
}


export function createRouter () {
  return new Router({
    mode: 'history',
    base: '/',
    linkActiveClass: 'nuxt-link-active',
    linkExactActiveClass: 'nuxt-link-exact-active',
    scrollBehavior,
    routes: [
  		{
			path: "/",
			component: _8e22e5b2,
			name: "index"
		},
		{
			path: "/login",
			component: _6e7ddf7e,
			name: "login"
		}
    ]
  })
}
