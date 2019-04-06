<template>
  <div class="registration_form">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group label="Название организации">
        <b-form-input
          id="company_name"
          v-model="form.company_name"
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

      <b-form-group label="ИНН (Идентификационный номер налогоплательщика)">
        <b-form-input id="inn" v-model="form.inn" required></b-form-input>
      </b-form-group>

      <b-form-group label="Дата регистрации компании">
        <b-form-input
          class="date"
          id="date"
          v-model="form.date"
          required
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Зарегистрироваться</b-button>
    </b-form>
  </div>
</template>

<script>
import moment from "moment";
export default {
  name: "registration_contractor",
  data() {
    return {
      form: {
        company_name: "",
        email: "",
        password: "",
        phone: "",
        inn: "",
        date: moment(new Date()).format("YYYY-MM-DD")
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
