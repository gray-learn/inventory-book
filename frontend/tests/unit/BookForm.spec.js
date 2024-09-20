import { shallowMount } from '@vue/test-utils'
import BookForm from '@/components/BookForm.vue'

describe('BookForm.vue', () => {
  it('emits add-book event when form is submitted', async () => {
    const wrapper = shallowMount(BookForm)
    const form = wrapper.find('form')
    await form.trigger('submit.prevent')
    expect(wrapper.emitted('add-book')).toBeTruthy()
  })
})