<template>
    <div id="app">
        <div class="header-top">
            <div class="row">
                <div class="col-4">
                    <a id="logo" href="/"></a>
                </div>
                <div class="col-8">
                    <div id="header-phone" class="pull-right text-right">
                        <span id="telephone">8 800 2000 878</span>
                        <br>
                        <span id="telephone-cen">Единый контакт-центр</span>
                    </div>
                </div>
            </div>
        </div>

        <b-navbar toggleable="lg" type="dark" variant="info" class="my-navbar">
            <div class="container navigation" style="min-height: 50px;">
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav>
                        <b-nav-item href="#">
                            <router-link style="color: white" to="/">Главная</router-link>
                        </b-nav-item>
                        <b-nav-item href="#">
                            <router-link style="color: white" to="/profile">Личный кабинет</router-link>
                        </b-nav-item>

                        <template v-if="isCompany || isContractor">
                            <b-nav-item href="#">
                                <router-link style="color: white" to="/market">Заявки</router-link>
                            </b-nav-item>
                        </template>

                        <template v-if="isCompany">
                            <b-nav-item href="#">
                                <router-link style="color: white" to="/kanban">Управление задачами</router-link>
                            </b-nav-item>
                        </template>
                        <template v-if="isCompany || isContractor || isCustomer">
                            <b-nav-item href="#">
                                <div style="color: white" class="top-name" v-on:click="sendLogoutReq()">Выйти</div>
                            </b-nav-item>
                        </template>
                    </b-navbar-nav>
                </b-collapse>
            </div>
        </b-navbar>
        <router-view/>

    </div>
</template>
<script>
    import Login from "./views/Login.vue";
    import Home from "./views/Home.vue";


    export default {
        data() {
            return {
                role:
                    localStorage.getItem("role") === null ? "" : localStorage.getItem("role"),
                isCustomer: false,
                isContractor: false,
                isCompany: false,
            };
        },
        created: function () {
            if (this.role === "customer") this.isCustomer = true;
            if (this.role === "contractor") this.isContractor = true;
            if (this.role === "company") this.isCompany = true;
            console.log(this.role);
        },
        components: {Login, Home},
        methods: {
            sendLogoutReq() {
                localStorage.removeItem("role");
                localStorage.removeItem("email");
                router.push("/home");
            },
        }
    };
</script>
<style lang="css">
    @import "assets/kanban.scss";
    @import "assets/css/style.css";
    @import url('https://fonts.googleapis.com/css?family=Exo+2');
</style>

