<template>
  <div id="app">
    <div id="nav">
      <span class="link_n"><router-link to="/">Home</router-link></span> |
      <span class="link_n"><router-link to="/about">Reg</router-link></span>
    </div>
    <router-view/>
  </div>
</template>

<style lang="less">
  .link_n {

  }
</style>
