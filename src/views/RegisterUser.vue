<template>
  <div class="main">
    <div class="content">
      <h2 class="greetings">Sign up to Diary</h2>
      <h5 class="have_account">Already have an account? <a href="#" class="link_d">Log in</a></h5>
      <form>
        <div class="name" :class="{error: errorName}">
          <label for="name">Name:</label>
          <input id="name" type="text" placeholder="You're name" v-model="name" v-on:input="changedName">
        </div>
        <div class="password" :class="{error: errorPassword}">
          <label for="password">Password:</label>
          <input id="password" type="password" v-model="password" placeholder="You're password" v-on:input="changedPassword">
        </div>
      </form>
      <button v-on:click.once="registerUser">Sign in</button>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
const axios = require('axios')

export default {
  name: "RegisterUser",
  data: function () {
    return {
      name: '',
      password: '',
      errorName: false,
      errorPassword: false,
    }
  },
  methods: {
    changedName: function () {
      this.errorName = !this.name;
    },
    changedPassword: function () {
      this.errorPassword = !this.password;
    },
    registerUser: function () {
      if (this.password && this.name) {
        axios.post(`http://${process.env.VUE_APP_HOST_CUSTOM}:5000/api/reg`, {
          name: this.name,
          password: this.password
          // eslint-disable-next-line no-unused-vars
        }).then((res) => {
          localStorage.setItem('isReg', 1)
        })
      }
    }
  }
}
</script>

<style scoped>
  .main {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .content {
    width: min(80%,500px);
  }

  input, label {
    display: block;
  }

  label {
    font-size: 1rem;
  }

  input {
    background: none;
    font-size: 1.2rem;
    width: 100%;
    border: none;
    outline:none;

  }

  .name, .password {
    padding: .4rem .8rem;
    border-radius: .6rem;
    border: 1px solid #b4b4b4;
    margin: 1rem 0;
  }


  .name.error, .password.error {
     border-color: red;
   }

  button {
    font-size: 1.4rem;
    display: block;
    width: 100%;
    padding: .36rem 0;
    background: none;
    border: 1px solid black;
    border-radius: .6rem;
    transition: .5s ease-in-out;
  }

  button:hover {
    background-color: black;
    color: white;
  }
</style>
