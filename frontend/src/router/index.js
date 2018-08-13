import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import list from '@/components/list'
import login from '@/components/Login'
import own from '@/components/own'
import profile from '@/components/profile'
import detail from '@/components/detail'
import user from '@/components/users'
import call from '@/components/call'

Vue.use(Router);

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
    },
    {
      path:'/login',
      name:'login',
      component:login,
      meta:{
        requiresGuest:true
      }
    },
    {
      path:'/own',
      name:'own',
      component:own,
      meta:{
        requiresAuth:true
      }
    },
    {
      path:'/profile',
      name:'profile',
      component:profile,
      meta:{
        requiresAuth:true
      }
    },
    {
      path:'/hei',
      name:'users',
      component:user,
      meta:{
        requiresAuth:true
      }
    },
    {
      path:'/:username',
      name:'call',
      component:call,
      meta:{
        requiresAuth:true
      }
    },
    {
      path:'/:id',
      name:'detail',
      component:detail,
      meta:{
        requiresAuth:true
      }
    },
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
