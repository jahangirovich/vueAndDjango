<template>
  <div>
    <nav-bar></nav-bar>
    <div class="addPost" v-bind:style="styles">
      <div class="into">
        <h2>Add Post</h2>
        <form @submit.prevent="addPost" name="myform" novalidate  enctype="multipart/form-data">
          <p>
            <v-text-field
            v-model="title"
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
            v-model="text"
          ></v-textarea>
          </p>
          <p v-if="!image">
                <v-btn
                  small
          color="blue-grey"
          class="white--text"
          @click="$refs.file.click()"
        >
          Upload
          <v-icon right dark>cloud_upload</v-icon>
        </v-btn>
            <input multiple type="file" required id="file" ref="file" @change="onFileChange" >
          </p>
          <p v-else>
            <img :src="image">
          </p>
          <v-btn depressed color="primary" type="submit" class="btn" >add</v-btn>
          <v-btn depressed color="error" class="btns" @click="close">close</v-btn>
        </form>
      </div>
    </div>
    <div class="all">
        <div class="centering">
          <div class="main">
            <div class="description">
              <h3>Hi There, Welcome To solveProblem </h3>
              <p>
                Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
                It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged
              </p>
              <v-btn small @click="appear" style="background-color: #3b4149;color:white;">Add Post</v-btn>
              <p class="my">
                <v-text-field
                v-model="searchText"
                label="Search"
                prepend-icon="search"
              ></v-text-field>
              </p>
            </div>
            <div class="blogs">
              <div class="real">
                <div v-if="loader" class="main_loader">
                    <div class="loader">
                    </div>
                </div>
                <div v-for="reality in filterBlogs" class="up">
                  <div class="words">
                    <h3>{{ reality.title }}</h3>
                    <p class="detail">
                      {{ reality.text }}
                    </p>
                    <div class="background">
                      <img :src="reality.image" alt="" width="100%" height="100%">
                      <div class="absolute">
                        <i class="fa fa-thumbs-up"></i>
                        <i class="fa fa-comment" aria-hidden="true" @click="getPost(reality.id)">{{ len }}</i>
                      </div>
                    </div>
                  </div>
                  </div>
                </div>
              </div>
            <div class="comments" v-bind:style="commentStyles">
              <div class="in_comments">
                <div class="head">
                  <p>
                    Comment For this post
                  </p>
                </div>
                <div class="center">
                  <ul>
                    <li v-for="comment in filterComments">
                      <div class="myname">
                        <div class="username">
                          <span>{{ comment.username }}</span>
                        </div>
                        <div class="text">
                          {{ comment.text }}
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="preloader" v-if="load">
                  <div class="loader">
                  </div>
                </div>
                <div class="foot">
                  <p class="hi">
                     <v-textarea
                      name="input-7-1"
                      label="Comment"
                      hint="Hint text"
                      v-model="commentText"
                    ></v-textarea>
                  </p>
                  <v-btn
                    small
                    @click="addComment"
                  >Save</v-btn>
                  <v-btn
                    small
                    @click="nothing"
                    class="mybtn">
                    Cancel
                  </v-btn>
                </div>
              </div>
            </div>
            </div>
          </div>
        </div>
    </div>
</template>


<style scoped>
  .centering{
    display: flex;
    margin: 0 auto;
    color:#3b4149
  }
  .mybtn{
    color:white;background-color: #a33737;
  }
  .head{
    position: relative;
    left:0;
    top:0;
    width: 100%;
    border-bottom: 1px solid #bed4dd;
  }
  p{
    margin: 0 auto;
  }
  ul{
    margin: 0 auto;
    width: 100%;
    padding: 0;
  }
  .hi textarea{
    font-size: 12px;
  }
  .detail{
    margin: 0 auto;
    position: relative;
    padding: 10px;
  }
  .foot{
    position: absolute;
    border-top: 1px solid #bed4dd;
    bottom:0;
    left:0;
    width: 100%;
    padding: 0px 0px;
    transition: 0.3s all;
  }
  .myname{
    position: relative;
    margin: 0 auto;
    padding: 10px;
    transition: 0.2s all;
    cursor: pointer;
    box-sizing: border-box;
    width: 100%;
    display: flex;
  }
  .username{
    width: 10%;
    font-weight: bold;
  }
  .text{
    width: 90%;
  }
  .myname:hover{
    background-color: #e3eff4;
  }
  .comments{
    background-color: rgba(0,0,0,0.6);
    position: fixed;
    width: 100%;
    height: 100%;
     transition: 0.5s all;
    left:0;
    top:0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .foot p{
    width: 80%;
  }
  .in_comments{
    background-color: white;
    width: 30%;
    height: 60%;
    position: relative;
    margin: 0 auto;
    transition: 0.5s all;
    font-family: 'Raleway',sans-serif;
  }
  .center{
    width: 100%;
  }
  .head p{
    padding: 10px;
    box-sizing: border-box;
  }
  .background{
    margin: 10px 0;
    position: relative;
  }
  .absolute{
    position: absolute;
    left:0;
    top:0;
    width: 100%;
    height: 99%;
    background-color: rgba(0,0,0,0);
    transition: 0.4s all;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .absolute i{
    color:white;
    cursor: pointer;
    transition: 0.5s all;
    transform: scale(0);
    font-size: 28px;
    margin: 0px 10px;
  }
  .absolute i:hover{
    color:#3b4149
  }
  .up:hover .absolute{
    background-color: rgba(0,0,0,0.6);
  }
  .up:hover .absolute i{
    transform: scale(1);
  }
  .image{
    position: relative;
    height: 100%;
  }
  h3{
    font-family: 'Raleway',sans-serif;
  }
  input[type=file]{
    visibility: hidden;
    width: 100%;
    display: inline-block;
  }
   label{
    font-family: 'Quicksand',sans-serif;
  }
   .v-text-field input{
     font-family: 'Raleway',sans-serif;
     font-weight: normal;
   }
   ul li{
     list-style-type: none;
   }
  .up{
    position: relative;
    animation: animate 0.6s ;
    border-bottom: 10px solid #edf2f9;
    box-sizing: border-box;
  }
  .my{
    position: relative;
    display: block;
    margin: 0 auto;
  }
  .search{
    width: 40%;
    margin: 20px auto;
  }
  .btns{
    background-color: #a33737;
    color:white;
  }
  .tools .fa-thumbs-up{
    margin: 0 20px;
  }
  .image{
    position: relative;
  }
  .up:hover  .tools{
    background-color: rgba(0,0,0,0.6);
  }
  .tools{
    position: absolute;
    left:0;
    transition: 0.2s all;
    top:0;
    width: 100%;
    height: 99%;
    margin: 0 auto;
    background-color: rgba(0,0,0,0);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
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
  .main_loader{
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    width: 100%;
    height: 100%;
    left:0;
    top:0;
  }
  p img{
    width: 100%;
    height: 80%;
  }
  .bottom{
    background-color: #edf2f9;
    padding: 10px;
    position: absolute;
    right: 0;
    bottom:0;
    width: 100%;
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

  .words p{
    padding: 10px 0px 0px 0px;
    font-family: 'Quicksand',sans-serif;
    text-align: left;
  }
  h4{
    font-family: 'Raleway',sans-serif;
    padding: 10px 0px;
    color:#3b4149;
  }
  .words{
    padding: 10px;
  }
  .upload{
    margin: 0 auto;
    text-align: center;
    display: inline-block;
    color:#3b4149;
    cursor: pointer;
    box-shadow: 0 0 5px rgba(0,0,0,0.5);
    padding: 10px;
    font-size: 13px;
  }
  .btn{
    background-color: #5a7896;
    color:white;
  }
  .description p{
    font-family: 'Quicksand',sans-serif;
    font-size: 13px;
    padding: 15px;
    box-sizing: border-box;
  }
  .description{
    width: 40%;
    margin: 0 auto;
    background-color: white;
    padding: 20px;
    box-sizing: border-box;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
    animation: animate 0.5s;
  }
  button{
    font-family: 'Quicksand',sans-serif;
    z-index: 0;
  }
  input[type=text]{
    border-bottom:1px solid #3b4149;
  }
  input[type=text]:focus ~ label,input[type=text]:valid ~ label{
    color:#5a7896;
    font-size: 11px;
    top:-5px;
    left:0;
  }
  input[type=text]:focus{
    border-bottom:1px solid #5a7896
  }
  p{
    position: relative;
  }
  p label{
    position: absolute;
    left:10px;
    transition: 0.3s all;
    top:10px;
  }
  .into{
    padding: 20px;
    box-sizing: border-box;
  }
  .into h2{
    font-weight: normal;

  }
  form{
    width: 30%;
    padding: 10px;
    margin: 50px auto;
  }
  form p input{
    width: 100%;
    outline: none;
    padding: 10px;
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
  @keyframes animate {
    from{
      transform: scale(0.5);
    }
    to{
      transform: scale(1);
    }
  }
  .description h3{
    font-family: 'Raleway',sans-serif;
  }
  .main{
    display: block;
    width: 100%;
  }
  .preloader{
    width: 100%;
    height: 100%;
    position: absolute;
    left:0;
    top:0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .blogs{
    padding: 0px;
    box-sizing: border-box;
    background-color: white;
    width: 40%;
    margin: 10px auto;
  }
  span{
    font-family: 'Quicksand',sans-serif;
  }
</style>

<script>
    import axios from 'axios'
    import navbar from './navbar'
    export default {
        name: "list",
        components:{
          'nav-bar':navbar
        },
        data(){
          return{
            hi:[],
            number:'',
            sheet:[],
            real:[],
            text:'',
            commentText:'',
            postTitle:[],
            title:'',
            image:'',
            comments:[],
            searchText:'',
            myimage:null,
            user:null,
            load:true,
            len:'',
            lenof:[],
            loader:true,
            me:null,
            error:[],
            styles:{
              height:"0%"
            },
            commentStyles:{
              transform:'scale(0)'
            },
            drawer: null,
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
        computed:{
          filterBlogs:function () {
            return this.real.filter((reality) => {
                return reality.title.toLowerCase().match(this.searchText)
            })
          },
          filterComments(){
            return this.comments.filter(
              (comment) =>{
                if(comment.post == this.postTitle.id){
                  this.lenof.push(comment.post);
                  this.len = this.lenof.length;
                  console.log(this.len);
                  return comment.text
                }
              }
            )
          }
        },
        methods:{
          define(){
            for (var x = 0;x < this.hi.length;x++){
              if(this.hi[x].key == localStorage.getItem('authToken')){
                this.number = this.hi[x].user;
              }
             }
          },
          clickToComment(){
            this.commentStyles.transform = "scale(1)"
          },
          nothing(){
            this.commentStyles.transform = "scale(0)"
          },
          appear(){
            this.styles.height = "100%"
          },
          close(){
            this.styles.height = "0%"
          },
          addPost:function (event) {
            const data = new FormData();
            data.append('image',this.myimage);
            data.append('title',this.title);
            data.append('text',this.text);
            data.append('user',this.number);
            data.append('username',localStorage.getItem('username'));
            if(this.title == '' || this.text == '' || this.myimage == ''){
              alert("Sorry But fields is empty")
            }
            else{
             axios.post(`http://localhost:8000/router/list/`,data,
              {
                headers:{
                  'Content-Type':'multipart/form-data'
                }
              }
              )
              .then(
                response =>{
                  this.real = response.data
                  this.getInf()
                  this.styles.height = "0%";
                  this.image = ""
                  this.text = ""
                  this.user = ""
                  this.title = ""
                  this.text = ""
                }
              )
              .catch(
                err =>{
                  console.log(err)
                }
              )
            }
          },
          disappear(){
            if(this.styles.marginLeft == "0%"){
              this.styles.marginLeft = "-20%"
            }
            else{
              this.styles.marginLeft = "0%"
            }
          },
          clear(){
            localStorage.clear('authToken');
            localStorage.removeItem('username');
            this.$router.push('/login')
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
                this.real = response.data
                this.loader = false;

              }
            )
          },
          getPost(id){
            axios.get(`http://localhost:8000/router/list/${id}/`)
              .then(
                response =>{
                  this.postTitle = response.data
                  this.commentStyles.transform = "scale(1)"
                  this.getComments()
                }
              )
              .catch(
                err =>{
                  console.log(err)
                }
              )
          },
          addComment(){
            if(this.commentText == ""){
              alert("Please fill it")
            }
            else{
             axios.post(`http://localhost:8000/router/comments/`,
              {
                text:this.commentText,
                user:this.number,
                post:this.postTitle.id,
                username:localStorage.getItem('username')
              })
             .then(
               response =>{
                 this.getComments()
                 this.load = false
               }
             )
             .catch(
               err =>{
                 this.error = err
               }
             )
            }
          },
          getComments(){
            axios.get(`http://localhost:8000/router/comments/`)
              .then(
                response =>{
                  this.comments = response.data
                  this.load = false
                }
              )
              .catch(
                err =>{
                  console.log(err)
                }
              )
          },
          onFileChange(event) {
            const files = event.target.files;
            let filename = files[0].name;
            if(filename.lastIndexOf('.') <= 0){
              return alert("Please add a valid file")
            }
            const fileReader = new FileReader()
            fileReader.addEventListener('load', () => {
              this.image = fileReader.result
            })
            fileReader.readAsDataURL(files[0])
            this.myimage = files[0]
          },
        }
    }
</script>
