<template>
    <div class="cover">
      <nav-bar v-bind:color="color.backgroundColor" v-bind:back="back.backgroundImage"></nav-bar>
      <div class="profile">
        <div class="image" v-bind:style="styles">
          <div class="add">
            <span @click="$refs.image.click()" v-if="!show" style="cursor: pointer;">Upload Image</span>
            <v-btn
              small
              v-if="show"
            >
              edit
            </v-btn>
            <input type="file" id="file" ref="image" style="display: none" @change="onFileChange">
          </div>
        </div>
        <div class="text">
          <div v-if="exist">
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
          <div v-if="!exist">
            <p>
              <v-text-field
              v-model="firstName"
              label="FirstName"
              required
              class="v-label"
              name="hi"
              ></v-text-field>
            </p>
            <p>
              <v-text-field
              v-model="surname"
              label="Surname"
              required
              name="hi"
              ></v-text-field>
            </p>
            <v-layout row wrap>
              <v-flex>
                <v-date-picker v-model="date" color="#3b4149 lighten-1" header-color="black"></v-date-picker>
              </v-flex>
            </v-layout>
            <v-btn
              small
              @click="addProfile"
            >
              Save
            </v-btn>
          </div>
          <div class="friends" v-if="exist">
            <p>Friends</p>
            <div class="profiles">

            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    import navbar from './navbar'
    import axios from 'axios'
    export default {
        name: "profile",
        components:{
          'nav-bar':navbar
        },
        data(){
          return{
            profile:{},
            errors:[],
            exist:false,
            firstName:'',
            surname:'',
            id:null,
            date:null,
            image:'',
            menu:false,
            show:false,
            filter:'',
            styles:{
              backgroundImage:`url(https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=9017084ac611b76fb7506ccc54d854ac&auto=format&fit=crop&w=2089&q=80)`,
              backgroundPosition:"center",
              backgroundSize:"cover"
            },
            color:{
              backgroundColor:'#4d657a'
            },
            myimage:'',
            back:{
              backgroundImage:'url(https://images.unsplash.com/photo-1532985757448-5335e8b6187b?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=d239a2ddd05a08bbd2ace32cd01307fd&auto=format&fit=crop&w=1950&q=80)'
            },
          }
        },
        watch: {
          menu (val) {
            val && this.$nextTick(() => (this.$refs.picker.activePicker = 'YEAR'))
          }
        },
        created(){
          axios.get(`http://localhost:8000/router/profiles/`)
              .then(
                response =>{
                  for(var x in response.data){
                    if(localStorage.getItem('username') == response.data[x].username){
                      this.profile = response.data[x]
                      localStorage.setItem('id',this.profile.id)
                    }
                  }
                  if(this.profile == [] || this.profile == null){
                    this.styles.backgroundImage = 'url(https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=9017084ac611b76fb7506ccc54d854ac&auto=format&fit=crop&w=2089&q=80)'
                  }
                  else{
                    for(var x in this.profile){
                      this.styles.backgroundImage = `url(${this.profile.image})`;
                      localStorage.setItem('image',this.profile.image);
                      this.id = this.profile.id
                      this.exist = true
                      break
                    }
                  }
                }
              )
              .catch(
                err =>{
                  this.errors = err
                }
              )
        },
        methods:{

          save (date) {
            this.$refs.menu.save(date)
          },
          addProfile(){
            const data = new FormData();
            data.append('image',this.myimage);
            data.append('firstName',this.firstName);
            data.append('surname',this.surname);
            data.append('date',this.date);
            data.append('username',localStorage.getItem('username'));
            axios.post(`http://localhost:8000/router/profiles/`,data,{
              headers:{
                  'Content-Type':'multipart/form-data'
                }
            })
              .then(
                response =>{
                  this.profile = response.data;
                  localStorage.setItem('image',this.image);
                  this.exist = true
                }
              )
              .catch(
                err =>{
                  this.errors = err
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
              this.styles.backgroundImage = `url('${fileReader.result}')`
              this.image = fileReader.result
            })
            fileReader.readAsDataURL(files[0])
            this.myimage = files[0]
            this.show = true
          },
        }
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
  .text{
    font-family: 'Raleway',sans-serif;
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
    border-radius: 50%;
    font-weight: bold;
  }
  .image:hover .add{
    background-color: rgba(0,0,0,0.6);
    width: 100%;
  }
  .friends{
    clear: left;
    position: relative;
    width: 100%;
    display: block;
    padding: 10px;
  }
  .friends p{
    font-weight: bold;
    font-family: 'Raleway',sans-serif;
  }
  .image{
    position: relative;
    width: 180px;
    height: 180px;
    cursor: pointer;
    border-radius: 50%;
    display: inline-block;
    float: left;
  }
  .text{
    width: 55%;
    margin: 0 auto;
    display: inline-block;
  }
  p{
    margin: 0 auto;
  }
</style>
