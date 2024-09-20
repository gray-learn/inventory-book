<template>
  <div id="app">
    <h1>Book Inventory Management System</h1>
    <BookForm @book-added="addBook" />
    <BookFilter @filter-applied="applyFilter" />
    <BookList :books="books" />
    <div class="export-buttons">
      <button @click="exportData('csv')">Export as CSV</button>
      <button @click="exportData('json')">Export as JSON</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import BookForm from './components/BookForm.vue';
import BookList from './components/BookList.vue';
import BookFilter from './components/BookFilter.vue';

export default {
  name: 'App',
  components: {
    BookForm,
    BookList,
    BookFilter
  },
  data() {
    return {
      books: []
    };
  },
  methods: {
    async fetchBooks() {
      try {
        const response = await axios.get('/api/books/');
        this.books = response.data;
      } catch (error) {
        console.error('Error fetching books:', error);
      }
    },
    addBook(book) {
      this.books.push(book);
    },
    async applyFilter(filter) {
      try {
        const response = await axios.get('/api/books/filter/', { params: filter });
        this.books = response.data;
      } catch (error) {
        console.error('Error filtering books:', error);
      }
    },
    exportData(format) {
      window.location.href = `/api/books/export/?format=${format}`;
    }
  },
  mounted() {
    this.fetchBooks();
  }
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5e1d2; /* Light brown background */
  border: 2px solid #8b5a2b; /* Dark brown border */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

h1 {
  color: #8b4513; /* SaddleBrown for header */
  text-align: center;
  font-family: 'Georgia', serif;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.2);
}

form div {
  margin-bottom: 10px;
}

label {
  display: inline-block;
  width: 120px;
  font-weight: bold;
  color: #8b4513; /* Dark brown for labels */
}

input {
  width: 200px;
  border: 1px solid #8b5a2b; /* Dark brown border */
  padding: 5px;
  border-radius: 4px;
  background-color: #f3e5d3; /* Lighter brown for inputs */
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  background-color: #e6ccb3; /* Light wood-like brown */
}

th, td {
  border: 1px solid #8b5a2b; /* Dark brown borders */
  padding: 8px;
  text-align: left;
  color: #3e2723; /* Dark brown text */
}

th {
  background-color: #a0522d; /* Dark brown for table headers */
  color: white;
}

.export-buttons {
  margin-top: 20px;
}

button {
  background-color: #8b5a2b; /* Dark brown button background */
  color: white;
  border: none;
  padding: 10px 15px;
  margin-right: 10px;
  cursor: pointer;
  border-radius: 5px;
  font-weight: bold;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #a0522d; /* Slightly lighter brown on hover */
}
</style>