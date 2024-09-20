<template>
  <div class="book-form">
    <h2>Add New Book</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="title">Title:</label>
        <input id="title" v-model="book.title" required>
      </div>
      <div>
        <label for="author">Author:</label>
        <input id="author" v-model="book.author" required>
      </div>
      <div>
        <label for="genre">Genre:</label>
        <input id="genre" v-model="book.genre" required>
      </div>
      <div>
        <label for="publication_date">Publication Date:</label>
        <input id="publication_date" type="date" v-model="book.publication_date" required>
      </div>
      <div>
        <label for="isbn">ISBN:</label>
        <input id="isbn" v-model="book.isbn" required>
      </div>
      <button type="submit">Add Book</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'BookForm',
  data() {
    return {
      book: {
        title: '',
        author: '',
        genre: '',
        publication_date: '',
        isbn: ''
      }
    };
  },
  methods: {
    async submitForm() {
      try {
        console.log(this.book)
        const response = await axios.post('/api/books/', this.book);
        this.$emit('book-added', response.data);
        this.resetForm();
      } catch (error) {
        console.error('Error adding book:', error);
      }
    },
    resetForm() {
      this.book = {
        title: '',
        author: '',
        genre: '',
        publication_date: '',
        isbn: ''
      };
    }
  }
};
</script>