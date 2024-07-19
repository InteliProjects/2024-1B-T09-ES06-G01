<template>
  <div class="dashboard-bar-chart">
    <h3>{{ title }}</h3>
    <bar-chart :data="chartData" :options="options" />
  </div>
</template>

<script lang="ts">
import { defineComponent, toRefs } from 'vue';
import { Bar } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default defineComponent({
  name: "DashboardBarChart",
  components: {
    BarChart: Bar
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
        x: {
          beginAtZero: true
        },
        y: {
          beginAtZero: true
        }
      },
      plugins: {
        legend: {
          position: 'bottom'
        }
      }
    };
    return { chartData, options };
  }
});
</script>

<style scoped>
.dashboard-bar-chart {
  background-color: #334C45;
  padding: 32px;
  border-radius: 8px;
  color: white;
  height: 100%;
  max-height: 400px;
  overflow: hidden;
}

.dashboard-bar-chart h3 {
  margin: 0 0 10px 0;
  font-size: 1.2rem;
}

.bar-chart {
  height: 100%;
}
</style>
