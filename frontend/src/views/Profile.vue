<template>
    <ProfileComponent v-if="isCompany || isContractor || isCustomer"/>
    <LoginComponent v-else/>
</template>

<script>
    import LoginComponent from "../components/LoginComponent.vue";
    import ProfileComponent from "../components/ProfileComponent.vue";

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
        },
        components: {LoginComponent, ProfileComponent}
    }

</script>

<style>
    @import url("//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css");
</style>
