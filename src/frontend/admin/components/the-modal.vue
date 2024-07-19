<template>
  <div v-if="isOpen" class="modal-overlay" @click="close">
    <div class="modal-content" @click.stop>
      <button class="close-button" @click="close">
        <img src="/close.svg" alt="Close button" />
      </button>
      <div class="modal-body">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isOpen: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    close() {
      this.$emit('close');
    }
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: #334C45;
  padding: 48px 128px;
  border-radius: 8px;
  position: relative;
  max-width: 1000px;
  max-height: 94vh;
  overflow: hidden;
}

.close-button {
  position: absolute;
  top: 32px;
  right: 32px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.modal-body {
  max-height: 80vh;
  overflow-y: auto;
  padding: 16px;
}
</style>
