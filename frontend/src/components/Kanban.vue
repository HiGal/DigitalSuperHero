<template>
    <div class="drag-container">
        <div class="col">
            <ul class="drag-list">

                <li v-for="stage in stages" class="drag-column" :class="{['drag-column-' + stage]: true}"
                    :key="stage">
                    <div class="heading">
                        <h2>{{ stage }}</h2>
                    </div>

                    <div class="drag-options"></div>
                    <ul class="drag-inner-list" ref="list" :data-status="stage">
                            <li class="drag-item kanban-label" v-for="block in getBlocks(stage)" :data-block-id="block.id"
                                :key="block.id">
                                <article>
                                    <slot :name="block.id">
                                        <strong>{{ block.status }}</strong>
                                        <div>{{ block.id }}</div>
                                    </slot>
                                </article>
                            </li>
                    </ul>
                    <!--                    <div class="drag-column-footer">-->
                    <!--                        <slot :name="`footer-${stage}`"></slot>-->
                    <!--                    </div>-->
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import dragula from 'dragula';

    export default {
        name: 'kanban',
        props: {
            stages: {},
            blocks: {},
        },
        data() {
            return {};
        },
        computed: {
            localBlocks() {
                return this.blocks;
            },
        },
        methods: {
            getBlocks(status) {
                return this.localBlocks.filter(block => block.status === status);
            },
        },
        mounted() {
            dragula(this.$refs.list)
                .on('drag', (el) => {
                    el.classList.add('is-moving');
                })
                .on('drop', (block, list) => {
                    let index = 0;
                    for (index = 0; index < list.children.length; index += 1) {
                        if (list.children[index].classList.contains('is-moving')) break;
                    }
                    this.$emit('update-block', block.dataset.blockId, list.dataset.status, index);
                })
                .on('dragend', (el) => {
                    el.classList.remove('is-moving');
                    window.setTimeout(() => {
                        el.classList.add('is-moved');
                        window.setTimeout(() => {
                            el.classList.remove('is-moved');
                        }, 600);
                    }, 100);
                });
        },
    };
</script>

<style lang="scss">
    @import '../assets/kanban.scss';
</style>