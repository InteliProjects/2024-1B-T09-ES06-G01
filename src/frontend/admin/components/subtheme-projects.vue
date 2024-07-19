<template>
  <h1>{{ subtheme }}</h1>
  <SwiperProjects :projects="projects" />
</template>

<script>
import SwiperProjects from "~/components/swiper-projects.vue";

export default {
  name: "SubthemeProjects",
  components: {
    SwiperProjects,
  },
  props: {
    subtheme: {
      type: String,
      required: true,
    },
    projects: {
      required: true,
    },
  },
};
</script>

<style scoped lang="scss">
h1 {
  color: white;
  margin-bottom: 26px;
  font-size: 24px;
}
</style>
