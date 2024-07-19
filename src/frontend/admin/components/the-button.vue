<template>
  <button
    :class="[secondaryStyle ? 'secondaryButton' : 'primaryButton']"
    :style="[secondaryStyle && buttonStyle]"
  >
    <img v-if="icon" :src="icon" alt="Icon" />
    {{ text }}
  </button>
</template>

<script>
export default {
  name: "TheButton",
  props: {
    icon: {
      type: String,
    },
    text: {
      type: String,
    },
    secondaryStyle: {
      type: Boolean,
      default: false,
    },
    background: {
      type: String,
      default: "green",
    },
    type: {
      type: String,
      default: "button",
    },
  },
  computed: {
    buttonStyle() {
      if (this.background === "red") {
        return {
          background: "linear-gradient(to right, #C84767, #CB6F86)",
        };
      } else if (this.background === "green") {
        return {
          background: "linear-gradient(to right, #3A8A88, #57BD99)",
        };
      }
    },
  },
};
</script>

<style scoped lang="scss">
button {
  border-radius: 6px;
  padding: 18px 43px;
  display: flex;
  align-items: center;
  gap: 21px;
  width: 100%;
  font-size: 20px;
  justify-content: center;
  cursor: pointer;
  transition: background 0.3s ease;
}

.primaryButton {
  background-color: #365e54;
  color: #42988c;
  font-weight: 300;
}

.secondaryButton {
  color: white;
  font-weight: 300;
  .gradient-linear {
    background: linear-gradient(to bottom, #ff0000, #0000ff);
  }
}
</style>
