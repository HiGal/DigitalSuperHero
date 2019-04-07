import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
    mode: "history",
    base: process.env.BASE_URL,
    routes: [
        {
            path: "/",
            name: "home",
            component: Home
        },
        {
            path: "/login",
            name: "login",
            component: () =>
                import(/* webpackChunkName: "about" */ "./views/Login.vue")
        },
        {
            path: "/registration_contractor",
            name: "registration_contractor",
            component: () =>
                import(/* webpackChunkName: "about" */ "./views/Registration_contractor.vue")
        },
        {
            path: "/registration_customer",
            name: "registration_customer",
            component: () =>
                import(/* webpackChunkName: "about" */ "./views/Registration_customer.vue")
        },
        {
            path: "/kanban",
            name: "kanban",
            component: () =>
                import("./views/kanban_view.vue")
        },
        {
            path: "/profile",
            name: "Profile",
            component: () =>
                import("./views/Profile.vue")
        }
    ]
});
