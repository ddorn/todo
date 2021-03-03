<template>
  <div class="flex flex-col">
    <TodoAddBar
      @new-item="todos.push($event)"
      :categories="categories"
      :listid="listId"
      class="pb-4 w-1/2 mx-auto h-auto"
    ></TodoAddBar>

    <div class="w-full h-auto flex flex-shrink-0 space-x-4 border-b overflow-x-auto scrollbar-none">
      <div
        v-for="day in days"
        :key="day"
        class="pb-4 w-72 flex-shrink-0"
        @dragover.prevent
        @drop="dropDay($event, day)"
      >
        <h2 class="text-xl">{{ niceDate(day) }}</h2>
        <transition-group tag="ul" name="list" class="relative">
          <TodoItem
            v-for="item in todosByDay[day]"
            :key="item.id"
            :item="item"
            draggable="true"
            @dragstart="drag($event, item)"
          ></TodoItem>
        </transition-group>
      </div>
    </div>

    <div class="flex-grow flex-shrink pt-4 px-4 w-4/5 mx-auto overflow-y-scroll">
      <div class="col-w-md col-fill-balance">
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
                v-for="item in todosByCateg[category]"
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
  </div>
</template>

<script>
import { store } from "../store.js";
import TodoAddBar from "@/components/TodoAddBar";
import TodoItem from "@/components/TodoItem";
import {attributes, groupBy, cmpTodos, range, filterObject} from "../helper";
import { DateTime, Settings } from "luxon";
Settings.defaultLocale = "fr";

export default {
  name: "TodoBoard",
  components: { TodoItem, TodoAddBar },
  props: ["listId"],
  data() {
    return {
      firstDay: DateTime.now()
        .startOf("day")
        .minus({ days: 1 }),
      daysVisible: 10
    };
  },
  computed: {
    todos() {
      return store.state.todos;
    },
    todosByDay() {
      let groups = groupBy(
        "deadline",
        filterObject(this.todos, c => c.deadline !== null)
      );
      let ordered = {};
      for (const group in groups) {
        ordered[DateTime.fromISO(group)] = groups[group].sort(cmpTodos);
      }
      return ordered;
    },
    todosByCateg() {
      let groups = groupBy(
        "categ",
        filterObject(this.todos, c => c.deadline === null)
      );
      Object.values(groups).forEach(group => group.sort(cmpTodos));
      return groups;
    },
    days() {
      return range(this.daysVisible).map(d =>
          this.firstDay.startOf("day").plus({ days: d })
      );
    },
    categories() {
      return attributes("categ", this.todos);
    },
  },
  methods: {
    niceDate(date) {
      console.log(date)
      const str = date.toFormat("cccc dd MMMM")
      // Capitalise first letter of words
      return str.replace(/\w\S*/g, (w) => (w.replace(/^\w/, (c) => c.toUpperCase())));
    },
    drag(ev, todo) {
      ev.dataTransfer.setData("id", todo.id);
      ev.dataTransfer.dropEffect = "move";
    },
    drop(ev, category) {
      const id = ev.dataTransfer.getData("id");
      if (category !== this.todos[id].category) {
        store.setTodoCategory(id, category);
      }
    },
    dropDay(ev, day) {
      const id = ev.dataTransfer.getData("id");
      store.setTodoDate(id, day.toISODate());
    }
  }
};
</script>
