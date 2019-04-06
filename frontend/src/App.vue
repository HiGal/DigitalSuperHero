<template>
    <div id="app">
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#">Сетевая компания</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav  >
                    <b-nav-item  href="#">
                        <router-link style="color: white" to="/">Домой</router-link>
                    </b-nav-item>
                    <b-nav-item href="#">
                        <router-link style="color: white" to="/login">Личный кабинет</router-link>
                    </b-nav-item>
                    <b-nav-item href="#">
                        <router-link style="color: white" to="/registration_contractor">Зарегистрироваться как подрядчик</router-link>
                    </b-nav-item>
                    <b-nav-item href="#">
                        <router-link style="color: white" to="/registration_customer">Зарегистрироваться как заказчик</router-link>
                    </b-nav-item>

                </b-navbar-nav>


            </b-collapse>
        </b-navbar>
        <router-view/>
    </div>
</template>

<style lang="css">
    @import "assets/css/style.css";
</style>

