<template>
  <div class="divider" :style="{ backgroundColor: color }"></div>
</template>

<script>
// recebe a cor como propriedade
export default {
  props: {
    color: {
      type: String,
      default: '#4B6C63'
    }
  }
}

</script>

<style scoped>
.divider {
  width: 100%;
  height: 1px;
  margin: 0 auto;
}
</style>