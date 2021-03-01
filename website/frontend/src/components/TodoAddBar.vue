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
      <option v-for="cat in categories" :value="cat" :key="cat">{{
        cat
      }}</option>
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
      <button
        type="submit"
        class="rounded-r bg-orange-300 text-center"
        v-on:click="addItem"
      >
        { icon('plus', 'h-7 px-2 py-1') }
      </button>
    </div>
  </form>
</template>

<script>
export default {
  name: "TodoAddBar",
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
      if (!cat || !name) return;
      let item = { name, categ: cat, done: false };
      fetch(`/api/list/${this.listid}`, {
        method: "post",
        body: JSON.stringify(item)
      }).then(resp =>
        resp.json().then(data => {
          item = data;
          this.$emit("new-item", item);
          this.addName = "";
        })
      );
      if (isNewCat) {
        this.addCateg = this.addCategAutre;
      }
    }
  }
};
</script>

<style></style>
