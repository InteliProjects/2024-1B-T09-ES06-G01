<template>
  <div class="subtheme-div">
    <img :src="macrothemeIcon" :alt="'Macrotheme icon to' + macrothemeIcon" />
    <p>{{ subtheme }}</p>
  </div>
</template>

<script>
export default {
  name: "ThePageBack",
  props: {
    macrothemeIcon: {
      type: String,
      required: true,
    },
    subtheme: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped lang="scss">
.subtheme-div {
    display: flex;
    gap: 19px;
    align-items: center;

    p {
        color: white;
        font-size: 24px;
        font-weight: 600;
    }

}
</style>
