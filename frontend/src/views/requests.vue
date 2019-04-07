<template>
    <b-container fluid>
        <div class="container profile">
            <b-table
                    show-empty
                    stacked="md"
                    :items="items"
                    :fields="fields"
                    :current-page="currentPage"
                    :per-page="perPage"
                    :filter="filter"
                    :sort-by.sync="sortBy"
                    :sort-desc.sync="sortDesc"
                    :sort-direction="sortDirection"
                    @filtered="onFiltered"
            >
                <template slot="id" slot-scope="row">
                    <h2 :class="row.value" :id="row.value" ref="el">Заявка № {{row.value}}</h2>
                    <h5>{{row.item.location}}</h5>
                    <b-button size="m" @click="row.toggleDetails">
                        {{ row.detailsShowing ? 'Скрыть' : 'Показать' }} детали
                    </b-button>
                </template>

                <template slot="row-details" slot-scope="row">
                    <b-card>
                        <ul>
                            <div class="idBtn" hidden>{{row.item.id}}</div>
                            <h6>{{row.item.info}}</h6>
                            <h6>Полное ТУ: <a
                                    href="https://drive.google.com/uc?export=download&id=1WQNuiQjtQG_YY2QBn6geF-Xfl9OaTQ8m">Файл</a>
                            </h6>
                            <h6>Контактная информация подрядчика:</h6>
                            <ol>• {{row.item.name}}</ol>
                            <ol>• Номер телефона: {{row.item.phone}}</ol>
                            <ol>• E-mail: {{row.item.email}}</ol>
                            <br>

                            <b-button class="btn-primary btn-info" @click="popUp">
                                {{row.item.status}}
                            </b-button>
                        </ul>
                    </b-card>
                </template>
            </b-table>
        </div>

        <b-row>
            <b-col md="6" class="my-1">
                <b-pagination
                        v-model="currentPage"
                        :total-rows="totalRows"
                        :per-page="perPage"
                        class="my-0"
                ></b-pagination>
            </b-col>
        </b-row>

        <b-modal id="modal-info" @hide="resetModal" :title="modalInfo.title" ok-only>
            <pre>{{ modalInfo.content }}</pre>
        </b-modal>
    </b-container>
</template>

<script>

    const items = [{
        "id": 1,
        "location": "Казань",
        "name": "Имя 1",
        "info": "~Дополнительная информация~",
        "phone": "79999999999",
        "email": "example@abc.com",
        "status": "Выполняется"

    },
        {
            "id": 2,
            "location": "Казань",
            "name": "Имя 2",
            "info": "~Дополнительная информация~",
            "phone": "79999999999",
            "email": "example@example.com",
            "status": "Техническая экспертиза"

        },
        {
            "id": 3,
            "location": "Казань",
            "name": "Имя 3",
            "info": "~Дополнительная информация~",
            "phone": "79999999999",
            "email": "example@example.com",
            "status": "Выполнено"

        },
        {
            "id": 4,
            "location": "Казань",
            "name": "Имя ",
            "info": "~Дополнительная информация~",
            "phone": "79999999999",
            "email": "example@example.com",
            "status": "Ожидает ответа заказчика"

        }];

    export default {
        data() {
            return {
                items: items,
                fields: [
                    {key: 'id', label: 'Мои заявки'}
                ],
                currentPage: 1,
                perPage: 25,
                totalRows: items.length,
                pageOptions: [25, 50, 100],
                sortBy: null,
                sortDesc: false,
                filter: null,
                modalInfo: {title: '', content: ''}
            }
        },
        methods: {
            info(item, index, button) {
                this.modalInfo.title = `Row index: ${index}`;
                this.modalInfo.content = JSON.stringify(item, null, 2);
                this.$root.$emit('bv::show::modal', 'modalInfo', button)
            },
            resetModal() {
                this.modalInfo.title = '';
                this.modalInfo.content = ''
            },
            onFiltered(filteredItems) {
                // Trigger pagination to update the number of buttons/pages due to filtering
                this.totalRows = filteredItems.length;
                this.currentPage = 1
            }
        }
    }
</script>

<style scoped>

</style>