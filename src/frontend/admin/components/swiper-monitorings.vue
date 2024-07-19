<template>
  <div>
    <Swiper
      :modules="[SwiperNavigation]"
      class="swiper-monitorings"
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
        },
      }"
      navigation
    >
      <SwiperSlide v-for="(slide, index) in monitorings" :key="index">
        <MonitoringCard :content="slide" />
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<script setup>
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/swiper-bundle.css";
import MonitoringCard from "~/components/monitoring-card.vue";

const props = defineProps({
  monitorings: {
    type: Array,
    required: true,
  },
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

.swiper-container:hover .swiper-button-next-monitorings,
.swiper-container:hover .swiper-button-prev-monitorings {
  opacity: 1;
}
</style>
