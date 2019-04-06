<template>
    <div id="app">
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#">Сетевая компания</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav  >
                    <b-nav-item  href="#">
                        <router-link style="color: white" to="/">Home</router-link>
                    </b-nav-item>
                    <b-nav-item href="#">
                        <router-link style="color: white" to="/login">Login</router-link>
                    </b-nav-item>
                    <b-nav-item href="#">
                        <router-link style="color: white" to="/registration_contractor">Registration_contractor</router-link>
                    </b-nav-item>
                    <b-nav-item href="#">
                        <router-link style="color: white" to="/registration_customer">Registration_customer</router-link>
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

