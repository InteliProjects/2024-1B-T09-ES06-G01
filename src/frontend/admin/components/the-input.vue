<template>
  <div class="input-div">
    <img v-if="icon" :src="icon" alt="Icon" />
    <input
      :type="type"
      :placeholder="placeholder"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    />
  </div>
</template>

<script>
export default {
  name: "TheInput",
  props: {
    icon: {
      type: String,
      required: false,
    },
    placeholder: {
      type: String,
      required: true,
    },
    modelValue: {
      type: String,
      required: true,
    },
    type: {
      type: String,
      required: false,
      default: "text",
    },
  },
};
</script>

<style scoped lang="scss">
.input-div {
  border: 2px solid #42988c;
  border-radius: 6px;
  position: relative;
  display: flex;
  align-items: center;
  padding: 18px 43px;
  gap: 21px;

  img {
    width: 19px;
    height: 19px;
  }

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
    color: #42988c;
    font-size: 20px;
    font-weight: 300;
  }
}
</style>
