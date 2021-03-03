<template>
  <div class="flex flex-col">
    <TodoAddBar
      @new-item="todos.push($event)"
      :categories="categories"
      :listid="listId"
      class="pb-4 w-1/2 mx-auto h-auto"
    ></TodoAddBar>

    <div ref="calendar" class="w-full h-auto pb-4 flex flex-shrink-0 border-b overflow-x-auto scrollbar-none">
      <button class="flex flex-col items-center justify-center w-72 flex-shrink-0 bg-gray-100 mx-2 rounded-md shadow shadow-inner">
        <Icon name="left-arrow" class="h-16"></Icon>
        Voir les jours précédents
      </button>

      <div
        v-for="day in days"
        :key="day"
        class="p-2 w-72 flex-shrink-0 mx-2 bg-white rounded-lg shadow bg-orange-50"
        @dragover.prevent
        @drop="dropDay($event, day)"
      >
        <h2 class="text-xl text-center underline py-2 mb-2">{{ niceDate(day) }}</h2>
        <transition-group tag="ul" name="list" class="relative flex flex-col space-y-1">
          <TodoItem
            v-for="item in todosByDay[day]"
            :key="item.id"
            :item="item"
            show-categ="true"
            draggable="true"
            @dragstart="drag($event, item)"
          ></TodoItem>
        </transition-group>
      </div>
    </div>

    <div class="flex-grow flex-shrink pt-4 px-4 w-4/5 mx-auto overflow-y-auto">
      <div class="col-w-md col-fill-balance">
        <div
            v-for="category in categories"
            :key="category"
            class="pb-4 inline-block w-full border-b mb-2"
            @dragover.prevent
            @drop="drop($event, category)"
        >
          <h2 class="text-xl pb-2">{{ category }}</h2>
          <transition-group tag="ul" name="list" class="flex flex-col space-y-1 relative">
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
import {store} from "../store.js";
import TodoAddBar from "@/components/TodoAddBar";
import TodoItem from "@/components/TodoItem";
import Icon from "@/components/Icon";
import {attributes, cmpTodos, filterObject, groupBy, range} from "../helper";
import {DateTime, Settings} from "luxon";

Settings.defaultLocale = "fr";

export default {
  name: "TodoBoard",
  components: { TodoItem, TodoAddBar, Icon },
  props: ["listId"],
  data() {
    return {
      firstDay: DateTime.now()
        .startOf("week"),
      daysVisible: 14
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
  },
  mounted() {
    // Scroll so that today is the left-most block
    const cal = this.$refs.calendar,
          child = cal.children[0],
          box = getComputedStyle(child),
          width = child.offsetWidth + parseInt(box.marginLeft) + parseInt(box.marginRight);

    cal.scrollLeft = width * -this.firstDay.diffNow("day").days;
  }
};
</script>
