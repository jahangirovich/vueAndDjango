<template>
  <div class="cover">
    <div class="hello">
    <div class="center">
      <h3>
        Login
      </h3>
      <form @submit.prevent="putIt">
        <p>
          <input type="text" id="hi" v-model="username" required >
          <label for="hi">Username</label>
          <span class="span"></span>
        </p>
        <p>
          <input type="password" v-model="password" required id="pass">
          <label for="pass">Password</label>
          <span class="span"></span>
        </p>
        <v-btn small color="#2f3844" type="submit">SignIn</v-btn>
        <p class="sign"><router-link to="/">SignUp?</router-link></p>
        <ul>
        <li v-for="error in errors">
          <span v-for="err in error.data">
            <span v-for="er in err">
              {{ er }}
            </span>
          </span>
        </li>
      </ul>
      </form>
    </div>
    <br>
  </div>
  </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "Login",
        data(){
          return{
            username:'',
            password:'',
            errors:'',
            hi:[]
          }
        },
        created(){
          axios.get(`http://localhost:8000/router/tokens/`)
          .then(
            response =>{
              this.hi = response.data
              this.list()
            }
          )
          .catch(
            error =>{
              console.log(error.message)
            }
          );
        },
        methods:{
          putIt(){
        axios.post(`http://localhost:8000/auth/token/create/`,{
              username:this.username,
              password:this.password,
            })
              .then(
                response =>{
                  sessionStorage.setItem('authToken', response.data.token)
                  sessionStorage.setItem('username', this.username)
                  localStorage.setItem('authToken',response.data.auth_token)
                  localStorage.setItem('username',this.username)
                  this.$router.push('/list');
                  this.list()
                }
              )
              .catch(
                e =>{
                  this.errors = e
                }
              )
          },
          list(){
              for (var x = 0;x < this.hi.length;x++){
                  if(this.hi[x].key == localStorage.getItem('authToken')){
                    this.number = this.hi[x].user;
                  }
              }
            }
        }
    }
</script>

<style scoped>
  input{
    color:#2f3844;
    outline: none;
    width: 100%;
    padding: 10px;
    font-family: 'Quicksand',sans-serif;
    font-size: 15px;
  }
  .cover{
    position: fixed;
    width: 100%;
    height: 100%;
    left:0;
    top:0;
    background-color: white;
  }
  a{
    text-decoration: none;
    color:#2f3844;
  }
  .center{
    padding: 10px;
    transition: 0.3s all;
    animation: animate 0.6s;
    background-color: white;
    width: 30%;
  }
  ul li{
    list-style-type: none;
    color: #82183a;
    margin: 0 auto;
    font-family: 'Quicksand',sans-serif;
  }
  ul{
    margin: 0 auto;
  }
  @keyframes animate {
    0%{
      transform: scale(0.5);
    }
    50%{
      transform: scale(1);
    }
    100%{
      transform: scale(1);
    }
  }
  .sign{
    font-family: 'Quicksand',sans-serif;
    padding: 10px;
    box-sizing: border-box;
    cursor: pointer;
  }
  h3{
    font-family: 'Quicksand',sans-serif;
    color:#2f3844;
    font-size: 23px;
    padding: 10px;
    font-weight: normal;
    transition: 0.6s all;
    position: relative;
    overflow: hidden;
  }

  h3 span:hover{
    background-color: #2f3844;
    color:white;
  }
  h3:hover{
     box-shadow: 0 0 5px rgba(0,0,0,0.5);
  }
  .hello{
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    width: 100%;
    height: 100%;
  }
  form{
    margin: 40px;

  }
  p{
    position: relative;
  }
  p label{
    font-size: 14px;
    position: absolute;
    left:10px;
    top:10px;
    font-family: 'Quicksand',sans-serif;
    transition: 0.4s all;
  }
  button{
    font-family: 'Quicksand',sans-serif;
  }
  .span{
    width: 100%;
    border-bottom: 1px solid #2f3844;
    position: absolute;
    left:0px;
  }
  .span::after{
    border-bottom: 1px solid #5a7896;
    position: absolute;
    left:0px;
    transition: 0.2s all;
    width: 0%;
    content: "";
  }
  input:focus ~ label{
    top:-5px;
    font-size: 10px;
    color:#5a7896;
  }
  input:valid ~ label{
    top:-5px;
    font-size: 10px;
    color:#5a7896;
  }
  input:focus ~ span{
    border:none;
  }
  input:focus ~ span::after{
    width: 100%;
  }
  input:focus{
    border:none;
  }
  input:valid ~ span{
    border:none;
  }
  input:valid ~ span::after{
    width: 100%;
  }
  input:valid{
    border:none;
  }
</style>
