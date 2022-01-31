<template>
  <editor
    api-key="no-api-key"
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
}
</script>

<style>
  .tox.tox-tinymce {
    padding: 0;
  }
</style>