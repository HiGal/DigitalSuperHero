<template>
    <div class="registration_form">
        <b-form @submit="onSubmit" v-if="show">
            <b-form-group label="Регистрация" class="reg"></b-form-group>
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
                        type="text"
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
    import router from "../router";
    import axios from "axios";

    export default {
        name: "registration_contractor",
        data() {
            return {
                form: {
                    user_type: "contractor",
                    company_name: "",
                    email: "",
                    password: "",
                    cpassword: "",
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
                this.role = this.register(
                    this.form.user_type,
                    this.form.company_name,
                    this.form.email,
                    this.form.password,
                    this.form.cpassword,
                    this.form.phone,
                    this.form.inn,
                    this.form.date
                );
                router.push("/");
            },
            register(
                user_type,
                company_name,
                email,
                password,
                cpassword,
                phone,
                inn,
                date
            ) {
                const AXIOS = axios.create({
                    baseURL: "http://10.20.35.154:5000",
                    headers: {
                        Authorization: "JWT " + localStorage.getItem("role"),
                        "Content-Type": "application/json; charset=UTF-8",
                        "Access-Control-Allow-Origin": "*"
                    }
                });

                AXIOS.post("/register", {
                    user_type: user_type,
                    email: email,
                    password: password,
                    cpassword: cpassword,
                    phone: phone,
                    inn: inn,
                    company_name: company_name,
                    reg_date: date
                })
                    .then(response => {
                        localStorage.setItem("role", response.data.role);
                        localStorage.setItem("email", response.data.email);
                    })
                    .catch(() => {
                        localStorage.removeItem("role");
                    });
                return localStorage.getItem("role");
            }
        }
    };
</script>
