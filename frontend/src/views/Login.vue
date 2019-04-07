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
            <b-button type="submit" variant="primary">Войти</b-button>
            <b-dropdown class="dropdown" right text="Регистрация" variant="info">
                <b-dropdown-item variant="info" href="/registration_customer">Зарегистрироваться как заказчик</b-dropdown-item>
                <b-dropdown-divider></b-dropdown-divider>
                <b-dropdown-item variant="info" href="/registration_contractor">Зарегистрироваться как подрядчик</b-dropdown-item>
            </b-dropdown>
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
                },
                roles: ["Заказчик", "Подрядчик", "Сетевая компания"
                ],
                show: true
            };
        },

        methods: {
            onSubmit(evt) {
                evt.preventDefault();
                if (this.form.role === "Заказчик") this.form.role = "customer";
                else if (this.form.role === "Подрядчик") this.form.role = "contractor";
                else if (this.form.role === "Сетевая компания") this.form.role = "company";
                else this.form.role = "";
                this.role = this.login(
                    this.form.role,
                    this.form.email,
                    this.form.password
                );
                router.push("/profile");
            },
            login(user_type, email, password) {
                const AXIOS = axios.create({
                    baseURL: "http://10.20.35.154:5000",
                    headers: {
                        Authorization: "JWT " + localStorage.getItem("role"),
                        "Content-Type": "application/json; charset=UTF-8",
                        "Access-Control-Allow-Origin": "*"
                    }
                });

                AXIOS.post("/login", {
                    user_type: user_type,
                    email: email,
                    password: password
                })
                    .then(response => {
                        localStorage.setItem("role", response.data.role);
                        localStorage.setItem("email", response.data.email);
                        console.log(localStorage.getItem("role"));
                    })
                    .catch(() => {
                        localStorage.removeItem("role");
                    });
                return localStorage.getItem("role");
            }
        }
    };
</script>
