<template>
  <div>
    <v-btn :color="color" @click="trigger"><slot>Choose File</slot></v-btn>
    <input
      :multiple="multiple"
      class="visually-hidden"
      type="file"
      v-on:change="files"
      ref="fileInput"
    />
  </div>
</template>

<script>
export default {};
</script>

<style lang="stylus" scoped></style>
