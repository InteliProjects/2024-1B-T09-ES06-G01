<template>
  <div class="dashboard-timeline">
    <h3>{{ title }}</h3>
    <line-chart :data="chartData" :options="options" />
  </div>
</template>

<script lang="ts">
import { defineComponent, toRefs } from 'vue';
import { Line } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement);

export default defineComponent({
  name: "DashboardTimeline",
  components: {
    LineChart: Line
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
.dashboard-timeline {
  background-color: #334C45;
  padding: 32px;
  border-radius: 8px;
  color: white;
  height: 100%;
  overflow: hidden;
}

.dashboard-timeline h3 {
  margin: 0 0 10px 0;
  font-size: 1.2rem;
}

.line-chart {
  height: 100%;
}
</style>
