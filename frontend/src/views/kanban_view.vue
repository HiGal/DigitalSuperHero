<template>
    <div id="kanban" class="kanban">
        <section class="section">
            <h4>
                Задачи
            </h4>
        </section>
        <Kanban :stages="statuses" :blocks="blocks" @update-block="updateBlock">
            <div v-for="stage in statuses" :slot="stage" :key="stage">
                <h2>
                    {{ stage }}
                </h2>
            </div>
            <div v-for="item in blocks" :slot="item.id" :key="item.id">
                <div class="ktext">
                    {{ item.title }}
                </div>
            </div>
        </Kanban>
    </div>
</template>


<script>
    import faker from 'faker';
    import {debounce} from 'lodash';
    import Kanban from '../components/Kanban';
    import axios from 'axios';

    export default {
        name: "kanban",
        components: {
            Kanban,
        },
        created: function (){
            const AXIOS = axios.create({
                baseURL: 'http://10.20.35.154:5000',
                headers: {
                    Authorization: "JWT " + localStorage.getItem("role"),
                    "Content-Type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*"
                }

            });
            AXIOS.post('/board',{
                action: 'get',
                email: 'aaaa@aaaa.com',
                password: 'parol'
            }).then(function (response) {
                console.log(response.data['ANALYSIS']);
                // for (item in response.data){
                //     let i = 0;
                //
                //     for(data_t in ){
                //         this.blocks.push({
                //             status: data_t[0],
                //
                //         })
                //     }
                //     i++;
                // }
            })
        },
        data() {
            return {
                statuses: [
                    'Заявки', 'Технический анализ', 'Поиск подрядчиков', 'Ожидают согласования', 'Проверка выполнения', 'Выполненные'
                ],
                blocks: [],
            };
        },
        mounted() {
            for (let i = 0; i <= 20; i += 1) {
                this.blocks.push({
                    id: i,
                    status: this.statuses[Math.floor(Math.random() * 6)],
                    title: faker.company.bs(),
                });
            }
        },
        methods: {
            updateBlock: debounce(function (id, status) {
                this.blocks.find(b => b.id === Number(id)).status = status;
            }, 500),
            addBlock: debounce(function (stage) {
                this.blocks.push({
                    id: this.blocks.length,
                    status: stage,
                    title: faker.company.bs(),
                });
            }, 500),
        },
    };
</script>

<style>
    #kanban {
        font-family: "Avenir", Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    #nav {
        padding: 30px;
    }

    #nav a {
        font-weight: bold;
        color: #2c3e50;
    }

    #nav a.router-link-exact-active {
        color: #42b983;
    }
</style>
