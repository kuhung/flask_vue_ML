<template>
  <div id="todo-list-example" class="container">
    <!-- set progressbar -->
    <vue-progress-bar></vue-progress-bar>
    <div class="row">
      <div class="col-md-6 mx-auto">
        <h1 class="text-center">Natural Language Processing (NLP)</h1>
        <form v-on:submit.prevent="addNewTask">
          <label for="tasknameinput">Spam Classification</label>
          <input v-model="taskname" type="text" id="tasknameinput" class="form-control" placeholder="Enter Sentence">
          <button type="submit" class="btn btn-success btn-block mt-3">
            Submit
          </button>
        </form>

        <table class="table">
          <tr>
            <td class="font-weight-bold text-left">Text</td>
            <td class="font-weight-bold text-left">Prediction</td>
          </tr>
          <tr v-for="(txt) in textClassify" v-bind:key="txt.id" v-bind:title="txt.title" v-bind:tag="txt.tag">
            <td class="text-left">{{txt.title}}</td>
            <td class="text-left">{{txt.tag}}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      textClassify: [],
      id: '',
      taskname: '',
      isEdit: false
    }
  },
  mounted () {
    this.getTasks()
  },
  methods: {
    start () {
      this.$Progress.start()
    },
    set (num) {
      this.$Progress.set(num)
    },
    increase (num) {
      this.$Progress.increase(num)
    },
    decrease (num) {
      this.$Progress.decrease(num)
    },
    finish () {
      this.$Progress.finish()
    },
    fail () {
      this.$Progress.fail()
    },
    getTasks () {
      axios({ method: 'GET', url: '/api/tasks' }).then(
        result => {
          console.log(result.data)
          this.textClassify = result.data
        },
        error => {
          console.error(error)
        }
      )
    },
    addNewTask () {
      this.$Progress.start()
      axios.post('/api/task',
        { title: this.taskname })
        .then(res => {
          this.taskname = ''
          this.getTasks()
          console.log(res)
          this.$Progress.finish()
        },
        res => {
          this.$Progress.fail()
        })
        .catch(err => {
          console.log(err)
        })
    },

    editTask (title, id) {
      this.id = id
      this.taskname = title
      this.isEdit = true
    },
    deleteTask (id) {
      axios.delete(`/api/task/${id}`)
        .then(res => {
          this.taskname = ''
          this.getTasks()
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
