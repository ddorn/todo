/**
 * This files handles all communications with the server,
 * and also to serve as a central store for all the data.
 *
 * The data here should be kept in sinc with the server,
 * but it may not happen, especially if the data on the server
 * is modified in an other way (two windows open...)
 */

import { reactive } from "vue";

const store = {
  name: "store",
  debug: true,
  state: reactive({
    todos: {},
    listId: null,
    lists: []
  }),

  getList(id) {
    if (id === undefined) {
      id = this.state.listId;
    }
    return this.state.lists.find(l => l.id === id);
  },
  getTodo(id) {
    return this.state.todos.find(t => t.id === id);
  },

  setListId(value) {
    if (value === this.state.listId) return;
    this.state.listId = value;
    if (value === null) this.state.todos = {};
    else this.fetchTodos();
  },

  fetchTodos() {
    // TODO: error handling
    if (this.debug) console.log("Fetching todos");
    fetch(`/api/list/${this.state.listId}`).then(resp =>
      resp.json().then(d => {
        if (this.debug) console.log(`Fetched ${d.length} todos`);
        this.state.todos = d.reduce((todos, todo) => {
          todos[todo.id] = todo;
          return todos;
        }, {});
      })
    );
  },

  fetchLists() {
    if (this.debug) console.log("Fetching lists");
    fetch("/api/list/").then(resp => {
      if (resp.ok) {
        resp.json().then(d => {
          this.state.lists = d;
          if (this.debug) console.log(`Fetched ${d.length} lists`);
        });
      } else {
        resp.json().then(d => console.log(d));
      }
    });
  },

  createTodo(name, categ) {
    fetch(`/api/list/${this.state.listId}`, {
      method: "post",
      body: JSON.stringify({ name, categ })
    }).then(resp =>
      resp.json().then(data => {
        this.state.todos[data.id] = data;
        // TODO: error handeling
      })
    );
  },

  modifyTodo(id, changes) {
    if (this.debug) console.log("modifyTodo:", id, changes);
    let item = this.state.todos[id];
    // backup changes
    let previous = {};
    for (let prop in changes) {
      previous[prop] = item[prop];
    }
    // apply them
    for (let prop in changes) {
      item[prop] = changes[prop];
    }
    // Push them to the server
    fetch(`/api/todo/${item.id}`, {
      method: "PATCH",
      body: JSON.stringify(changes)
    }).then(resp => {
      // Revert if there is an error
      if (!resp.ok) {
        for (let prop in changes) {
          item[prop] = previous[prop];
        }
        if (this.debug) {
          console.log(`Error modifyTodo:`, resp.details, changes);
        }
        // TODO: emit event for visual clue
      }
    });
  },

  toggleDone(id) {
    this.modifyTodo(id, { done: !this.state.todos[id].done });
  },

  toggleStar(id) {
    this.modifyTodo(id, { important: !this.state.todos[id].important });
  },
  setTodoName(id, name) {
    this.modifyTodo(id, { name });
  },
  setTodoCategory(id, category) {
    this.modifyTodo(id, { categ: category });
  },
  setTodoDate(id, date) {
    // Date must be an ISO date in a string or null
    this.modifyTodo(id, { deadline: date });
  }
};

export { store };
