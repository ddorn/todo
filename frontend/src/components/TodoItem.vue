<template>
  <div
    class="py-1 px-2 flex  items-center bg-white shadow rounded-md"
    :class="{ 'text-gray-500': item.done }"
  >
    <button
      @click="toggleDone"
      class="flex rounded border-2 border-orange-200 w-6 h-6 mr-2"
      :class="{ 'text-gray-300': !item.done }"
    >
      <Icon name="check" class="h-6 pb-0.5"></Icon>
    </button>
    <div class="flex-grow relative leading-tight mr-1">
      <div v-if="showCateg" class="text-xs -mt-1 text-gray-400">{{ item.categ }}</div>
<!--      <span class="" :class="{ 'line-through': this.item.done }">{{ item.name }}</span>-->
      <div class="justify-self-start">
        <input
            v-if="editing"
            ref="input"
            class="text-gray-600 w-full"
            v-model="editedName"
            @change="edit"
            @focusout="editing = false"
            type="text"
        />
        <div v-else :class="{ 'line-through': this.item.done }"
             @click="toggleEdit" class="">{{ item.name }}</div>
    </div>
    </div>
    <button @click="toggleStar" class="flex w-6 h-6 flex-shrink-0 text-gray-300">
      <Icon
          v-if="item.important"
          :class="item.done ? 'text-gray-300' : 'text-orange-300'"
          name="star"
          class="h-6"
          fill="currentColor"
      ></Icon>
      <Icon v-else name="star" class="h-6"></Icon>
    </button>
  </div>
</template>

<script>
import { store } from "../store.js";
import Icon from "@/components/Icon";

export default {
  name: "TodoItem",
  components: { Icon },
  props: {
    "item": Object,
    "show-categ": {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      editing: false,
      editedName: this.item.name,
      isOpen: false
    };
  },
  methods: {
    toggleDone() {
      store.toggleDone(this.item.id);
    },
    toggleStar() {
      store.toggleStar(this.item.id);
    },
    toggleEdit() {
      this.editing = !this.editing;
      if (this.editing) setTimeout(() => this.$refs.input.focus(), 1);
    },
    edit() {
      store.setTodoName(this.item.id, this.editedName);
      this.editing = false;
    }
  }
};
</script>

<style scoped></style>
