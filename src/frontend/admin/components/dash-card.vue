<template>
  <div class="dashboard-card">
    <h3>{{ title }}</h3>
    <p>{{ value }}</p>
  </div>
</template>

<script>
export default {
  name: "DashboardCard",
  props: {
    title: {
      type: String,
      required: true,
    },
    value: {
      type: Number,
      required: true,
    }
  }
};
</script>

<style scoped>
.dashboard-card {
  background-color: #334C45;
  padding: 20px;
  border-radius: 8px;
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.dashboard-card h3 {
  margin: 0;
  font-size: 1.2rem;
}

.dashboard-card p {
  margin: 0;
  font-size: 2rem;
  font-weight: bold;
}
</style>
