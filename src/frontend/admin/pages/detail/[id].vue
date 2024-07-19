<template>
  <div v-if="project.nome" class="page">
    <ThePageBack page="Detalhamento" />
    <div class="side-by-side">
      <h1>{{ project.nome }}</h1>
      <TheSubtheme
        :subtheme="project.subtema_nome"
        :macrothemeIcon="`/${project.macrotema_nome}-icon.svg`"
      />
    </div>
    <ProfileInfo
      :picture="project.ceos[0].foto"
      :name="project.ceos[0].nome"
      :enterprise="project.ceos[0].empresa_nome"
    />
    <TheDivider />
    <h2 class="desc-title">Descrição</h2>
    <p class="desc-text">
      {{ project.descricao }}
    </p>
    <div v-if="!isActive && !hasDenied" class="buttons-div">
      <TheButton @click="accept" text="Aceitar" secondaryStyle />
      <TheButton @click="deny" text="Negar" secondaryStyle background="red" />
    </div>
    <div v-if="isActive && !hasDenied">
      <TheDivider />
      <h2 class="desc-title">Acompanhamento</h2>
      <div
        v-if="project.atualizacoes.length"
        class="swiper-monitorings-container"
      >
        <SwiperMonitorings :monitorings="project.atualizacoes" />
      </div>
      <div
        :class="project.atualizacoes.length ? 'monitoring-form-container' : ''"
      >
        <MonitoringForm @create-monitoring="createMonitoring" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRuntimeConfig } from "#imports";
import { useRouter } from "vue-router";
import ThePageBack from "~/components/the-page-back.vue";
import TheSubtheme from "~/components/the-subtheme.vue";
import ProfileInfo from "~/components/profile-info.vue";
import TheDivider from "~/components/the-divisor.vue";
import TheButton from "~/components/the-button.vue";
import SwiperMonitorings from "~/components/swiper-monitorings.vue";
import MonitoringForm from "~/components/create-monitoring-form.vue";

const config = useRuntimeConfig();
const project = ref({});
const isActive = ref(false);
const hasDenied = ref(false);
const router = useRouter();

const { id } = router.currentRoute.value.params;

const accept = async () => {
  isActive.value = true;
  try {
    const baseURL = config.public.baseURL;
    await fetch(`${baseURL}projetos/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        estado: "ativo",
      }),
    });
  } catch (error) {
    console.error("Error:", error);
    isActive.value = false;
  }
};

const deny = async () => {
  isActive.value = false;
  hasDenied.value = true;
  try {
    const baseURL = config.public.baseURL;
    await fetch(`${baseURL}projetos/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        estado: "recusado",
      }),
    });

  } catch (error) {
    console.error("Error:", error);
    isActive.value = false;
    hasDenied.value = false;
  }
};

const fetchData = async () => {
  try {
    const baseURL = config.public.baseURL;
    const projectResponse = await fetch(`${baseURL}projetos/${id}`);
    const projectJSON = await projectResponse.json();
    project.value = projectJSON;
    isActive.value = ["ativo"].includes(projectJSON.estado);
    hasDenied.value = ["recusado"].includes(projectJSON.estado);
  } catch (error) {
    console.error("Error:", error);
  }
};

async function createMonitoring(monitoringData) {
  try {
    const baseURL = config.public.baseURL;
    await fetch(`${baseURL}projetos/atualizacao`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        projeto_id: id,
        ...monitoringData,
      }),
    });
    fetchData();
  } catch (error) {
    console.error("Error:", error);
  }
}

onMounted(() => {
  fetchData();
});
</script>

<style scoped lang="scss">
.page {
  padding: 0px 60px 32px 60px;

  h1 {
    font-size: 32px;
  }

  .side-by-side {
    margin-bottom: 35px;
  }

  .divider {
    margin-top: 35px;
    margin-bottom: 35px;
  }

  .desc-title {
    color: white;
    font-size: 24px;
    margin-bottom: 35px;
    font-weight: 500;
  }

  .desc-text {
    color: white;
    font-size: 20px;
    margin-bottom: 35px;
    font-weight: 300;
  }

  .buttons-div {
    display: flex;
    gap: 16px;
    width: 50%;
  }

  .monitoring-container {
    display: flex;
    width: 100vw;
  }

  .monitoring-form-container {
    display: flex;
    justify-content: center;
  }

  .swiper-monitorings-container {
    margin-bottom: 32px;
  }
}

.side-by-side {
  display: flex;
  justify-content: space-between;
}
</style>
