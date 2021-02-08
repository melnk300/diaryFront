<template>
  <div class="main">
    <div class="date">
      <span class="back_arrow arrow"></span>
      <span class="today_date">{{beautifulDate}}</span>
      <span class="forward_arrow arrow"></span>
    </div>
    <div class="content">

    </div>
  </div>
</template>

<script>
const luxon = require('luxon')
const dt = luxon.DateTime

export default {
  name: "Tasks",
  data: function () {
    return {
      date: dt.local().setLocale('ru'),
      tasks: [
        {
          id: '1',
          subject: 'русский',
          task: '№434',
          author: 'Rusm'
        },
        {
          id: '2',
          subject: 'русский',
          task: '№434',
          author: 'Rusm'
        },
        {
          id: '3',
          subject: 'русский',
          task: '№434',
          author: 'Rusm'
        }
      ]
    }
  },
  computed: {
    beautifulDate: function () {
      return this.date.toFormat('dd LLL yyyy')
    }
  }
}
</script>

<style scoped>

</style>
