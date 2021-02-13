<template>
  <div class="main">
    <div class="date">
<!--      <span class="back_arrow arrow">&#706;</span>-->
      <span class="today_date">
        <input type="date" id="date" v-model="inputDate">
      </span>
<!--      <span class="forward_arrow arrow" v-on:click="addDay">&#707;</span>-->
    </div>
    <div class="content">
      <div class="tasks" v-for="task in tasks" :key="tasks.indexOf(task)">
        <div class="task-card">
          <p class="meta">
            <span class="subject">{{task.subject}}</span>
            <span class="author">{{task.author}}</span>
          </p>
          <p class="task-content">{{task.task}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const luxon = require('luxon')
let dt = luxon.DateTime.local().setLocale('ru')
export default {
  name: "Tasks",
  data() {
    return {
      inputDate: dt.toFormat('yyyy-MM-dd'),
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
        },
        {
          id: '4',
          subject: 'русский',
          task: '№434',
          author: 'Rusm'
        },
        {
          id: '5',
          subject: 'русский',
          task: '№434',
          author: 'Rusm'
        },
        {
          id: '6',
          subject: 'русский',
          task: '№434',
          author: 'Rusm'
        }
      ]
    }
  },
  computed: {
  }
}
</script>

<style scoped lang="less">

  @media handheld {
    .content {
      display: block;
    }
  }

  @media not handheld {
    .content {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr 1fr;
      grid-gap: 1.5em;
    }
  }

  .date {
    display: flex;
    justify-content: center;
    margin-top: .5em;
  }

  #date {
    border: none;
    background: none;
    text-align: center;
    cursor: pointer;
  }

  .content {
    margin: 1.2em .6em;
  }

  .task-card {
    padding: .2em .8em;
    background-color: white;
    border-radius: 10px;

    .author {
      font-size: .8em;
      color: #7389d6;
      padding: 0 .3em;
    }
  }
</style>
