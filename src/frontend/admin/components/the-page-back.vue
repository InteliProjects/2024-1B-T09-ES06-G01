<template>
  <div class="page-back">
    <button @click="goBack">
      <img src="/back.png" alt="Back button" />
    </button>
    <h1>{{ page }}</h1>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
const router = useRouter()

export default {
  name: "ThePageBack",
  props: {
    page: {
      type: String,
      required: true,
    },
    route: {
      type: String,
    },
  },
  setup() {
    const router = useRouter();

    const goBack = () => {
      router.back();
    };

    return {
      goBack
    };
  }
};
</script>

<style scoped lang="scss">
.page-back {
  display: flex;
  align-items: center;
  gap: 33px;
  margin-bottom: 32px;
}

img {
  width: 35px;
  height: 35px;
}

h1 {
  font-size: 24px;
}
</style>
