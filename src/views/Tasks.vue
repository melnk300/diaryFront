<template>
  <div class="main">
    <div class="pop_up-button">+</div>
    <div class="pop_up-menu">
      <div class="pop_up-content">
        <h2>Add task</h2>
      </div>
    </div>
    <div class="date">
<!--      <span class="back_arrow arrow">&#706;</span>-->
      <span class="today_date">
        <input type="date" id="date" v-model="inputDate">
      </span>
<!--      <span class="forward_arrow arrow" v-on:click="addDay">&#707;</span>-->
    </div>
    <div class="content">
      <div class="task-card" v-for="task in tasks" :key="tasks.indexOf(task)">
        <p class="meta">
          <span class="subject">{{task.subject}}</span>
          <span class="author">{{task.author}}</span>
        </p>
        <p class="task-content">{{task.task}}</p>
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
          task: 'Выполнить упражнения: 244-250 (под нечётными номерами)',
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

<style scoped>

</style>

<style scoped lang="less">

  @media screen and (max-width: 991px) {
    .task-card {
      margin: .8em 0;
    }
  }

  @media screen and (min-device-width: 992px) {
    .content {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr 1fr;
      grid-gap: 1em;
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
    padding: .6em 1.2em;
    background-color: white;
    border-radius: 10px;

    .subject {
      font-weight: 500;
      font-size: 1.1em;
      text-transform: capitalize;
    }

    .author {
      font-size: .8em;
      color: #7389d6;
      padding: 0 .6em;
    }

    .task-content {

    }
  }

  .pop_up-button {
    display: flex;
    position: absolute;
    bottom: .8em;
    right: .8em;
    width: 1em;
    height: 1em;
    font-size: 2.5em;
    background-color: limegreen;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    cursor: pointer;
  }

  .pop_up-menu {
    position: fixed;
    margin: 5% auto
  }

  .pop_up-content {
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
