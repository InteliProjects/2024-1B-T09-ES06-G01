<template>
  <section class="user" @click="$emit('click')">
    <div class="user-info">
      <img :src="user.foto" :alt="user.nome" />
      <div>
        <h1>{{ user.nome }}</h1>
        <p>{{ user.empresa_nome }}</p>
      </div>
    </div>
    <div class="user-actions" @click.stop="emitDelete">
      <button>
        <img src="/delete.svg" alt="Deletar CEO" title="Deletar CEO" />
      </button>
    </div>
  </section>
  <TheDivisor color="#4B6C63" />
</template>

<script>
import TheDivisor from '~/components/the-divisor.vue';

export default {
  props: {
    user: {
      type: Object,
      required: true
    }
  },
  emits: ['click', 'delete'],
  components: {
    TheDivisor
  },
  methods: {
    emitDelete() {
      this.$emit('delete', this.user.id);
    }
  }
}

</script>

<style scoped lang="scss">

.user {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
  cursor: pointer;

  &-info {
    display: flex;
    align-items: center;
    justify-content: center;

    img {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      margin-right: 16px;
    }

    h1 {
      font-size: 24px;
      margin-bottom: 8px;
      font-weight: 500;
    }

    p {
      font-size: 20px;
      color: #4B6C63;
    }
  }

  &-actions {
    img {
      width: 32px;
    }
  }
}
</style>