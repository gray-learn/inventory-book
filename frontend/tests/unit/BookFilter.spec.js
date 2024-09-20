import { shallowMount } from '@vue/test-utils'
import BookFilter from '@/components/BookFilter.vue'

describe('BookFilter.vue', () => {
  it('emits filter-books event when form is submitted', async () => {
    const wrapper = shallowMount(BookFilter)
    const form = wrapper.find('form')
    await form.trigger('submit.prevent')
    expect(wrapper.emitted('filter-books')).toBeTruthy()
  })
})