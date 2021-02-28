<template>
  <div class="main">
    <div class="c1">
      <div class="user_card">
        <img
          class="user_img"
          src="https://www.topinspired.com/wp-content/uploads/2015/04/make-up-routines-for-women-over-thirty.jpg"
          alt="img"
        />
        <div class="card_name">{{ login }}</div>
      </div>
    </div>
    <div class="c2">
      <div class="subjects">Ss</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Profile",
  data: function () {
    return {
      login: localStorage.getItem("login"),
    };
  },
};
</script>

<style scoped lang="less">
.main {
  display: grid;
  grid-template-columns: 1fr 5fr;
  gap: 1em;
}

.user_card {
  background-color: white;
  padding: 1em 0.7em;
  border-radius: 0.5em;
}

.user_img {
  width: 100%;
  border-radius: 0.5em 0.5em 0 0;
}
</style>