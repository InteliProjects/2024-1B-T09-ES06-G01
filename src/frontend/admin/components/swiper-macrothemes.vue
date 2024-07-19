<template>
  <div>
    <Swiper
      :modules="[SwiperNavigation]"
      class="swiper-macrotheme"
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
          slidesPerView: 4,
          spaceBetween: 40,
        },
      }"
      navigation
    >
      <SwiperSlide
        v-for="slide in slides"
        :key="slide.id"
        @click="navigate(slide.nome)"
      >
        <img :src="slide.image" alt="Slide" />
        <div class="slide-text">{{ slide.texto }}</div>
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/swiper-bundle.css";
import { Navigation } from "swiper/modules";
export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      slides: [
        {
          id: 1,
          image: "/bem-estar.png",
          texto: "Bem-Estar, Saúde e Felicidade",
          nome: "bem-estar",
        },
        {
          id: 2,
          image: "/produtividade.png",
          texto: "Produtividade e Competitividade",
          nome: "produtividade",
        },
        {
          id: 3,
          image: "/reducao.png",
          texto: "Redução do Impacto Ambiental",
          nome: "redução",
        },
        {
          id: 4,
          image: "/diversidade.png",
          texto: "Diversidade e Inclusão",
          nome: "diversidade",
        },
        {
          id: 5,
          image: "/integridade.png",
          texto: "Integridade e Práticas Éticas",
          nome: "integridade",
        },
        {
          id: 6,
          image: "/conservacao.png",
          texto: "Conservação do Planeta",
          nome: "conservação",
        },
      ],
    };
  },
  methods: {
    navigate(nome) {
      this.$router.push(`/macrotheme/${nome}`);
    },
  },
};
</script>

<style scoped>
.swiper-container {
  width: 100%;
  height: 136.7px;
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
  position: relative;
  cursor: pointer;
}

.swiper-slide img {
  width: 100%;
}

.slide-text {
  position: absolute;
  top: 50%;
  left: 20%;
  transform: translate(-20%, -20%);
  font-size: 18px;
  font-weight: 600;
  color: white;
}

.swiper-container:hover .swiper-button-next,
.swiper-container:hover .swiper-button-prev {
  opacity: 1;
}
</style>
