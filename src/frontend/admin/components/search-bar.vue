<template>
  <div class="search-bar">
    <input type="text" v-model="query" @input="onInput" placeholder="Pesquisar usuários..." />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  }
});

const emit = defineEmits(['update:modelValue']);

const query = ref(props.modelValue);

const onInput = () => {
  emit('update:modelValue', query.value);
};

watch(() => props.modelValue, (newQuery) => {
  query.value = newQuery;
});
</script>

<style scoped lang="scss">
.search-bar {
  border: 2px solid #42988C;
  border-radius: 6px;
  position: relative;
  display: flex;
  align-items: center;
  padding: 18px;
  gap: 21px;
  margin-bottom: 32px;
  width: 30%;
  margin-right: auto;

  input {
    width: 100%;
    height: 100%;
    background: none;
    outline: none;
    border: none;
    color: white;
    font-size: 20px;
  }

  input::placeholder {
    color: #42988C;
    font-size: 20px;
    font-weight: 300;
  }
}
</style>
