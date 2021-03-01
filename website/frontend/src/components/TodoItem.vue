<template>
  <li
    class="py-1 px-2 flex justify-between items-center bg-white shadow my-2 rounded-md"
    :class="{ 'text-gray-500 line-through': item.done }"
  >
    <button
      @click="toggleDone"
      class="rounded border-2 border-orange-200 w-6 h-6 mr-4"
      :class="{ 'text-gray-300': !item.done }"
    >
      { icon('check', "h-6 pb-1") }
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
    <button @click="toggleStar" class="w-6 h-6 flex-shrink-0 text-gray-300">
      <span
        v-if="item.important"
        :class="item.done ? 'text-gray-300' : 'text-orange-300'"
        >{ icon('star', "h-6 pb-1", True) }</span
      >
      <span v-else class="texor">{ icon('star', "h-6 pb-1", False) }</span>
    </button>
  </li>
</template>

<script>
export default {
  name: "TodoItem",
  props: ["item"],
  emits: ["error"],
  data() {
    return {
      editing: false,
      editedName: this.item.name,
      isOpen: false
    };
  },
  methods: {
    toggleDone() {
      this.$emit("toggle-done");
      // this.item.done = !this.item.done;
      // fetch(`/api/todo/${this.item.id}`, {
      //   method: "PATCH",
      //   body: JSON.stringify({ done: !this.item.done })
      // }).then(resp => {
      //   if (!resp.ok) {
      //     this.item.done = !this.item.done; // Toggle back on error
      //     this.$emit("error", `Could not mark "${this.item.name}" as done`);
      //   }
      // });
    },
    toggleStar() {
      this.$emit("toggle-star");
      // this.item.important = !this.item.important;
      // fetch(`/api/todo/${this.item.id}`, {
      //   method: "PATCH",
      //   body: JSON.stringify({ important: !this.item.important })
      // }).then(resp => {
      //   if (!resp.ok) {
      //     this.item.important = !this.item.important; // Toggle back on error
      //     this.$emit(
      //       "error",
      //       `Could not mark "${this.item.name}" as important`
      //     );
      //   }
      // });
    },
    toggleEdit() {
      this.editing = !this.editing;
      if (this.editing) setTimeout(() => this.$refs.input.focus(), 1);
    },
    edit() {
      this.$emit("set-name", this.editedName);
      this.editing = false;
      // fetch(`/api/todo/${this.item.id}`, {
      //   method: "PATCH",
      //   body: JSON.stringify({ name: this.editedName })
      // }).then(resp => {
      //   if (resp.ok) {
      //     this.item.name = this.editedName;
      //   }
      // });
    }
  }
};
</script>

<style scoped></style>
