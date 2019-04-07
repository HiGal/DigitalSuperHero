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
    // import axios from 'axios';

    export default {
        name: "kanban",
        components: {
            Kanban,
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
            // for (let i = 0; i <= 20; i += 1) {
            //     this.blocks.push({
            //         id: i,
            //         status: this.statuses[Math.floor(Math.random() * 6)],
            //         title: faker.company.bs(),
            //     });
            // }

            this.blocks.push({
                id: 1,
                status: this.statuses[1],
                title: "Подключение ТЦ к узлу электропитания"
            });

            this.blocks.push({
                id: 2,
                status: this.statuses[0],
                title: "Установка трансформатора на улице Гаврилова"
            });

            this.blocks.push({
                id: 3,
                status: this.statuses[0],
                title: "Подключение новостройки к сети (15 Мв)"
            });

            this.blocks.push({
                id: 4,
                status: this.statuses[5],
                title: "Подключение частного дома к сети"
            });

            this.blocks.push({
                id: 5,
                status: this.statuses[2],
                title: "Подключение частного дома к сети"
            });
            // const AXIOS = axios.create({
            //     baseURL: 'http://10.20.35.154:5000',
            //     headers: {
            //         Authorization: "JWT " + localStorage.getItem("role"),
            //         "Content-Type": "application/json; charset=UTF-8",
            //         "Access-Control-Allow-Origin": "*"
            //     }
            //
            // });
            // AXIOS.post('/board', {
            //     action: 'get',
            //     email: 'aaaa@aaaa.com',
            //     password: 'parol'
            // }).then(function (response) {
            //     // console.log(response.data['ANALYSIS']);
            //     var elements = response.data;
            //
            //     for (var element in elements) {
            //         var data = elements[element];
            //         this.blocks.push({
            //             id: data.id,
            //             status: 1,
            //             title: data.task
            //         })
            //     }
            // })
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
