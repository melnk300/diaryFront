<template>
  <div class="main">
    <h2 class="greetings">Sign up to Diary</h2>
    <h5 class="have_account">Already have an account? <a href="#" class="link_d">Log in</a></h5>
    <form>
      <div class="name">
        <label for="name">Email:</label>
        <input id="name" type="email" placeholder="You're name" v-model="email">
      </div>
      <div class="password">
        <label for="password">Password:</label>
        <input id="password" type="password" v-model="password">
      </div>
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
  form > * {
    display: block;
  }

  label {
    font-size: 1.15rem;

  }

  input {
    font-size: 1.3rem;
    width: 80%;
    border: none;
  }

  .email, .password {

  }
</style>
