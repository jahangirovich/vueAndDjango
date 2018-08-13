<template>
  <div class="main">
    <nav-bar v-bind:color="color.backgroundColor" v-bind:back="back.backgroundImage"></nav-bar>
    <div class="what">
      <div class="loader" v-if="load">
      </div>
      <div v-for="profile in profiles">
        <router-link v-bind:to="{name:'call',params:{username:profile.username}}">
          <div class="into">
            <div class="image" :style="{ backgroundImage: `url('${profile.image}')` }">

            </div>
            <div class="text">
              <span>{{ profile.username }}</span>
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
    import axios from 'axios'
    import navbar from './navbar'
    export default {
        name: "users",
        components:{
          'nav-bar':navbar
        },
        data(){
          return{
            profiles:[],
            style:{
              backgroundImage:`url()`
            },
            load:true,
            color:{
              backgroundColor:'#726d54'
            },
            back:{
              backgroundImage:'url(https://images.unsplash.com/photo-1532976799258-5848600ec8f1?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=7f5720dc13466c17724a53402f0eab26&auto=format&fit=crop&w=2000&q=80)'
            },
          }
        },
        created(){
          axios.get(`http://localhost:8000/router/profiles/`)
            .then(
              response =>{
                this.profiles = response.data;
                this.load = false
              }
            )
            .catch(
              err =>{
                console.log(err)
              }
            )
        },
        methods:{

        }
    }
</script>

<style scoped>
  .what{
    width: 30%;
    background-color: white;
    padding: 0px;
    margin: 0 auto;
    position: relative;
  }
  a{
    text-decoration: none;
  }
  .into{
    display: flex;
    padding: 10px;
    cursor: pointer;
    transition: 0.3s all;
  }
  .into:hover{
    box-shadow: 0 0 5px rgba(0,0,0,0.5);
  }
  .loader{
    position: absolute;
    left:50%;
    top:50%;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    z-index: 2;
    border:5px solid white;
    border-top-color:#3b4149;
    animation: rotate 1s infinite;
  }
  @keyframes rotate {
    from{
      transform: rotate(360deg);
    }
    to{
      transform: rotate(0deg);
    }
  }
  .image{
    width: 60px;
    height: 60px;
    background-position: center;
    background-size: cover;
    border-radius: 50%;
  }
  .text{
    position: relative;
    padding: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 17px;
    color:#3b4149;
    font-family: 'Raleway',sans-serif;
    width: 70%;
  }
</style>
