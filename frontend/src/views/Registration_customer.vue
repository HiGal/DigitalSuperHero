<template>
  <div class="registration_form">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group label="Имя">
        <b-form-input id="name" v-model="form.name" required></b-form-input>
      </b-form-group>

      <b-form-group label="Фамилия">
        <b-form-input
          id="surname"
          v-model="form.surname"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Отчество">
        <b-form-input
          id="midname"
          v-model="form.midname"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group label="E-mail">
        <b-form-input
          id="email"
          v-model="form.email"
          type="email"
          required
          placeholder="example@example.ru"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Пароль">
        <b-form-input
          id="password"
          v-model="form.password"
          type="password"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Номер телефона">
        <b-form-input
          id="phone"
          v-model="form.phone"
          required
          placeholder="79999999999"
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Зарегистрироваться</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "registration_customer",
  data() {
    return {
      form: {
        name: "",
        surname: "",
        midname: "",
        email: "",
        password: "",
        phone: ""
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
