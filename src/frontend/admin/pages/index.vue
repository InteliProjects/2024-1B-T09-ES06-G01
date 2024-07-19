<template>
  <section>
    <h1>Projetos por macrotema</h1>
    <SwiperMacrotheme />
    <TheDivisor />
    <h1>Projetos pendentes</h1>
    <SwiperProjects :projects="inactiveProjects" />
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import SwiperMacrotheme from '~/components/swiper-macrothemes.vue';
import SwiperProjects from '~/components/swiper-projects.vue';
import TheDivisor from '~/components/the-divisor.vue';
import { useRuntimeConfig } from '#imports';

const inactiveProjects = ref([]);

const fetchInactiveProjects = async () => {
  try {
    const config = useRuntimeConfig();
    const response = await $fetch('projetos/inativos', {
      baseURL: config.public.baseURL
    });
    inactiveProjects.value = response;
  } catch (error) {
    console.error('Error fetching inactive projects:', error);
  }
};

onMounted(() => {
  fetchInactiveProjects();
});
</script>

<style scoped lang="scss">
section {
  padding: 0 60px 128px 60px;
  display: flex;
  flex-direction: column;
  gap: 16px;

  h1 {
    font-size: 24px;
    margin-bottom: 16px;
  }
}
</style>
