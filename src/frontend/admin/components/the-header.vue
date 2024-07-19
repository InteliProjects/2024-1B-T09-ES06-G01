<template>
  <header class="header">
    <div class="header-content">
      <img src="/coffeebreak.svg" alt="Logo" />
      <div class="header-content__actions">
        <nuxt-link to="/">
          <img src="/home.svg" alt="Home" />
        </nuxt-link>
        <nuxt-link to="/users">
          <img src="/user.svg" alt="User" />
        </nuxt-link>
        <nuxt-link to="/dash">
          <img src="/dash.svg" alt="Dashboard" />
        </nuxt-link>
      </div>
    </div>
    <TheDivisor color="#989898" />
  </header>
</template>

<script>
import TheDivisor from '~/components/the-divisor.vue';

export default {
  name: 'the-header',
  components: {
    TheDivisor
  }
}
</script>

<style scoped lang="scss">
@use '~/assets/css/variables.scss' as v;

.header {
  background-color: v.$primary-color;
  width: 100%;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  padding: 60px 60px 32px 60px;

  &-content {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 32px;
  
    img {
      width: 214px;
    }

    div {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 200px;
      flex-wrap: wrap;
    }

  }

  a {
    img {
      width: 32px;
      margin-left: 16px;
    }
  }
}
</style>