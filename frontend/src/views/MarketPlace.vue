<template>
    <b-container fluid>
        <b-row>
            <b-col md="6" class="my-1">
                <b-form-group label-cols-sm="3" label="Найти" class="mb-0">
                    <b-input-group>
                        <b-form-input v-model="filter" placeholder="Начните вводить значение..."></b-form-input>
                        <b-input-group-append>
                            <b-button :disabled="!filter" @click="filter = ''">Очистить</b-button>
                        </b-input-group-append>
                    </b-input-group>
                </b-form-group>
            </b-col>

            <b-col md="6" class="my-1">
                <b-form-group label-cols-sm="3" label="Сортировать" class="mb-0">
                    <b-input-group>
                        <b-form-select v-model="sortBy" :options="sortOptions">
                            <option slot="first" :value="null">-</option>
                        </b-form-select>
                        <b-form-select v-model="sortDesc" :disabled="!sortBy" slot="append">
                            <option :value="false">по возрастанию</option>
                            <option :value="true">по убыванию</option>
                        </b-form-select>
                    </b-input-group>
                </b-form-group>
            </b-col>

            <b-col md="6" class="my-1">
                <b-form-group label-cols-sm="3" label="Показывать по" class="mb-0">
                    <b-form-select v-model="perPage" :options="pageOptions"></b-form-select>
                </b-form-group>
            </b-col>
        </b-row>

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
                        <h6>Полное ТУ: <a href="https://drive.google.com/uc?export=download&id=1WQNuiQjtQG_YY2QBn6geF-Xfl9OaTQ8m">Файл</a></h6>
                        <h6>Контактная информация:</h6>
                        <p>• {{row.item.name}}</p>
                        <p>• Номер телефона: {{row.item.phone}}</p>
                        <p>• E-mail: {{row.item.email}}</p>

                        <b-button class="btn-primary btn-info" @click="popUp">
                            Откликнуться на заявку
                        </b-button>
                    </ul>
                </b-card>
            </template>
        </b-table>

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

        <div class="container">
            <div class="modal" id="myModal" tabindex="-1" role="dialog" aria-labelledby="expansion">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title">Modal Header</h4>
                        </div>
                        <div class="modal-body">
                            <p>Some text in the modal.</p>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </b-container>

</template>

<script>

    const items = [{
        "id": 123,
        "location": "Казань",
        "name": "Имя 1",
        "info": "~Дополнительная информация~",
        "phone": "79999999999",
        "email": "example@abc.com",
    },
        {
            "id": 345,
            "location": "Казань",
            "name": "Имя 2",
            "info": "~Дополнительная информация~",
            "phone": "79999999999",
            "email": "example@example.com",

        },
        {
            "id": 567,
            "location": "Казань",
            "name": "Имя 3",
            "info": "~Дополнительная информация~",
            "phone": "79999999999",
            "email": "example@example.com",
        },
        {
            "id": 789,
            "location": "Казань",
            "name": "Имя ",
            "info": "~Дополнительная информация~",
            "phone": "79999999999",
            "email": "example@example.com",
        }];

    export default {
        data() {
            return {
                items: items,
                fields: [
                    {key: 'id', label: 'Заявки'}
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
        computed: {
            sortOptions() {
                return this.fields
                    .filter(f => f.sortable)
                    .map(f => {
                        return {text: f.label, value: f.key}
                    })
            }
        },
        methods: {
            info(item, index, button) {
                this.modalInfo.title = `Row index: ${index}`;
                this.modalInfo.content = JSON.stringify(item, null, 2);
                this.$root.$emit('bv::show::modal', 'modalInfo', button)
            },
            resetModal() {
                this.modalInfo.title = ''
                this.modalInfo.content = ''
            },
            onFiltered(filteredItems) {
                // Trigger pagination to update the number of buttons/pages due to filtering
                this.totalRows = filteredItems.length;
                this.currentPage = 1
            },
            popUp(e) {
                //$(document).ready(function(){});
                var element = e.target.parentElement.getElementsByTagName('div')[0];
                var id = element.innerText;
                var data = NaN;
                // for (let i = 0; i < items.length; i++) {
                //     if (items[i]['id'] == id) {
                //         data = items[i];
                //         break;
                //     }
                // }
                // <a href="#details" class="btn btn-primary btn-lg" data-toggle="modal">Show details</a>
                //
                // <div class="modal" id="details" tabindex="-1" role="dialog" aria-labelledby="expansion"

                $('#myModal').modal('show');
            }
        }
    }
</script>
