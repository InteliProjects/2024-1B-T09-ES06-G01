<template>
  <div class="card">
    <div class="content">
        <p class="date">{{ content.data  }}</p>
        <p class="description">{{ content.descricao }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MonitoringCard",
  props: {
    content: {
      type: Object,
      required: true,
    },
  },
};
</script>


<style scoped lang="scss">
.card {
  width: 319px;
  height: 220px;
  border-radius: 6px;
  background-color: #334C45;
  display: flex;
  align-items: center;
  padding: 0px 30px;
  overflow: hidden;

  .content {
    display: flex;
    flex-direction: column;
    gap: 10px;
      
      .date {
        font-size: 16px;
        color: white;
        font-weight: 300;
      }
    
      .description {
        font-size: 20px;
        color: white;
        font-weight: 300;
      }
  }

}
</style>
