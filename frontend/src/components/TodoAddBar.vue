<template>
  <form
    :onsubmit="addItem"
    class="flex items-center flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-2"
  >
    <select
      ref="catSelect"
      class="px-1 flex-grow w-full border md:w-min h-8"
      id="category-select"
      name="category"
      v-model="addCateg"
    >
      <option value="" disabled selected hidden>Category</option>
      <option v-for="cat in categories" :value="cat" :key="cat">
        {{ cat }}
      </option>
      <option value="-OTHER-">Nouvelle catégorie</option>
    </select>

    <input
      class="border w-full h-8 flex-grow px-2"
      placeholder="Nouvelle catégorie..."
      id="category-select"
      v-if="addCateg === '-OTHER-'"
      v-model="addCategAutre"
      type="text"
    />

    <div class="flex flex-grow w-full">
      <div class="flex w-full h-8">
        <input type="text" class="flex-grow border px-2" v-model="addName" />
      </div>
      <button type="submit" class="rounded-r bg-orange-300 text-center" v-on:click="addItem">
        <Icon name="plus" class="h-7 px-2 py-1"></Icon>
      </button>
    </div>
  </form>
</template>

<script>
import Icon from "@/components/Icon";
import { store } from "../store";
export default {
  name: "TodoAddBar",
  components: { Icon },
  props: ["categories", "listid"],
  emits: ["new-item"],
  data() {
    return {
      addCateg: "",
      addName: "",
      addCategAutre: ""
    };
  },
  methods: {
    addItem(event) {
      if (event) event.preventDefault(); // Don't submit the form and change page
      let isNewCat = this.addCateg === "-OTHER-";
      let cat = isNewCat ? this.addCategAutre : this.addCateg;
      let name = this.addName;
      this.addName = "";
      if (!cat || !name) return;
      store.createTodo(name, cat);
      if (isNewCat) {
        this.addCateg = this.addCategAutre;
      }
    }
  }
};
</script>

<style></style>
