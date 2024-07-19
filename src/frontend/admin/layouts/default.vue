<template>
  <TheHeader />
  <slot></slot>
</template>

<script>
import TheHeader from '~/components/the-header.vue';

export default {
  components: {
    TheHeader
  },
};
</script>
