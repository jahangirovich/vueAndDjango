<template>
  <div class="all">
    <v-navigation-drawer
      v-model="drawer"
      absolute
      dark
      temporary
      class="navigation"
      v-bind:style="{backgroundImage:back}"
    >
       <div class="btns">
         <router-link to="/own">
           <v-btn class="btn">
             <i class="fa fa-paint-brush" aria-hidden="true"></i>
             Own Post
           </v-btn>
         </router-link>
         <router-link to="/list">
           <v-btn class="btn">
             <i class="fa fa-bars"></i>
             Posts
           </v-btn>
         </router-link>
         <router-link to="/profile">
           <v-btn class="btn">
             <i class="fa fa-user" aria-hidden="true"></i>
             Profile
           </v-btn>
         </router-link>
         <router-link to="/hei">
           <v-btn class="btn">
             <i class="fa fa-users" aria-hidden="true"></i>
             Users
           </v-btn>
         </router-link>
       </div>
    </v-navigation-drawer>
      <div class="navbar" v-bind:style="{backgroundColor:color}">
        <div class="direct">
          <div class="leftside">
            <v-toolbar-side-icon class="side" @click.stop="drawer = !drawer">
            </v-toolbar-side-icon>
           </div>
        </div>
        <div class="direct2">
          <span>{{ user }}</span>
          <i class="fa fa-power-off" @click="clear"></i>

        </div>
      </div>
  </div>
</template>

<script>
    import axios from 'axios'
    import navbar from './navbar'
    export default {
        name: "navbar",
        props:['color','back'],
        data(){
          return{
            show:true,
            styles:{
              width:"15%",
            },
            animation:{
              animation:'animate 1s all'
            },
            drawer:null,
            user:localStorage.getItem('username'),
          }
        },
        methods:{
          disappear(){
            if(this.styles.width == "15%"){
              this.styles.width = "0"
            }
            else{
              this.styles.width = "15%"
            }
          },
          clear(){
            localStorage.clear('authToken');
            localStorage.removeItem('username');
            this.$router.push('/login')
          },

        }
    }
</script>

<style scoped>
  .navbar{
    color:white;
    display: flex;
  }
  a{
    text-decoration: none;
  }
  .menu{
    width: 100%;
    margin: 5px auto;
    background-color: white;
    box-shadow: none;
    color:#3b4149;
  }
  .btn .fa {
    position: absolute;
    left: 0;
  }
  .menu .fa {
    position: absolute;
    left: 0;
  }
  .btns{
    margin: 60px 0px;
  }
  .job{
    font-size: 20px;
    cursor: pointer;
  }
  @keyframes animate {
    from{
      transform: rotate(180deg);
    }
    to{
      transform: rotate(0deg);
    }
  }
  .direct2 .fa-power-off{
    font-size: 20px;
    padding: 0px 10px;
    cursor: pointer;
  }
  .logout{
    cursor: pointer;
    font-weight: bold;
  }
  .btn{
    width: 100%;
    margin: 0 auto;
    background-color: white;
    box-shadow: none;
    color:#3b4149;
  }
  .theme--dark .v-btn:not(.v-btn--icon):not(.v-btn--flat){
    background-color: rgba(249,249,249,0.1);
    color:white
  }
  .direct{
    text-align: left;
  }
  .btn .fa-plus{
    position: absolute;
    left:0;
  }
  .navbar div{
    width: 50%;
  }
  .navigation{
    background-size: cover;
    align-items: center;
    justify-content: center;
    background-position: center;
    display: flex;
  }
  .direct2{
    font-family: 'Quicksand',sans-serif;
    padding: 15px;
    text-align: right;
    box-sizing: border-box;
  }
  .direct2 span{
    padding: 10px;
  }
</style>
