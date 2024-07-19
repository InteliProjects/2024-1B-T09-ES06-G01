<template>
  <div class="dashboard-radar-chart">
    <h3>{{ title }}</h3>
    <Radar :data="chartData" :options="options" />
  </div>
</template>

<script lang="ts">
import { defineComponent, toRefs } from 'vue';
import { Radar } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler
} from 'chart.js';

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler
);

export default defineComponent({
  name: "DashboardRadarChart",
  components: {
    Radar
  },
  props: {
    title: {
      type: String,
      required: true,
    },
    chartData: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const { chartData } = toRefs(props);
    const options = {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          beginAtZero: true,
          angleLines: {
            color: 'white' // Cor das linhas radiais
          },
          grid: {
            color: 'rgba(255, 255, 255, 0.2)' // Cor das linhas da grade
          },
          pointLabels: {
            font: {
              size: 14
            }
          },
          ticks: {
            color: '#fffff0', // Cor dos valores dos ticks
            backdropColor: 'rgba(0, 0, 0, 0)' // Remove o fundo dos ticks
          }
        }
      },
      plugins: {
        legend: {
          position: 'bottom',
        }
      }
    };
    return { chartData, options };
  }
});
</script>

<style scoped>
.dashboard-radar-chart {
  background-color: #334C45;
  padding: 32px;
  border-radius: 8px;
  color: white;
  height: 100%;
  max-height: 400px;
  overflow: hidden;
}

.dashboard-radar-chart h3 {
  margin: 0 0 10px 0;
  font-size: 1.2rem;
}

.radar-chart {
  height: 100%;
}
</style>
