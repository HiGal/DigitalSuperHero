<template>
    <div class="user-table">
        <b-table :items="data" :fields="fields">
            <template slot="request" slot-scope="data">
                <b-card>
                    <b-card-text>
                        With supporting text below as a natural lead-in to additional content.
                    </b-card-text>
                    <b-button href="#" variant="primary">Go somewhere</b-button>
                </b-card>
            </template>
        </b-table>
    </div>
</template>

<script>
    export default {
        name: "MarketPlace",
        props: ["requests"],
        data() {
            return {
                fields: {
                    card: {
                        key: "request",
                        Label: "",
                        sortable: true
                    }
                },
                currentPage: 1
            }
        },
    }
</script>

