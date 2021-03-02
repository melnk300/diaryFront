<template>
  <div class="main">
    <div class="content">
      <h2 class="greetings">Log in to Diary</h2>
      <h5 class="have_account">
        Do not have account?<router-link to="sign_up" class="link_d"
          >Let's Sing up</router-link
        >
      </h5>
      <form>
        <div class="name" :class="{ error: errorName }">
          <label for="name">Name:</label>
          <input
            id="name"
            type="text"
            placeholder="You're name"
            v-model="name"
            v-on:input="changedName"
          />
        </div>
        <div class="password" :class="{ error: errorPassword }">
          <label for="password">Password:</label>
          <input
            id="password"
            type="password"
            v-model="password"
            placeholder="You're password"
            v-on:input="changedPassword"
          />
        </div>
      </form>
      <button v-on:click="registerUser">Sign in</button>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
const axios = require("axios");

export default {
  name: "LoginUser",
  data: function () {
    return {
      name: "",
      password: "",
      errorName: false,
      errorPassword: false,
    };
  },
  mounted() {
    if (localStorage.getItem("isReg") === "1") {
      this.$router.push("/tasks");
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
        axios
          .post(
            `http://${process.env.VUE_APP_HOST_CUSTOM}:5000/api/log_check`,
            {
              login: this.name,
              password: this.password,
            }
          )
          .then((res) => {
            console.log(res);
            if (res.data === 200) {
              console.log(`i'm ok. I'm not teapot`);
              localStorage.setItem("isReg", "1");
              localStorage.setItem("login", this.name);
              localStorage.setItem("password", this.password);
              this.$router.push("/tasks");
              this.$router.go(this.$router.currentRoute);
            } else {
              this.$store.dispatch("ADD_ERROR", {
                header: "You're login or password incorrect.",
                description: "",
                level: "error",
              });
            }
          });
      }
    },
  },
};
</script>

<style scoped>
.main {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.content {
  width: min(80%, 500px);
}

input,
label {
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
  outline: none;
}

.name,
.password {
  padding: 0.4rem 0.8rem;
  border-radius: 0.6rem;
  border: 1px solid #b4b4b4;
  margin: 1rem 0;
}

.name.error,
.password.error {
  border-color: red;
}

button {
  font-size: 1.4rem;
  display: block;
  width: 100%;
  padding: 0.36rem 0;
  background: none;
  border: 1px solid black;
  border-radius: 0.6rem;
  transition: 0.5s ease-in-out;
}

button:hover {
  background-color: black;
  color: white;
}
</style>
