<template>
    <div class="container profile">
        <div class="row">
            <div class="col-6">
                <div class="img-profile">
                    <img src="../assets/profile.png" width="350" height="350">
                </div>
            </div>
            <div class="col-6">
                <div class="personal-info">
                    <h3>{{blocks.surname}}Галеев {{blocks.name}}Фарит {{blocks.fathername}}Фарукович</h3>
                    <small>
                        <cite title="Казань, Россия">Казань, Россия</cite>
                        <i class="glyphicon glyphicon-map-marker">
                        </i>
                    </small>
                    <p>
                        <i class="glyphicon glyphicon-envelope"></i>
                        {{blocks.email}}
                        abc@example.com
                        <br>
                        <i class="glyphicon glyphicon-earphone"></i>
                        {{blocks.phone}}
                        +7 (906) 321-15-58
                    </p>
                    <b-button class="btn btn-lg btn-primary" onclick="/requests">Мои заявки</b-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import faker from 'faker';
    import random from 'random';
    import router from "../router";

    export default {
        name: "Profile",
        data() {
            return {
                blocks: [],
                role:
                    localStorage.getItem("role") === null ? "" : localStorage.getItem("role"),
            }
        },
        created: function() {
            if (this.role === "") router.push("/login");
        },
        mounted() {
            this.blocks.push({
                name: faker.name.firstName(),
                surname: faker.name.lastName(),
                fathername: faker.name.firstName(),
                INN: random.int( 10000,99999),
                phone: faker.phone.phoneNumber(),
                email: faker.internet.email(),

            })
        }
    }
</script>

<style>
 @import url("//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css");
</style>
