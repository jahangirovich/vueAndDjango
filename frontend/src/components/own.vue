<template>
    <div class="all_list">
      <nav-bar></nav-bar>
      <div class="list">
        <div class="loader" v-if="loader">

        </div>
        <div class="detail">
          <p>Your own post : {{ username }}</p>
        </div>
        <div class="cycle" v-for="(list,index) in hi">
          <div class="all">
             <div class="words">
            <span class="hard">
              {{ list.title }}
            </span>
            <br>
            <br>
            <span>
              {{ list.text }}
            </span>
            </div>
            <div class="edit">
              <v-icon class="delete" @click="deleteIt(list.id,index)">delete</v-icon>
              <v-icon class="edits" @click="editIt(list.id)">edit</v-icon>
            </div>
          </div>
          <div class="addPost" v-bind:style="styles">
          <div class="into">
            <h2>Add Post</h2>
            <form @submit.prevent="saveIt(list.id)" name="myform" novalidate  enctype="multipart/form-data">
              <p>
                <v-text-field
                v-model="need.title"
                :counter="10"
                label="Title"
                required
                name="hi"
              ></v-text-field>
              </p>
              <p>
                <v-textarea
                name="input"
                label="Text*"
                v-model="need.text"
              ></v-textarea>
              </p>
              <p v-if="!myimage">
                  <input multiple type="file" required id="file" ref="myref" @change="onFileChange" >
                <label for="file">
                  Upload Image
                  <v-icon right dark>cloud_upload</v-icon>
                </label>
                </p>
                <p v-else>
                  <img :src="myimage">
                </p>
                <v-btn depressed color="" type="submit" class="btn" >Save</v-btn>
                <v-btn depressed color="error" class="btns" @click="cancel">close</v-btn>
              <ul>
                <li v-for="err in error">
                  {{ err }}
                </li>
              </ul>
              </form>
            </div>

          </div>
        </div>
      </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import navbar from './navbar'
    export default {
        name: "own",
        components:{
            'nav-bar':navbar
          },
        data(){
          return{
            loader:true,
            hi:[],
            actual:true,
            real:[],
            number:null,
            sheet :[],
            username:localStorage.getItem('username'),
            need:[],
            error:[],
            styles:{
              height:"0%"
            },
            image:'',
            myimage:''
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
          define(){
            for (var x = 0;x < this.hi.length;x++){
              if(this.hi[x].key == localStorage.getItem('authToken')){
                this.number = this.hi[x].user;
              }
             }
          },
          getInf(){
            axios.get(`http://localhost:8000/router/list/`)
            .then(
              response =>{
                for (var x = 0;x < response.data.length;x++){
                  if(this.number == response.data[x].user){
                    this.sheet.push(response.data[x])
                  }
                }
                this.hi = this.sheet
                this.loader = false
              }
            )
          },
          deleteIt(id,index){
            axios.delete(`http://localhost:8000/router/list/${id}/`)
              .then(
                response =>{
                  this.hi.splice(index,1)
                  this.loader = false
                }
              )
              .catch(
                err =>{
                  console.log(err)
                }
              )
          },
          me(){
            this.$refs.myref.click()
          },
          editIt(id){
            axios.get(`http://localhost:8000/router/list/${id}/`)
              .then(
                response =>{
                  this.need = response.data;
                  this.actual = false;
                  this.styles.height = "100%"
                }
              )
              .catch(
                err =>{
                  console.log(err)
                }
              )
          },
          cancel(){
            this.styles.height = "0%"
          },
          saveIt(id){
            if(this.image == ''){
              alert("please fill image")
            }
            else {
              const data = new FormData();
            data.append('image',this.image);
            data.append('title',this.need.title);
            data.append('text',this.need.text);
            data.append('user',this.number);
            data.append('id',this.need.id);
            data.append('username',localStorage.getItem('username'));
            axios.put(`http://localhost:8000/router/list/${id}/`,data,
              {
                headers:{
                  'Content-Type':'multipart/form-data'
                }
              })
              .then(
                response =>{

                  this.styles.height = "0%"
                }
              )
              .catch(
                err =>{
                  this.error= err
                }
              )
            }
          },
          onFileChange(event) {
              const files = event.target.files;
              let filename = files[0].name;
              if(filename.lastIndexOf('.') <= 0){
                return alert("Please add a valid file")
              }
              const fileReader = new FileReader()
              fileReader.addEventListener('load', () => {
                this.myimage = fileReader.result
              })
              fileReader.readAsDataURL(files[0])
              this.image = files[0]
          },
      }
    }
</script>

<style scoped>
  .list{
    width: 40%;
    background-color: white;
    margin: 0 auto;
    font-family: 'Quicksand',sans-serif;
  }
  .hard{
    font-weight: bold;
  }
  .addPost{
    width: 100%;
    transition: 0.5s all;
    overflow: hidden;
    position: fixed;
    left:0;
    top:0;
    background-color: white;
    font-family: 'Raleway',sans-serif;
    color:#3b4149;
    z-index: 1;
  }
  input[type=file]{

    display: none;
  }
  .btns{
    background-color: #a33737;
    color:white;
  }
  .tools .fa-thumbs-up{
    margin: 0 20px;
  }
  .up:hover  .tools{
    background-color: rgba(0,0,0,0.6);
  }
  .into{
    width: 40%;
    margin: 40px auto;
    padding: 10px;
  }
  .tools .fa{
    color:white;
    font-size: 30px;
    cursor: pointer;
    transition: 0.5s all;
  }
  .tools .fa:hover{
    color:#3b4149
  }
  p img{
    width: 100%;
    height: 80%;
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
  .blogs{
    position: relative;
  }

  h4{
    font-family: 'Raleway',sans-serif;
    padding: 10px 0px;
    color:#3b4149;
  }
  button{
    font-family: 'Quicksand',sans-serif;
    z-index: 0;
  }
  @keyframes animate {
    from{
      transform: scale(0.5);
    }
    to{
      transform: scale(1);
    }
  }
  .detail{
    font-family: 'Raleway',sans-serif;
    padding: 10px;
    margin: 0 auto;
    font-size: 18px;
  }
  .delete{
    color:#af2440
  }
  .edits{
    color:#3b475e
  }
  .edit i{
    font-size: 17px;
    cursor: pointer;
    padding: 0px 10px;
  }

  .edit{
    position: absolute;
    right: 0;
    top:0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 12%;
    height: 100%;
  }
  .cycle{
    position: relative;
    padding: 10px;
    transition: 0.5s all;
    border-bottom:1px solid #edf2f9;
  }
  .cycle:hover{
    box-shadow: 0 0 5px rgba(0,0,0,0.5);
  }
  .images{
    width: 20%;
    position: absolute;
    left:0;
    top:0;
    height: 100%;
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
</style>
