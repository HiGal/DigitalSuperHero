<template>
    <div id="app">
        <div class="header-top">
            <div class="row">
                <div class="col-4">
                    <a id="logo" href="/"></a>
                </div>
                <div class="col-8">
                    <div id="header-phone" class="pull-right text-right">
                        <span id="phone">8 800 2000 878</span>
                        <br>
                        <span id="phone-cen">Единый контакт-центр</span>
                    </div>
            </div>
        </div>
    </div>
    <b-navbar toggleable="lg" type="dark" variant="info">
        <div class="container navigation" style="min-height: 50px;">
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item href="#">
                        <router-link style="color: white" to="/">Главная</router-link>
                    </b-nav-item>
                    <b-nav-item href="#">
                        <router-link style="color: white" to="/login">Личный кабинет</router-link>
                    </b-nav-item>
                    <b-nav-item href="#">
                        <router-link style="color: white" to="/registration_contractor">Зарегистрироваться как
                            подрядчик
                        </router-link>
                    </b-nav-item>
                    <b-nav-item href="#">
                        <router-link style="color: white" to="/registration_customer">Зарегистрироваться как
                            заказчик
                        </router-link>
                    </b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </div>
    </b-navbar>
    <router-view/>

    </div>
</template>

<style lang="css">
    @import "assets/css/style.css";
     @import url('https://fonts.googleapis.com/css?family=Exo+2');
</style>

