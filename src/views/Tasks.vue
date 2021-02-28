<template>
  <div class="main">
    <div class="date">
      <!--      <span class="back_arrow arrow">&#706;</span>-->
      <span class="today_date">
        <input type="date" id="date" v-model="inputDate" />
      </span>
      <!--      <span class="forward_arrow arrow" v-on:click="addDay">&#707;</span>-->
    </div>
    <div class="content">
      <div class="task-card" v-for="task in tasks" :key="tasks.indexOf(task)">
        <p class="meta">
          <span class="subject">{{ task.subject }}</span>
          <span class="author">{{ task.author }}</span>
        </p>
        <p class="task-content">{{ task.task }}</p>
      </div>
    </div>
    <div class="popup" v-if="modalActive">
      <div class="popup_menu">
        <form v-on:submit.prevent="addTask">
          <h2>Let's add a task</h2>
          <div class="input" :class="{ error: errorSubject }">
            <input
              id="subject"
              type="text"
              placeholder="Subject"
              v-model="newTask.subject"
              v-on:input="changedSubject"
            />
          </div>
          <div class="input" :class="{ error: errorTask }">
            <input
              id="task"
              type="text"
              placeholder="Task"
              v-model="newTask.task"
              v-on:input="changedTask"
            />
          </div>
          <div class="input" :class="{ error: errorDate }">
            <input
              id="form_date"
              type="date"
              v-model="newTask.date"
              v-on:input="changedDate"
            />
          </div>
          <button>Submit</button>
        </form>
      </div>
    </div>
    <div class="popup_btn" v-on:click="modalActive = true">+</div>
  </div>
</template>

<script>
const axios = require("axios");
const luxon = require("luxon");
let dt = luxon.DateTime.local().setLocale("ru");
export default {
  name: "Tasks",
  data() {
    return {
      inputDate: dt.toFormat("yyyy-MM-dd"),
      tasks: [
        {
          id: "1",
          subject: "русский",
          task: "Выполнить упражнения: 244-250 (под нечётными номерами)",
          author: "Rusm",
        },
        {
          id: "2",
          subject: "русский",
          task: "№434",
          author: "Rusm",
        },
        {
          id: "3",
          subject: "русский",
          task: "№434",
          author: "Rusm",
        },
        {
          id: "4",
          subject: "русский",
          task: "№434",
          author: "Rusm",
        },
        {
          id: "5",
          subject: "русский",
          task: "№434",
          author: "Rusm",
        },
        {
          id: "6",
          subject: "русский",
          task: "№434",
          author: "Rusm",
        },
      ],
      newTask: {
        subject: "",
        task: "",
        date: "",
      },
      modalActive: false,
      errorSubject: false,
      errorTask: false,
      errorDate: false,
    };
  },
  methods: {
    addTask: function () {
      if (this.newTask.subject && this.newTask.task && this.newTask.date) {
        axios.post(`http://${process.env.VUE_APP_HOST_CUSTOM}:5000/api/`, {
          user: {
            login: localStorage.getItem("login"),
            password: localStorage.getItem("password"),
          },
          payload: {
            subject: this.newTask.subject,
            task: this.newTask.task,
          },
        });
        console.log(
          localStorage.getItem("login"),
          localStorage.getItem("password")
        );
        this.modalActive = false;
      }
    },
    changedSubject: function () {
      this.errorSubject = !this.newTask.subject;
    },
    changedTask: function () {
      this.errorTask = !this.newTask.task;
    },
    changedDate: function () {
      this.errorDate = !this.newTask.date;
    },
  },
  computed: {},
};
</script>

<style scoped>
.popup_menu {
  width: min(80%, 400px);
}

form {
  width: 100%;
}
</style>

<style scoped lang="less">
@media screen and (max-width: 991px) {
  .task-card {
    margin: 0.8em 0;
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
  margin-top: 0.5em;
}

#date {
  border: none;
  background: none;
  text-align: center;
  cursor: pointer;
}

.content {
  margin: 1.2em 0.6em;
}

.task-card {
  padding: 0.6em 1.2em;
  background-color: white;
  border-radius: 1em;
  box-shadow: 1px 1px 6px 1px rgba(0, 0, 0, 0.06);

  .subject {
    font-size: 1.2em;
    text-transform: capitalize;
  }

  .author {
    font-size: 0.8em;
    color: #7389d6;
    padding: 0 0.6em;
  }

  .task-content {
    font-size: 1.1em;
  }
}

.popup_btn {
  position: fixed;
  display: flex;
  background-color: #60e060;
  width: 1.2em;
  height: 1.2em;
  font-size: 2em;
  border-radius: 50%;
  justify-content: center;
  align-items: center;
  right: 0.6em;
  bottom: 0.6em;
  cursor: pointer;
}

.popup {
  position: fixed;
  display: flex;
  justify-content: center;
  align-items: center;
  left: 0;
  top: 0;
  height: 100vh;
  width: 100vw;
  background-color: rgba(0, 0, 0, 0.2);

  .popup_menu {
    background-color: white;
    display: flex;
    align-items: center;
    padding: 1em 0.8em;
    border-radius: 1em;
    box-shadow: 1px 1px 6px 1px rgba(0, 0, 0, 0.06);

    input {
      background: none;
      font-size: 1.2rem;
      width: 100%;
      border: none;
      outline: none;
    }

    .input {
      padding: 0.4rem 0.8rem;
      border-radius: 0.6rem;
      border: 1px solid #b4b4b4;
      margin: 1rem 0;
    }

    .error {
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

      &:hover {
        color: white;
        background-color: black;
      }
    }
  }
}
</style>
