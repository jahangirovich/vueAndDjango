<template>
  <div class="main">
    <nav-bar v-bind:color="color.backgroundColor" v-bind:back="back.backgroundImage"></nav-bar>
    <div class="test">
      <div class="first" v-if="call" id="style">
        <div class="users">
          <div class="user1">
            <div class="image" v-bind:style="style">

            </div>
            <div class="text">
              <span style="font-weight: bold">{{ username }}</span>
            </div>
          </div>
          <div class="vs">
            <i class="fa fa-bolt"></i>
          </div>
          <div class="user2">
            <div class="image2" v-bind:style="style2">

            </div>
              <div class="text">
                {{ user2.username }}
              </div>
          </div>
        </div>
        <div class="btn">
          <v-btn
          @click="getTest"
          >
            Start Fight
          </v-btn>
        </div>
      </div>
      <div class="second" v-if="!call">
        <div class="question" id="my">
          <div class="question1" id="question1">
            <div class="loading">

            </div>
            <div class="words">
              <span>{{ timer }}</span>
              <span>{{ real.question }}</span>
            </div>
            <div class="fill">
                <p>
                  <v-text-field
                  v-model="answer1"
                  label="Answer"
                  required
                  ></v-text-field>
                </p>
              <p class="btn">
                <v-btn
                small
                @click="check"
                class="button"
                >
                  Check
                </v-btn>
              </p>
            </div>
          </div>
          <div class="question1">
              <div class="yes" id="yes" v-if="show">
                <span>Right</span>
              </div>
              <div class="no" id="no" v-if="!show">
                <span>You are not right</span>
              </div>
          </div>
          <div class="question1" id="question1">
            <div class="loading">

             </div>
            <div class="words">
              <span>{{ real2.question }}</span>
            </div>
            <div class="fill">
                <p>
                  <v-text-field
                  v-model="answer2"
                  label="Answer"
                  required
                  ></v-text-field>
                </p>
              <p class="btn">
                <v-btn
                small
                @click="check"
                class="button"
                >
                  Check
                </v-btn>
              </p>
            </div>
          </div>
          <div class="question1">
              <div class="yes" id="yes" v-if="show">
                <span>Right</span>
              </div>
              <div class="no" id="no" v-if="!show">
                <span>You are not right</span>
              </div>
          </div>
          <div class="question1" id="question1">
            <div class="loading">

            </div>
            <div class="words">
              <span>{{ real3.question }}</span>
            </div>
            <div class="fill">
                <p>
                  <v-text-field
                  v-model="answer3"
                  label="Answer"
                  required
                  ></v-text-field>
                </p>
              <p class="btn">
                <v-btn
                small
                @click="check"
                class="button"
                >
                  Check
                </v-btn>
              </p>
            </div>
          </div>
          <div class="question1">
              <div class="yes" id="yes" v-if="show">
                <span>Right</span>
              </div>
              <div class="no" id="no" v-if="!show">
                <span>You are not right</span>
              </div>
          </div>
          <div class="question1" id="question1">
            <div class="loading">

            </div>
            <div class="words">
              <span>{{ real4.question }}</span>
            </div>
            <div class="fill">
                <p>
                  <v-text-field
                  v-model="answer4"
                  label="Answer"
                  required
                  ></v-text-field>
                </p>
              <p class="btn">
                <v-btn
                small
                @click="check"
                class="button"
                >
                  Check
                </v-btn>
              </p>
            </div>
          </div>
          <div class="question1">
              <div class="yes" id="yes" v-if="show">
                <span>Right</span>
              </div>
              <div class="no" id="no" v-if="!show">
                <span>You are not right</span>
              </div>
          </div>
          <div class="question1">
          </div>
        </div>
        <div class="finish" id="finish">
          <p class="end">
            Finished
          </p>
          <p>
            Good job you have finished this.Click it to see a result.
          </p>
          <p class="end_button">
                <v-btn
                small
                @click="check"
                class="button"
                >
                  Finish
                </v-btn>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    import axios from 'axios'
    import navbar from './navbar'
    export default {
        name: "call",
        components:{
          'nav-bar':navbar
        },
        data(){
          return{
            username:localStorage.getItem('username'),
            style:{
              backgroundImage:`url(${localStorage.getItem('image')})`
            },
            style2:{
              backgroundImage:``,
            },
            color:{
              backgroundColor:'#59824e'
            },
            back:{
              backgroundImage:'url(https://images.unsplash.com/photo-1533022876396-2b6f9e38fbfc?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e495e0fd33982a09987d9a3634724be7&auto=format&fit=crop&w=2134&q=80)'
            },
            user2:[],
            call:true,
            tests:[],
            real:[],
            real2:[],
            real3:[],
            real4:[],
            real5:[],
            all:[],
            right:[],
            answer1:'',
            answer2:'',
            answer3:'',
            answer4:'',
            wrong:'',
            show:false,
            some:0,
            timer:5
          }
        },

        methods:{
          decrease(){
            this.timer -= 1;
          },
          big(){
             var myindex = 0;
             carousel();
             function carousel() {
                    var i;
                    var x = document.getElementsByClassName('question1');
                    for (i = 0;i < x.length;i++){
                      x[i].style.display = "none";
                    }
                    myindex++;
                    if(myindex > x.length){
                      myindex = 1;
                    }
                    x[myindex-1].style.display = "block";
                    if(myindex%2 == 1){
                      setTimeout(carousel,9000);
                    }
                    else{
                      setTimeout(carousel,2000);
                    }
                    if(myindex == 9){
                      document.getElementById('my').style.display = "none";
                      document.getElementById('finish').style.display = "block";
                      myindex = 0
                    }
                  }
          },
          getTest(){
            this.call = false;
            axios.get(`http://localhost:8000/router/Test/`)
              .then(
                response =>{
                  this.tests = response.data;
                  var x = this.tests.length;
                  var rand;
                  var rand2;
                  var rand3;
                  var rand4;
                  var rand5;
                  function random() {
                    rand = Math.floor(Math.random() * x);
                    rand2 = Math.floor(Math.random() * x);
                    rand3 = Math.floor(Math.random() * x);
                    rand4 = Math.floor(Math.random() * x);
                    rand5 = Math.floor(Math.random() * x);
                    if(rand == rand2 || rand2 == rand3 || rand3 == rand4 || rand5 == rand || rand4 == rand2 || rand3 == rand5 || rand == rand3 || rand4 == rand5 || rand2 == rand5 || rand == rand4){
                      random()
                    }
                  }
                  random();
                  this.real = this.tests[rand];
                  this.real2 = this.tests[rand2];
                  this.real3 = this.tests[rand3];
                  this.real4 = this.tests[rand4];
                  this.real5 = this.tests[rand5];
                  this.big();
                  setInterval(this.decrease,1000);
                }
              )
              .catch(
                err =>{
                  console.log(err)
                }
              )
          },
          check(){
            if(this.answer1 == this.real.answer ||  this.answer2 == this.real2.answer || this.answer3 == this.real3.answer || this.answer4 == this.real4.answer){
              this.show = true
            }
            else if(this.answer1 != this.real.answer){
              this.show = false
            }
            var hide = document.getElementsByClassName('button');
            hide[this.some].style.display = "none";
            this.some++;
            console.log(this.some)
          }
        },
        created(){
            axios.get('http://localhost:8000/router/profiles/')
              .then(
                response =>{
                  for(var x = 0;x < response.data.length;x++){
                    if(response.data[x].username == this.$route.params.username){
                      this.user2 = response.data[x]
                    }
                  }
                  this.style2.backgroundImage = `url(${this.user2.image})`
                }
              )
              .catch(
                err =>{
                  console.log(err)
                }
              );
          },
    }
</script>

<style scoped>

  .test{
    width: 40%;
    background-color: white;
    padding: 0px;
    animation:get 0.6s;
    margin: 0 auto;
  }
  .finish{
    background-color: white;
    width: 100%;
    padding: 10px;
    margin-top: 10%;
    display: none;
    text-align: center;
    animation:get 0.6s;
    font-family: 'Quicksand',sans-serif;
  }
  .end{
     color:#59824e;
    font-size: 26px;
  }
  @keyframes get {
    from{
      transform: scale(0);
    }
    to{
      transform: scale(1);
    }
  }
  .finish .end_button button{
    background-color: white;
    color:#59824e;
    border:1px solid #59824e;
  }
  .loading{
    width: 100%;
    animation: what 8s;
    left:0;
    top:0;
    position: absolute;
    background-color: #59824e;
    padding: 5px;
  }
  .question{
    width: 100%;
    margin: 0 auto;
    animation:get 0.6s;
  }
  .question1{
    display: none;
    width: 100%;
    animation:get 0.6s;
  }
  .question2{
    display: inline-block;
    width: 100%;
  }
  @keyframes what {
    from{
      width: 0;
    }
    to{
      width: 100%;
    }
  }
  .btn{
    width: 100%;
    text-align: right;
  }
  .first{
  }
  .fill{
    width: 40%;
    margin: 0 auto;
  }
  .first{

  }
  .second{
    padding: 0;
  }
  .words{
    color:#59824e;
    padding: 10px;
  }
  .question{
    font-family: 'Raleway',sans-serif;
    font-size: 16px;
  }
  .question1{
    padding: 10px;
  }
  .vs{
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .vs i{
    font-size: 30px;
    color:#59824e
  }
  .image{
    width: 160px;
    height: 160px;
    background-position: center;
    background-size: cover;
    border-radius: 50%;
    border:2px solid lightgray;
    margin: 0 auto;
    animation: left 0.6s ;
  }
  .image2{
    width: 160px;
    height: 160px;
    border:2px solid lightgray;
    background-position: center;
    background-size: cover;
    position: relative;
    border-radius: 50%;
    animation: right 0.6s;
    margin: 0 auto;
  }
  .yes{
    font-size: 30px;
    font-family: 'Raleway',sans-serif;
    color:#59824e;
    animation:appear 0.5s;
  }
  .no{
    font-size: 30px;
    font-family: 'Raleway',sans-serif;
    color: #932c3a;
    animation:appear 0.5s;
  }
  @keyframes appear {
    from{
      position: relative;
      top:100px;
      opacity: 0;
    }
    to{
      position: relative;
      top:0;
      opacity: 1;
    }
  }
  .btn {
    width: 100%;
  }
  .btn button{
    font-family: 'Quicksand',sans-serif;
    background-color: #59824e;
    color:white;
  }
  .first{
    animation-duration: 0.4s;
  }
  @keyframes right {
    from{
      position: relative;
      right:200px;
      opacity: 0;
    }
    to{
      position: relative;
      right:0;
      opacity: 1;
    }
  }
  @keyframes disappear {
    from{
      position: relative;
      left:0px;
      opacity: 0;
    }
    to{
      position: relative;
      left:600px;
      opacity: 1;
    }
  }
  .users{
    display: flex;
    position: relative;
  }
  .user1{
    width: 50%;
    padding: 20px;
  }
  .user2{
    width: 50%;
    padding: 20px;
  }
  .question{
    position: relative;
    margin-top: 10%;
  }
  .text{
    width: 100%;
    font-family: 'Quicksand',sans-serif;
    font-size: 16px;
    padding: 10px;
  }
  @keyframes left {
    from{
      position: relative;
      left:200px;
      opacity: 0;
    }
    to{
      position: relative;
      left:0;
      opacity: 1;
    }
  }
</style>
