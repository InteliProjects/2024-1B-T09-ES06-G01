<template>
  <div class="card">
    <TheInput @keyup.enter="submit" v-model="data" placeholder="Data" type="date" />
    <TheInput
      @keyup.enter="submit"
      v-model="descricao"
      placeholder="Descrição"
    />
  </div>
</template>

<script>
import TheInput from "~/components/the-input.vue";

export default {
  components: {
    TheInput,
  },
  data() {
    return {
      data: "",
      descricao: "",
    };
  },
  methods: {
    submit() {
      const formattedDate = this.formatDate(this.data);
      const monitoringData = {
        data: formattedDate,
        descricao: this.descricao,
      };

      this.$emit("create-monitoring", monitoringData);
    },
    formatDate(date) {
      const [year, month, day] = date.split("-");
      return `${year}-${month}-${day}`;
    },
  },
};
</script>

<style scoped>
.card {
  width: 319px;
  height: 220px;
  border-radius: 6px;
  border: 3px solid #334c45;
  padding: 30px 25px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
