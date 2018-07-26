import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import list from '@/components/list'
Vue.use(Router)

let router =  new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld,
      meta:{
        requiresGuest:true
      }
    },
    {
      path:'/list',
      name:'list',
      component:list,
      meta:{
        requiresAuth:true
      }
    }
  ]
})

router.beforeEach((to,from,next) => {
  if(to.matched.some(record => record.meta.requiresAuth)){
    if(localStorage.getItem("authToken") == null || localStorage.getItem("authToken") == undefined){
      next({
        path:'/',
        query:{
          redirect:to.fullPath
        }
      })
    }
    else{
      next()
    }
  }
  else if(to.matched.some(record => record.meta.requiresGuest)){
    if(localStorage.getItem("authToken") != null || localStorage.getItem("authToken") != undefined){
      next({
        path:'/list',
        query:{
          redirect:to.fullPath
        }
      })
    }
    else{
      next()
    }
  }
  else{
    next();
  }
});
export default router;
