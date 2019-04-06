<template>
  <div class="login_form">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group label="Войти в личный кабинет">
        <b-form-group>
          <b-form-select
            id="input-3"
            v-model="form.role"
            :options="roles"
            required
          ></b-form-select>
        </b-form-group>

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
      </b-form-group>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "login",
  data() {
    return {
      form: {
        role: "",
        login: "",
        password: ""
      },
      // roles: [
      //   { text: "Выберите категорию:", value: "" },
      //   { text: "Заказчик", value: "customer" },
      //   { text: "Подрядчик", value: "contractor" }
      // ],
      roles: [
        { text: "Выберите категорию:", value: "" },
        "Заказчик",
        "Подрядчик"
      ],
      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      this.token = this.login(
        this.form.role,
        this.form.login,
        this.form.password
      );
    },
    login(user_type, email, password) {
      const AXIOS = axios.create({
        baseURL: "http://10.20.35.154:5000",
        headers: {
          "Content-Type": "application/json; charset=UTF-8"
        }
      });

      AXIOS.post("/login", {
        user_type: user_type,
        email: email,
        password: password
      })
        .then(response => {
          localStorage.setItem("token", response.data.token);
        })
        .catch(() => {
          localStorage.removeItem("token");
        });
      return localStorage.getItem("token");
    }
  }
};
</script>
