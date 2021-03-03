<template>
  <div>
    <TodoAddBar
      @new-item="todos.push($event)"
      :categories="categories"
      :listid="listId"
      class="pb-4"
    ></TodoAddBar>

    <div class="col-w-lg w-full">
      <div
        v-for="category in categories"
        :key="category"
        class="pb-4 inline-block w-full"
        @dragover.prevent
        @drop="drop($event, category)"
      >
        <h2 class="text-xl">{{ category }}</h2>
        <transition-group tag="ul" name="list" class="relative">
          <TodoItem
            v-for="item in shopByCateg[category]"
            :item="item"
            :key="item.id"
            draggable="true"
            @dragstart="drag($event, item)"
          >
          </TodoItem>
        </transition-group>
      </div>
    </div>
  </div>
</template>

<script>
import { store } from "../store.js";
import TodoAddBar from "@/components/TodoAddBar";
import TodoItem from "@/components/TodoItem";
import { attributes, groupBy, cmpTodos } from "../helper";

export default {
  name: "TodoList",
  components: { TodoItem, TodoAddBar },
  props: ["listId"],
  data() {
    return {};
  },
  computed: {
    todos() {
      return store.state.todos;
    },
    shopByCateg() {
      let groups = groupBy("categ", this.todos);
      Object.values(groups).forEach(group => group.sort(cmpTodos));
      return groups;
    },
    categories() {
      return attributes('categ', this.todos);
    }
  },
  methods: {
    drag(ev, todo) {
      ev.dataTransfer.setData("id", todo.id);
      ev.dataTransfer.dropEffect = "move";
    },
    drop(ev, category) {
      const id = ev.dataTransfer.getData("id");
      if (category !== this.todos[id].category) {
        store.setTodoCategory(id, category);
      }
    }
  }
};
</script>
