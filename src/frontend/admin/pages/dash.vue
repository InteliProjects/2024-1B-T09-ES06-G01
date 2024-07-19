<template>
  <section class="dashboards">
    <header class="dashboard-header">
      <ThePageBack page="Dashboards" />
    </header>
    <div class="dashboard-grid">
      <div class="dashboard-row">
        <div class="dashboard-column small-column">
          <DashboardCard title="Projetos" :value="projectCount" />
          <DashboardCard title="Sinergias" :value="synergyCount" />
        </div>
        <div class="dashboard-row large-row">
          <DashboardTimeline title="Sinergias x Tempo" :chartData="timelineData" class="large-timeline"/>
          <DashboardCard title="CEOs" :value="ceoCount" class="small-ceos" />
        </div>
      </div>
      <div class="dashboard-row">
        <DashboardBarChart title="Sinergias e Projetos x Macrotema" :chartData="barChartData"/>
        <DashboardRadarChart title="Sinergias e Projetos x Macrotemas" :chartData="radarChartData"/>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRuntimeConfig } from '#imports';
import ThePageBack from '~/components/the-page-back.vue';
import DashboardCard from '~/components/dash-card.vue';
import DashboardTimeline from '~/components/dash-timeline.vue';
import DashboardBarChart from '~/components/dash-bar.vue';
import DashboardRadarChart from '~/components/dash-radar.vue';

const config = useRuntimeConfig();
const projectCount = ref(0);
const synergyCount = ref(0);
const ceoCount = ref(0);
const timelineData = ref({
  labels: [],
  datasets: []
});
const barChartData = ref({
  labels: [],
  datasets: []
});
const radarChartData = ref({
  labels: [],
  datasets: []
});

const fetchDashboardData = async () => {
  try {
    const [projectRes, ceoRes, synergyRes, projectsMacrotemaRes, synergiesMacrotemaRes, synergiesTimelineRes] = await Promise.all([
      $fetch('/projetos/dash', { baseURL: config.public.baseURL }),
      $fetch('/ceos/dash', { baseURL: config.public.baseURL }),
      $fetch('/projetos/sinergias', { baseURL: config.public.baseURL }),
      $fetch('/projetos/projetosxmacrotema', { baseURL: config.public.baseURL }),
      $fetch('/projetos/sinergiaxmacrotema', { baseURL: config.public.baseURL }),
      $fetch('/projetos/sinergiaxtempo/all_time', { baseURL: config.public.baseURL })
    ]);

    projectCount.value = projectRes.projetos;

    ceoCount.value = ceoRes.ceos;

    synergyCount.value = synergyRes.sinergias;

    barChartData.value = {
      labels: Object.keys(projectsMacrotemaRes),
      datasets: [
        {
          label: 'Projetos',
          backgroundColor: '#57BD99',
          data: Object.values(projectsMacrotemaRes)
        },
        {
          label: 'Sinergias',
          backgroundColor: '#365E54',
          data: Object.values(synergiesMacrotemaRes)
        }
      ]
    };

    radarChartData.value = {
      labels: Object.keys(projectsMacrotemaRes),
      datasets: [
        {
          label: 'Projetos',
          backgroundColor: 'rgba(87, 189, 153, 0.2)',
          borderColor: '#57BD99',
          pointBackgroundColor: '#57BD99',
          data: Object.values(projectsMacrotemaRes)
        },
        {
          label: 'Sinergias',
          backgroundColor: 'rgba(54, 94, 84, 0.2)',
          borderColor: '#365E54',
          pointBackgroundColor: '#365E54',
          data: Object.values(synergiesMacrotemaRes)
        }
      ]
    };

    const timelineLabels = Object.keys(synergiesTimelineRes);
    const timelineValues = Object.values(synergiesTimelineRes);

    timelineData.value = {
      labels: timelineLabels,
      datasets: [
        {
          label: 'Sinergias',
          backgroundColor: '#57BD99',
          borderColor: '#57BD99',
          fill: false,
          data: timelineValues
        }
      ]
    };
  } catch (error) {
    console.error('Error fetching dashboard data:', error);
  }
};

onMounted(() => {
  fetchDashboardData();
});
</script>

<style scoped lang="scss">
.dashboards {
  padding: 0 60px;
}

.dashboard-header {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.dashboard-grid {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 32px;
}

.dashboard-row {
  display: flex;
  gap: 16px;
}

.dashboard-column {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.dashboard-row > * {
  flex: 1;
}

.small-column {
  flex: 1;
}

.large-row {
  flex: 3;
  display: flex;
  gap: 16px;
}

.large-timeline {
  flex: 3;
  max-height: 420px;
}

.small-ceos {
  flex: 1;
}

.dashboard-column > * {
  min-height: 200px;
  max-height: 400px;
}
</style>
