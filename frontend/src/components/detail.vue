<template>
  <div class="all">
    <nav-bar v-bind:back="back.backgroundImage" v-bind:color="color.backgroundColor"></nav-bar>
    <div class="profile">
        <div class="image" v-bind:style="styles">
          <div class="add">

          </div>
        </div>
        <div class="text">
          <div class  ="what">
            <p>
              <b>{{ profile.username }}</b>
            </p>
            <div class="detail">
              <p>
                <b>First Name:</b>
              {{ profile.firstName }}
              </p>
              <p>
                <b>Surname:</b>
                {{ profile.surname }}
              </p>
              <p>
                <b>Date of birth:</b>
                {{ profile.date }}
              </p>
            </div>
          </div>
        </div>
        <div class="btn" v-if="!user">
          <v-btn
          small
          v-if="!friend"
          @click="addFriends()"
          class="button1"
          >
            add Friend
          </v-btn>
          <v-btn
            small
            v-if="friend"
            @click="deleteFriend(friends.id)"
            class="button"
          >
            Delete Friend
          </v-btn>
        </div>
      </div>
  </div>
</template>

<script>
    import navbar from './navbar'
    import axios from 'axios'
    import profile from './profile'
    export default {
        name: "detail",
        components:{
          'nav-bar':navbar,
        },
        data(){
          return{
            styles:{
              backgroundImage:"",
              backgroundSize:"cover",
              backgroundPosition:"center",
            },
            profile:[],
            error:[],
            pk:null,
            friend:false,
            friends:[],
            user:false,
            back:{
              backgroundImage:'url(https://images.unsplash.com/photo-1533016680729-2752694b094e?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=ed68e0b8e428b34dff7f108a702ae95b&auto=format&fit=crop&w=2134&q=80)'
            },
            color:{
              backgroundColor:'#535b77'
            },
          }
        },
      methods:{
        addFriends(){
          axios.post(`http://localhost:8000/router/friends/`,{
            username:localStorage.getItem('username'),
            friend:this.$route.params.id
          })
            .then(
              response =>{
                this.getFriends()
              }
            )
            .catch(
              err =>{
                console.log(err)
              }
            )
        },
        getFriends(){
          axios.get(`http://localhost:8000/router/friends/`)
          .then(
            response =>{
              for (var x = 0; x < response.data.length;x++){
                if(response.data[x].friend == this.$route.params.id){
                  this.friend = true
                  this.friends = response.data[x]
                  break;
                }
                else{
                  this.friend = false;
                  this.friends = []
                }
                }
              }
            )
            .catch(
              err =>{
                console.log(err)
              }
            )
        },
        deleteFriend(id){
          axios.delete(`http://localhost:8000/router/friends/${id}/`)
            .then(
              response =>{
                this.getFriends()
                this.friend = false;
              }
            )
            .catch(
              err =>{
                console.log(err)
              }
            )
        },
      },
      created(){
          axios.get(`http://localhost:8000/router/profiles/`)
              .then(
                response =>{
                  for(var x in response.data){
                    if(this.$route.params.id == response.data[x].id){
                      this.profile = response.data[x]
                    }

                  }
                  if(this.profile == [] || this.profile == null){
                    this.styles.backgroundImage = 'url(https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=9017084ac611b76fb7506ccc54d854ac&auto=format&fit=crop&w=2089&q=80)'
                  }
                  else{
                    for(var x in this.profile){
                      if(this.profile.username == localStorage.getItem('username')){
                        this.user = true
                      }
                      else{
                        this.user = false
                      }
                      this.styles.backgroundImage = `url(${this.profile.image})`;
                      break
                    }
                  }
                  this.pk = this.$route.params.id
                }
              )
              .catch(
                err =>{
                  this.errors = err
                }
              )
        this.getFriends()
      },
    }
</script>

<style scoped>
  .profile{
    position: relative;
    width: 50%;
    margin: 0 auto;
    background-color: white;
    padding: 10px;

    overflow: hidden;
  }
  .btn{
    text-align: left;
    padding: 0px;
    width: 100%;
    clear: left;
  }
  .button{
    background-color: #99213b;
    color:white;
  }
  .btn .button1{
    background-color: #475975;
    color:white
  }
  .text{
    font-family: 'Raleway',sans-serif;
    display: inline-block;
  }
  .button1{
    background-color: #3b4149;
    color:white;
  }
  .detail{
    padding: 10px;
    text-align: left;
    width: 100%;
  }
  .detail p{
    padding: 10px;
    border-bottom:1px solid #ebeef4
  }
  .picker{
    color:black;
    background-color: rgba(0,0,0,0.1);
  }
  .v-label{
    font-size: 13px;
  }
  input{
    font-size: 13px;
  }
  ul li{
    list-style-type: none;
  }
  .add{
    position: absolute;
    width: 0%;
    height: 100%;
    background-color: rgba(0,0,0,0);
    left:0;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: 0.4s all;
    overflow: hidden;
    color:white;
    top:0;
    font-family: 'Quicksand',sans-serif;
    font-size: 11px;
    font-weight: bold;
  }
  .image{
    position: relative;
    width: 200px;
    height: 200px;
    cursor: pointer;
    display: inline-block;
    float: left;
  }
  .text{
    width: 65%;
    margin: 0 auto;
    position: relative;
    left:0;
    top:0;
  }
  p{
    margin: 0 auto;
  }
</style>
