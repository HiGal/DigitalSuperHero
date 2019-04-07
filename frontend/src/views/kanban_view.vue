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
                <div>
                    <strong>id:</strong> {{ item.id }}
                </div>

                <div class="ktext">
                    {{ item.title }}
                </div>
            </div>
            <div v-for="stage in statuses" :key="stage" :slot="`footer-${stage}`">
                <a href="" @click.prevent="() => addBlock(stage)">+ Add new block</a>
            </div>
        </Kanban>
    </div>
</template>


<script>
    import faker from 'faker';
    import {debounce} from 'lodash';
    import Kanban from '../components/Kanban';

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
