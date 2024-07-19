<template>
  <div v-if="image" class="macrotheme-background-div">
    <img :src="`/${image}`" alt="Macrotheme background" />
    <h1>{{ macrotheme }}</h1>
  </div>
  <div class="page">
    <ThePageBack page="Macrotema" />
    <div>
      <div
        v-for="(projects, subtheme, index) in groupedProjects"
        :key="subtheme"
      >
        <SubthemeProjects :subtheme="subtheme" :projects="projects" />
        <TheDivider
          v-if="index < Object.keys(groupedProjects).length - 1"
          :key="`divider-${index}`"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRuntimeConfig } from "#imports";
import ThePageBack from "~/components/the-page-back.vue";
import TheDivider from "~/components/the-divisor.vue";
import SubthemeProjects from "~/components/subtheme-projects.vue";
import { useRouter } from "vue-router";

const config = useRuntimeConfig();
const groupedProjects = ref({});
const macrotheme = ref("");
const image = ref("");
const router = useRouter();

const { nome } = router.currentRoute.value.params;

switch (nome) {
  case "diversidade":
    image.value = "diversidade-bg.png";
    break;
  case "integridade":
    image.value = "integridade-bg.png";
    break;
  case "redução":
    image.value = "reducao-bg.png";
    break;
  case "produtividade":
    image.value = "produtividade-bg.png";
    break;
  case "conservação":
    image.value = "conservacao-bg.png";
    break;
  case "bem-estar":
    image.value = "bem-estar-bg.png";
    break;
  default:
    image.value = "";
}

const fetchData = async () => {
  try {
    const baseURL = config.public.baseURL;
    const response = await fetch(`${baseURL}projetos/macrotema?nome=${nome}`);
    const projects = await response.json();

    macrotheme.value = projects[0].macrotema_nome_completo;

    const grouped = projects.reduce((acc, project) => {
      if (!acc[project.subtema_nome]) {
        acc[project.subtema_nome] = [];
      }
      acc[project.subtema_nome].push(project);
      return acc;
    }, {});

    groupedProjects.value = grouped;
  } catch (error) {
    console.error("Error:", error);
  }
};

onMounted(() => {
  fetchData();
});
</script>

<style scoped lang="scss">
.page {
  padding: 0px 60px 33px 60px;

  .divider {
    margin-top: 36px;
    margin-bottom: 26px;
  }
}

.macrotheme-background-div {
  transform: translateY(-33px);
  width: 100%;
  height: 244px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
  }

  h1 {
    color: white;
    font-size: 48px;
    position: relative;
  }
}
</style>
