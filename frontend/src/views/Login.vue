<template>
  <div class="login_form">
    <b-form @submit="onSubmit" v-if="show">
      <b-form-group label="Войти в личный кабинет">
      </b-form-group>
        <b-form-group>
          <b-form-select
            id="role"
            v-model="form.role"
            :options="roles"
            required
          ></b-form-select>
        </b-form-group>

        <b-form-group>
          <b-form-input
            id="email"
            v-model="form.email"
            type="email"
            required
            placeholder="E-mail"
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
        <b-form-group>
        <b-form-input
                id="cpassword"
                v-model="form.cpassword"
                type="cpassword"
                required
                placeholder="Подтвердите пароль"
        ></b-form-input>
      </b-form-group>
        <b-button type="submit" variant="primary">Войти</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
import router from "../router";
export default {
  name: "login",
  data() {
    return {
      form: {
        role: "",
        email: "",
        password: "",
        cpassword: ""
      },
      roles: ["Выберите категорию:", "Заказчик", "Подрядчик", "Сетевая компания"
      ],
      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      if (this.form.role === "Выберите категорию:") this.form.role = "";
      else if (this.form.role === "Заказчик") this.form.role = "customer";
      else if (this.form.role === "Подрядчик") this.form.role = "contractor";
      else if (this.form.role === "Сетевая компания") this.form.role = "company";
      this.token = this.login(
        this.form.role,
        this.form.email,
        this.form.password,
              this.form.cpassword
      );
      router.push("/");
    },
    login(user_type, email, password, cpassword) {
      const AXIOS = axios.create({
        baseURL: "http://10.20.35.154:5000",
        headers: {
          "Content-Type": "application/json; charset=UTF-8"
        }
      });

      AXIOS.post("/login", {
        user_type: user_type,
        email: email,
        password: password,
        cpassword: cpassword
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
