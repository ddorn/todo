<template>
  <div class="bg-gray-50 text-black relative flex flex-col min-h-screen min-w-screen items-center">
    <nav class="flex p-4 text-2xl bg-orange-500 shadow-lg mb-6 fixed w-full overflow-hidden">
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
          <span @click="updateLists()" class="">{{ title }}</span>
        </button>
      </div>
    </nav>

    <!-- Same size as the top bar -->
    <div class="mb-4 text-2xl p-4">42</div>

    <div v-if="listId === null" class="p-4 w-full h-full flex flex-col md:w-1/2">
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

    <todo-list v-else :list-id="listId" class="md:w-4/5 w-full p-4"></todo-list>
  </div>
</template>

<script>
import { store } from "./store.js";
import TodoList from "./components/TodoList.vue";
import Icon from "@/components/Icon";

import "./assets/index.css";

export default {
  name: "App",
  components: {
    Icon,
    TodoList
  },
  data() {
    return {
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
      return this.listId === null ? "Listes de Diego" : this.lists[this.listId].title;
    }
  },
  methods: {
    setListId(value) {
      store.setListId(value);
      if (value !== null) {
        document.title = this.lists.find(l => l.id === value).title;
      } else {
        document.title = "Listes de Diego";
      }
    }
  },
  created() {
    store.fetchLists();
  }
};
</script>

<style></style>
