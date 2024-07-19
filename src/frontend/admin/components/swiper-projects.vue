<template>
  <div>
    <Swiper
      :modules="[SwiperNavigation]"
      class="swiper-projects"
      :slides-per-view="1"
      :space-between="10"
      :breakpoints="{
        640: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 30,
        },
        1024: {
          slidesPerView: 3,
          spaceBetween: 40,
        },
        1640: {
          slidesPerView: 4,
          spaceBetween: 40,
        }
      }"
      navigation
    >
      <SwiperSlide v-for="slide in projects" :key="slide.id">
        <CardProject :slide="slide" />
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/swiper-bundle.css';
import CardProject from '~/components/card-project.vue';

const props = defineProps({
  projects: {
    type: Array,
    required: true
  }
});
</script>

<style scoped>
.swiper-container {
  width: 100%;
  overflow: hidden;
  position: relative;
}

.swiper-wrapper {
  display: flex;
}

.swiper-slide {
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-container:hover .swiper-button-next-projects, 
.swiper-container:hover .swiper-button-prev-projects {
  opacity: 1;
}
</style>
