<template>
  <div class="book-filter">
    <h2>Filter Books</h2>
    <form @submit.prevent="submitFilter">
      <div>
        <label for="filterTitle">Title:</label>
        <input id="filterTitle" v-model="filter.title">
      </div>
      <div>
        <label for="filterAuthor">Author:</label>
        <input id="filterAuthor" v-model="filter.author">
      </div>
      <div>
        <label for="filterGenre">Genre:</label>
        <input id="filterGenre" v-model="filter.genre">
      </div>
      <button type="submit">Apply Filter</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'BookFilter',
  data() {
    return {
      filter: {
        title: '',
        author: '',
        genre: ''
      }
    };
  },
  methods: {
    submitFilter() {
      this.$emit('filter-applied', this.filter);
    }
  }
};
</script>