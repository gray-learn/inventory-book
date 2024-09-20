<template>
  <div id="app">
    <h1>Book Inventory Management System</h1>
    <BookForm @book-added="addBook" />
    <BookFilter @filter-applied="applyFilter" />
    <BookList :books="books" />
    <div class="export-buttons">
      <button @click="exportCSV">Export as CSV</button>
      <button @click="exportJSON">Export as JSON</button>
      <button @click="refresh">Refresh</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import BookForm from './components/BookForm.vue';
import BookList from './components/BookList.vue';
import BookFilter from './components/BookFilter.vue';
import { saveAs } from 'file-saver'; // Import file-saver
import { exportToCsv } from 'json-to-csv-export';

export default {
  name: 'App',
  components: {
    BookForm,
    BookList,
    BookFilter
  },
  data() {
      return {
        books: [],  // Store the books fetched from the backend
        fields: [
          { label: 'ID', key: 'id' },
          { label: 'Title', key: 'title' },
          { label: 'Author', key: 'author' },
          { label: 'Genre', key: 'genre' },
          { label: 'Publication Date', key: 'publication_date' },
          { label: 'ISBN', key: 'isbn' }
        ],
      };
  },
  computed: {
    formattedBooks() {
      // Format books for CSV download
      return this.books.map(book => ({
        id: book.id,
        title: book.title,
        author: book.author,
        genre: book.genre,
        publication_date: book.publication_date,
        isbn: book.isbn
      }));
    }
  },
  methods: {
    refresh() {
      this.fetchBooks();
    },
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
        const response = await axios.get('/books/filter/', { params: filter });
        this.books = response.data;
      } catch (error) {
        console.error('Error filtering books:', error);
      }
    },
    async exportJSON() {
      // Convert books array to a JSON string
      const jsonData = JSON.stringify(this.books, null, 2); // Pretty print with 2 spaces
      const blob = new Blob([jsonData], { type: 'application/json' });
      
      // Use FileSaver to save the file
      saveAs(blob, 'books_inventory.json');
    },
    async exportCSV() {
      try {
        // Fetch the latest books data from the backend
        const response = await axios.get('/api/books/'); // Ensure this URL matches your backend
        const books = response.data; // Get the books from the response

        // Customize the fields and file name for CSV export
        const dataToExport = books.map((book) => ({
          ID: book.id,
          Title: book.title,
          Author: book.author,
          Genre: book.genre,
          PublicationDate: book.publication_date,
          ISBN: book.isbn,
        }));

        exportToCsv({
          data: dataToExport,
          filename: 'books_inventory.csv',
          delimiter: ',',
        });
      } catch (error) {
        console.error('Error exporting CSV:', error);
      }
    },
    created() {
      console.log('fetchBooks called on load');
      this.fetchBooks(); // Fetch books on component load
    }
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