<template>
  <div id="app">
    <div class="logo">Diary</div>
    <div id="nav">
      <span><router-link class="link_n" to="/">Home</router-link></span>
      <span><router-link class="link_n" to="/tasks">Tasks</router-link></span>
      <span><router-link class="link_n" to="/reg">Reg</router-link></span>
    </div>
    <router-view/>
  </div>
</template>

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
    text-align: center;
    font-size: 2rem;
  }

  #nav {
    display: flex;
    justify-content: space-around;
  }

  .link_n, .link_n:hover, .link_n:active, .link_n:visited {
    color: black;
    text-decoration: none;
  }

  .link_n {
    display: inline-block;
    font-size: 1.1rem;

    &::after {
      background-color: orange;
      display: block;
      content: ' ';
      height: 2px;
      width: 30%;
      opacity: 0;
      transition: .2s ease-in-out;
    }

    &:hover:after {
      opacity: 1;
      width: 100%;
    }
  }
</style>
