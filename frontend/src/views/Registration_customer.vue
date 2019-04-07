<template>
    <div class="registration_form">
        <b-form @submit="onSubmit" v-if="show">
            <b-form-group label="Регистрация" class="reg"></b-form-group>

            <b-form-group label="Фамилия">
                <b-form-input
                        id="surname"
                        v-model="form.surname"
                        required
                ></b-form-input>
            </b-form-group>

            <b-form-group label="Имя">
                <b-form-input id="name" v-model="form.name" required></b-form-input>
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

            <b-form-group label="Подтвердите пароль">
                <b-form-input
                        id="сpassword"
                        v-model="form.cpassword"
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
    import moment from "moment";
    import router from "../router";
    import axios from "axios";

    export default {
        name: "registration_customer",
        data() {
            return {
                form: {
                    user_type: "customer",
                    name: "",
                    surname: "",
                    midname: "",
                    email: "",
                    password: "",
                    cpassword: "",
                    phone: ""
                },
                show: true
            };
        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault();
                this.token = this.register(
                    this.form.user_type,
                    this.form.email,
                    this.form.password,
                    this.form.cpassword,
                    this.form.phone,
                    this.form.name,
                    this.form.surname,
                    this.form.midname
                );
                router.push("/");
            },
            register(
                user_type,
                email,
                password,
                cpassword,
                phone,
                name,
                surname,
                midname
            ) {
                const AXIOS = axios.create({
                    baseURL: "http://10.20.35.161:5000",
                    headers: {

                        "Content-Type": "application/json; charset=UTF-8"
                    }
                });

                AXIOS.post("/register", {
                    user_type: user_type,
                    email: email,
                    password: password,
                    cpassword: cpassword,
                    phone: phone,
                    name: name,
                    surname:surname,
                    midname:midname
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
