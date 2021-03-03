<template>
  <li
    class="py-1 px-2 flex justify-between items-center bg-white shadow rounded-md"
    :class="{ 'text-gray-500 line-through': item.done }"
  >
    <button
      @click="toggleDone"
      class="flex rounded border-2 border-orange-200 w-6 h-6 mr-4"
      :class="{ 'text-gray-300': !item.done }"
    >
      <Icon name="check" class="h-6"></Icon>
    </button>
    <span class="justify-self-start flex-grow overflow-ellipsis">
      <input
        v-if="editing"
        ref="input"
        class="pr-1 text-gray-600"
        v-model="editedName"
        @change="edit"
        @focusout="editing = false"
        :size="Math.min(27, editedName.length)"
        type="text"
      />
      <span v-else @click="toggleEdit" class="h-6">{{ item.name }}</span>
    </span>
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
  </li>
</template>

<script>
import { store } from "../store.js";
import Icon from "@/components/Icon";

export default {
  name: "TodoItem",
  components: { Icon },
  props: ["item"],
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
      // this.$emit("toggle-done");
    },
    toggleStar() {
      store.toggleStar(this.item.id);
    },
    toggleEdit() {
      this.editing = !this.editing;
      if (this.editing) setTimeout(() => this.$refs.input.focus(), 1);
    },
    edit() {
      store.setTodoName(this.editedName);
      this.editing = false;
    }
  }
};
</script>

<style scoped></style>
