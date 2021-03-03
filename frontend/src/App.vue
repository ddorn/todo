<template>
  <div class="h-screen w-screen bg-gray-50 text-black flex flex-col items-center overflow-x-hidden">
    <nav class="z-50 flex items-center p-4 text-2xl bg-orange-500 shadow-lg mb-6 fixed left-0 right-0 w-full overflow-hidden">
      <div
        :class="{
          'hover:underline md:hover:translate-x-20 md:transform md:transition md:relative md:-left-20 md:px-10':
            listId !== null
        }"
      >
        <button
          @click="setListId(null)"
          class="flex items-center hover:opacity-100 focus:outline-none"
        >
          <Icon v-if="listId !== null" name="left-arrow" class="pr-2 md:pr-4 h-6 text-gray-700">
          </Icon>
          <span class="">{{ title }}</span>
        </button>
      </div>
      <div class="flex-grow"></div>
      <button @click="calendarView = !calendarView" class="hover:scale-110 transform">
        <Icon v-if="!calendarView" name="calendar" class="h-8"></Icon>
        <Icon v-else name="board" class="h-8"></Icon>
      </button>
    </nav>

<!--    Size of the top bar : 5rem -> 20 units. -->

    <div v-if="listId === null" class="pt-20 w-full h-full flex flex-col md:w-1/2">
      <div class="flex flex-col space-y-4 px-4 self-center">
        <a
          @click="setListId(list.id)"
          v-for="list in lists"
          :key="list.id"
          class="cursor-pointer p-4 w-full rounded-xl shadow-lg bg-orange-100 hover:scale-105 transform transition"
        >
          <div class="text-xl px-4">{{ list.title }}</div>
          <p class="px-4 text-gray-700">{{ list.description }}</p>
        </a>
      </div>
    </div>

    <todo-board v-else-if="calendarView" :list-id="listId" class="pt-20 h-full flex-grow w-full flex-shrink"></todo-board>
    <todo-list v-else :list-id="listId" class="pt-20 h-full md:w-4/5 w-full p-4"></todo-list>
  </div>
</template>

<script>
import { store } from "./store.js";
import Icon from "@/components/Icon";
import TodoBoard from "./components/TodoBoard";
import TodoList from "./components/TodoList.vue";

import "./assets/index.css";

export default {
  name: "App",
  components: {
    Icon,
    TodoList,
    TodoBoard
  },
  data() {
    return {
      calendarView: true,
      state: store.state
    };
  },
  computed: {
    lists() {
      return store.state.lists;
    },
    listId() {
      return store.state.listId;
    },
    title() {
      return this.listId === null ? "Listes de Diego" : store.getList().title;
    }
  },
  methods: {
    setListId(value) {
      store.setListId(value);
      document.title = this.title;
    }
  },
  created() {
    store.fetchLists();
  }
};
</script>

<style></style>
