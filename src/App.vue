<template>
  <div id="app">
    <div class="error_d" v-if="error" :class="error.level" v-on:>
      <p class="error_head">{{ error.header }}</p>
      <p class="error_msg">{{ error.description }}</p>
      <button class="error_btn" v-on:click="closeError">Ok</button>
    </div>
    <div class="logo">Diary</div>
    <div id="nav">
      <span><router-link class="link_n" to="/">Home</router-link></span>
      <span><router-link class="link_n" to="/tasks">Tasks</router-link></span>
      <span v-if="isReg === '0'"
        ><router-link class="link_n" to="/log_in"
          >Log in | Sign up</router-link
        ></span
      >
      <p class="user_links" v-else>
        <router-link to="/profile" class="link_n">Profile</router-link>
        <span class="link_n" v-on:click="signOut">Sign out</span>
      </p>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      isReg: localStorage.getItem("isReg"),
    };
  },
  mounted() {
    console.log(this.error);
  },
  methods: {
    signOut: function () {
      localStorage.setItem("isReg", "0");
      localStorage.setItem("login", "");
      localStorage.setItem("password", "");
      this.$router.go(this.$router.currentRoute);
    },
    closeError: function () {
      this.$store.commit("SET_ERROR", "");
    },
  },
  computed: {
    error() {
      return this.$store.getters.ERROR;
    },
  },
};
</script>

<style scoped>
</style>

<style lang="less">
* {
  font-family: Roboto, sans-serif;
  padding: 0;
  margin: 0;
}

#app {
  background-color: #fafafa;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.logo {
  margin: 0.3em 0;
  text-align: center;
  font-size: 2rem;
  cursor: pointer;
}

#nav {
  display: flex;
  justify-content: space-around;
}

.link_n,
.link_n:hover,
.link_n:active,
.link_n:visited {
  color: black;
  text-decoration: none;
}

.link_n {
  display: inline-block;
  font-size: 1.1rem;
  cursor: pointer;

  &::after {
    background-color: orange;
    display: block;
    content: " ";
    height: 2px;
    width: 30%;
    opacity: 0;
    transition: 0.2s ease-in-out;
  }

  &:hover:after {
    opacity: 1;
    width: 100%;
  }
}

.error_d {
  top: 0.5em;
  left: 50%;
  transform: translate(-50%, 0);
  position: fixed;
  display: flex;
  background-color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 0.4rem;
  flex-direction: column;
  align-items: flex-end;

  &.error {
    background-color: rgb(250, 139, 139);
  }

  button.error_btn {
    margin-top: 0.4rem;
    font-size: 1rem;
    padding: 0.36rem 0.5rem;
    background: none;
    border: 1px solid black;
    border-radius: 0.6rem;
    transition: 0.2s ease-in-out;
    cursor: pointer;

    &:hover {
      background-color: black;
      color: white;
    }
  }
}

.user_links {
  span {
    margin: 0 0.4em;
  }
}
</style>
