<template>
  <form @submit.prevent="submit" class="form">
    <h1>{{ user ? 'Editar' : 'Cadastrar' }} usuário</h1>
    <TheInput v-model="nome" placeholder="Nome" />
    <div class="form-divisor">
      <TheInput v-model="empresa" placeholder="Empresa" />
      <TheInput v-model="cargo" placeholder="Cargo" />
    </div>
    <TheInput v-model="email" placeholder="E-mail cadastro" />
    <div class="form-divisor">
      <TheInput v-model="linkedin" placeholder="LinkedIn" />
      <TheInput v-model="celular" placeholder="Celular" />
    </div>
    <TheInput v-model="linkEmpresa" placeholder="Link empresa" />
    <div class="form-divisor">
      <TheButton text="Voltar" @click="closeModal" />
      <TheButton 
        :text="user ? 'Atualizar usuário' : 'Criar usuário'" 
        type="submit" 
        secondaryStyle 
      />
    </div>
  </form>
</template>

<script>
import TheInput from '~/components/the-input.vue';
import TheButton from '~/components/the-button.vue';

export default {
  props: {
    user: {
      type: Object,
      default: null
    }
  },
  components: {
    TheInput,
    TheButton
  },
  data() {
    return {
      nome: this.user?.nome || '',
      empresa: this.user?.empresa_nome || '',
      cargo: this.user?.cargo || '',
      email: this.user?.email || '',
      linkedin: this.user?.linkedin || '',
      celular: this.user?.celular || '',
      linkEmpresa: this.user?.empresa_link || ''
    };
  },
  methods: {
    submit() {
      const userData = {
        id: this.user?.id || Date.now(),
        nome: this.nome,
        empresa_nome: this.empresa,
        foto: this.user?.foto || 'https://api.dicebear.com/8.x/miniavs/svg?seed=dudu',
        cargo: this.cargo,
        email: this.email,
        linkedin: this.linkedin,
        celular: this.celular,
        empresa_link: this.linkEmpresa,
        senha: ''
      };

      if (this.user) {
        this.$emit('update-user', userData);
      } else {
        this.$emit('create-user', userData);
      }
    },
    closeModal(event) {
      event.preventDefault();
      this.$emit('close-modal');
    }
  }
}
</script>

<style scoped lang="scss">
.form {
  display: flex;
  flex-direction: column;
  gap: 16px;

  &-divisor {
    display: flex;
    justify-content: space-between;
    > * {
      width: 48%;
    }
  }
}
</style>
