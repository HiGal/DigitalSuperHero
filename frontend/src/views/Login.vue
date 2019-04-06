<template>
  <div class="login_form">
      <b-form @submit="onSubmit" @reset="onReset" v-if="show" label="Войти в личный кабинет">
      <b-form-group>
        <b-form-input
          id="login"
          v-model="form.login"
          type="login"
          required
          placeholder="Логин"
        ></b-form-input>
      </b-form-group>
      <b-form-group>
        <b-form-input
          id="password"
          v-model="form.password"
          type="password"
          required
          placeholder="Пароль"
        ></b-form-input>
      </b-form-group>

        <b-button type="submit" variant="primary">Войти</b-button>

      </b-form>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      form: {
        login: "",
        password: ""
      },
        show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    }
  }
};
</script>
