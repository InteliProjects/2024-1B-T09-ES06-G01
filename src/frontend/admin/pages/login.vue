<template>
  <div class="page">
    <div class="card">
      <div class="register-side">
        <h1>Seja bem vindo!</h1>
        <div class="buttons-div">
          <TheInput v-model="email" icon="/user.png" placeholder="Email" />
          <TheInput
            v-model="password"
            icon="/padlock.png"
            placeholder="Senha"
          />
        </div>
        <button class="forgot-password">Esqueceu a senha?</button>
        <TheButton @click="login" text="Entrar" :secondaryStyle="true" />
        <div class="or-div">
          <TheDivider />
          <p>ou</p>
          <TheDivider />
        </div>
        <TheButton icon="/google.png" text="Entrar no Google" />
        <button class="sign-up">
          Não tem uma conta? <span>Solicitar cadastro</span>
        </button>
      </div>
      <div class="logo-side">
        <div class="logo-div">
          <img src="/half-coffeebreak-logo.png" alt="Coffeebreak logo" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TheInput from "~/components/the-input.vue";
import TheButton from "~/components/the-button.vue";
import TheDivider from "~/components/the-divisor.vue";

definePageMeta({
  layout: false,
});

export default {
  components: {
    TheInput,
    TheButton,
    TheDivider,
  },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login() {
      setTimeout(() => {
        if (this.email == "admin@gmail.com" && this.password == "admin123") {
          localStorage.setItem("isAuthenticated", "true");
          setTimeout(() => {
            this.$router.push("/");
          }, 850);
        } else {
          alert(
            "E-mail ou senha incorretos. Verifique suas credenciais e tente novamente."
          );
        }
      }, 500);
    },
  },
};
</script>

<style scoped lang="scss">
.page {
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 130px 8vw;

  .card {
    display: grid;
    grid-template-columns: 1fr 1fr;
    overflow: hidden;
    border-radius: 6px;
    box-shadow: 0 344px 138px rgba(0, 0, 0, 0.02),
      0 193px 116px rgba(0, 0, 0, 0.06), 0 86px 86px rgba(0, 0, 0, 0.11),
      0 21px 47px rgba(0, 0, 0, 0.12);

    .register-side {
      background-color: #334c45;
      padding: 100px 110px;

      h1 {
        color: white;
        font-size: 24px;
        margin-bottom: 36px;
        font-weight: 600;
        text-align: center;
      }

      .buttons-div {
        display: flex;
        flex-direction: column;
        gap: 14px;
        margin-bottom: 14px;
      }

      .forgot-password {
        margin-bottom: 14px;
        color: #42988c;
        font-size: 16px;
        text-align: right;
        font-weight: 300;
        margin-left: auto;
      }

      .or-div {
        margin: 20px 0px;
        display: flex;
        gap: 8px;
        align-items: center;

        p {
          color: #42988c;
          font-weight: 300;
          font-size: 16px;
        }

        .divider {
          background-color: #42988c;
        }
      }

      .sign-up {
        color: white;
        font-weight: 300;
        font-size: 16px;
        text-align: center;
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto;

        span {
          color: #42988c;
        }
      }
    }

    .logo-side {
      background-color: #375c52;
      padding: 64px 55px;
      box-sizing: border-box;

      .logo-div {
        background-color: #32534a;
        overflow: hidden;
        position: relative;
        width: 100%;
        height: 100%;

        img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          position: absolute;
          top: 0;
          left: 0;
        }
      }
    }
  }
}
</style>
