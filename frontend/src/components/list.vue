<template>
    <div>
      <p>My name is joha</p>
      <button @click="clear">Logout</button>
      <ul>

      </ul>
      {{ number }}
      <ul>
        <li v-for="(reality,index) in real">
          <span>{{ reality.text }}</span>
          <span>{{ reality.user }}</span>
          <span @click="deletePost(reality.id,index)" style="color:red">delete</span>
        </li>
      </ul>
      <form action="" @submit.prevent="addPost">
        <input type="text" v-model="text">
        <button type="submit">Add</button>
      </form>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "list",
        data(){
          return{
            hi:[],
            number:'',
            sheet:[],
            real:[],
            text:'',
            user:null
          }
        },
        created(){
          axios.get(`http://localhost:8000/router/tokens/`)
            .then(
              response =>{
                this.hi = response.data
                this.define()
                this.getInf()
              }
            )
            .catch(
              error =>{
                console.log(error.message)
              }
            );
        },
        methods:{
          clear(){
            localStorage.clear('authToken');
            localStorage.removeItem('username');
            this.$router.push('/')
          },
          define(){
            for (var x = 0;x < this.hi.length;x++){
              if(this.hi[x].key == localStorage.getItem('authToken')){
                this.number = this.hi[x].user;
              }
             }
          },
          addPost(){
            axios.post(`http://localhost:8000/router/list/`,{
              text:this.text,
              user:this.number
            })
              .then(
                response =>{
                  this.real.push(response.data)
                }
              )
              .catch(
                err =>{
                  console.log(err)
                }
              )
          },
          deletePost(id,index){
            axios.delete(`http://localhost:8000/router/list/${id}/`)
              .then(
                response =>{
                  this.real.splice(index,1)
                }
              )
              .catch(
                err =>{
                  console.log(err)
                }
              )
          },
          getInf(){
            axios.get(`http://localhost:8000/router/list/`)
            .then(
              response =>{
                for (var x = 0; x < response.data.length;x++){
                  if(this.number == response.data[x].user){
                    this.sheet.push(response.data[x])
                  }
                }
                this.real = this.sheet
              }
            )
          },

        }
    }
</script>

<style scoped>

</style>
