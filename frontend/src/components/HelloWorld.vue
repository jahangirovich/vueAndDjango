<template>
  <div class="hello">
    <p>Register</p>
    <form @submit.prevent="signUp">
      <input type="text" v-model="username" required>
      <input type="email" v-model="email" required>
      <input type="password" v-model="password" required>
      <button type="submit">Add</button>
    </form>
    <p>Login</p>
    <form @submit.prevent="putIt">
      <input type="text" v-model="username" required>
      <input type="password" v-model="password" required>
      <button type="submit">Login</button>
    </form>
    <ul>

    </ul>
    <button @click="clear">Clear</button>
    <textarea v-model="text" id="" cols="30" rows="10"></textarea>
    <span @click="postIt">Add</span>
    {{ hi }}
    <br>
    {{ number }}
  </div>
</template>

<script>
  import axios from 'axios'
  const $ = window.jQuery
export default {
  name: 'HelloWorld',
  data () {
    return {
      username:'',
      email:'',
      password:'',
      my:[],
      text:'',
      user:localStorage.getItem('username'),
      hi:[],
      no:[],
      number:'',
      errors:''
    }
  },
  created(){
    this.my = sessionStorage
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

      signUp () {
        axios.post('http://localhost:8000/auth/users/create/', this.$data, (data) => {
          alert('Your account has been created. You will be signed in automatically')
          this.list()
        })
        .catch((response) => {
          alert(response.responseText)
        })
      },
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
              this.$router.push('/list')
              this.list()
            }
          )
          .catch(
            e =>{
              this.errors = e
            }
          )
      },
      clear(){
        localStorage.removeItem('authToken',this.my.authToken)
        localStorage.removeItem('username',this.my.username)
      },
      postIt(){
        axios.post(`http://localhost:8000/router/text/`,{
          text:this.text,
          user:1
        })
          .then(
            response =>{
              console.log(response.data)
            }
          )
          .catch(
            error =>{
              console.log(error)
            }
          )
      },
      list(){
        var me = this.hi
        for (var x = 0;x < this.hi.length;x++){
            if(this.hi[x].key == localStorage.getItem('authToken')){
              this.number = this.hi[x].user;
            }
        }
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
