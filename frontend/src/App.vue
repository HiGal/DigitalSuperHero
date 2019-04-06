<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/registration_contractor">Registration_contractor</router-link> |
      <router-link to="/registration_customer">Registration_customer</router-link>
    </div>
    <router-view />
  </div>
</template>

<style lang="css">
  @import "assets/css/style.css";
</style>
<script>
    import Home from "./views/Home";
    import Kanban from "./components/Kanban";
    export default {
        components: {Kanban, Home}
    }
</script>