<template>
  <editor
    :api-key="tinymce_api_key"
    :init="{
      branding: false,
      height: 500,
      menubar: true,
      plugins: [
        'advlist autolink lists link image charmap print preview anchor',
        'searchreplace visualblocks code fullscreen',
        'insertdatetime media table paste code help wordcount'
      ],
      toolbar:
        'undo redo | formatselect | bold italic backcolor | \
        alignleft aligncenter alignright alignjustify | \
        bullist numlist outdent indent | removeformat'
    }"
  />
</template>

<script>
import Editor from '@tinymce/tinymce-vue'

export default {
  name: 'TinyMCE',
  components: {
    editor: Editor
  },
  data() {
    return {
      tinymce_api_key: process.env.VUE_APP_TINYMCE_API_KEY
    }
  }
}
</script>

<style>
  .tox.tox-tinymce {
    padding: 0;
  }
</style>