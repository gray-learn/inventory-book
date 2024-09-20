import { shallowMount } from '@vue/test-utils'
import BookList from '@/components/BookList.vue'

describe('BookList.vue', () => {
  it('renders books when passed', () => {
    const books = [
      { id: 1, title: 'Book 1', author: 'Author 1' },
      { id: 2, title: 'Book 2', author: 'Author 2' }
    ]
    const wrapper = shallowMount(BookList, {
      propsData: { books }
    })
    expect(wrapper.findAll('tr').length).toBe(books.length + 1) // +1 for header row
  })
})