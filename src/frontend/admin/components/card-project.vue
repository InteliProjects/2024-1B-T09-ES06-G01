<template>
  <article class="card">
    <header class="card-header">
      <div class="card-header-info">
        <img :src="slide.ceos[0].foto" alt="Foto do CEO dono do projeto" />
        <div class="card-header-info-nome">
          <p>{{ slide.ceos[0].nome }}</p>
          <span>{{ slide.ceos[0].empresa_nome }}</span>
        </div>
      </div>
      <div class="card-header-macrotema">
        <img :src="macrotemaIconSrc" alt="Ícone do macrotema" />
        <span>{{ slide.subtema_nome }}</span>
      </div>
    </header>
    <div class="card-body">
      <h3 :title="slide.nome">{{ slide.nome }}</h3>
      <TheButton text="Ver mais" secondaryStyle @click="goToDetails(slide.id)" />
    </div>
  </article>
</template>

<script>
import TheButton from '~/components/the-button.vue';

export default {
  props: {
    slide: {
      type: Object,
      required: true
    }
  },
  components: {
    TheButton
  },
  methods: {
    goToDetails(id) {
      this.$router.push(`/detail/${id}`);
    }
  },
  computed: {
    macrotemaIconSrc() {
      return `/${this.slide.macrotema_nome}.svg`;
    }
  }
}
</script>

<style scoped lang="scss">
.card {
  width: 100%;
  max-width: 432px;
  border-radius: 6px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
  background-color: #334C45;
  padding: 10px 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 16px;

  &-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px;
    flex-direction: row;
    padding-bottom: 0;

    img {
      width: 40px;
      height: 40px;
      border-radius: 100%;
    }

    &-info {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0;

      &-nome {
        margin-left: 10px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 30px;

        p, span {
          font-size: 14px;
          color: #FFFFF0;
          margin: 0;
          padding: 0;
        }

        span {
          font-size: 10px;
        }
      }
    }

    img:last-child {
      width: 30px;
      height: 30px;
    }

    h4 {
      font-size: 14px;
      color: #666;
    }

    &-macrotema {
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
      flex-direction: row;

      img {
        width: 18px;
        height: 18px;
      }

      span {
        font-size: 12px;
        margin-left: 10px;
        color: #fff !important;
      }
    }
  }

  &-body {
    padding: 16px;
    padding-top: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;

    h3 {
      font-size: 18px;
      margin-bottom: 16px;
      color: #FFFFF0;
      font-weight: 400;
      line-height: 22px;
      max-height: 44px;
      overflow: hidden;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-line-clamp: 1;
      -webkit-box-orient: vertical;
    }

    a {
      display: inline-block;
      font-size: 14px;
      color: #4B6C63;
      text-decoration: none;
      transition: color 0.3s;

      &:hover {
        color: #2E4D43;
      }
    }
  }
}
</style>
