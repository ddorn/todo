<template>
  <div>
    <TodoAddBar
      @new-item="todos.push($event)"
      :categories="categories"
      :listid="listId"
      class="pb-4"
    ></TodoAddBar>

    <div class="col-w-lg w-full">
      <div v-for="(group, name) in shopByCateg" class="pb-4 inline-block w-full" :key="name">
        <h2 class="text-xl">{{ name }}</h2>
        <transition-group tag="ul" name="flip-list">
          <TodoItem
            v-for="item in group"
            :item="item"
            :key="item.id"
            @error="console.log(event)"
          ></TodoItem>
        </transition-group>
      </div>
    </div>
  </div>
</template>

<script>
import { store } from "../store.js";
import TodoAddBar from "@/components/TodoAddBar";
import TodoItem from "@/components/TodoItem";

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
      let groups = {};
      Object.values(this.todos).forEach(item => {
        if (item.categ in groups) {
          groups[item.categ].push(item);
        } else {
          groups[item.categ] = [item];
        }
      });
      for (const group in groups) {
        groups[group].sort((a, b) => {
          let ddone = a.done - b.done,
            dimportant = b.important - a.important;
          return ddone !== 0 ? ddone : dimportant !== 0 ? dimportant : a.name.localeCompare(b.name);
        });
      }
      return groups;
    },
    categories() {
      return new Set(Object.values(this.todos).map(item => item.categ));
    }
  },
  methods: {}
};
</script>
