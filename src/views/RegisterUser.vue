<template>
  <div class="main">
    <h2 class="greetings">Sign up to Diary</h2>
    <h5 class="have_account">Already have an account? <a href="#" class="link_d">Log in</a></h5>
    <form>
      <label for="email">Email:</label>
      <input id="email" type="email" placeholder="example@mail.com">
      <label for="password">Password:</label>
      <input id="password" type="password">
    </form>
  </div>
</template>

<script>
export default {
  name: "RegisterUser",
  data: function () {
    return {
      email: '',
      password: ''
    }
  }
}
</script>

<style scoped lang="less">

</style>
