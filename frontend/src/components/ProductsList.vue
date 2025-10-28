<script setup>
import Product from '@/components/Product.vue'

const props = defineProps({ products: { type: Array, default: () => [] } })
</script>

<template>
    <div class="grid">
        <Product v-for="product in props.products" :key="product.id" :image_url="product.image_url"
            :price="product.price" :shop_url="product.shop_url" :shop_domain="product.shop_domain" />
    </div>
    <div ref="bottom" style="height: 1px;"></div>
</template>

<style>
:root {
    --gap: 5px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--gap);
    padding-top: 90px;
}

@media (min-width: 427px) {
    .grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: var(--gap);
    }
}

@media (min-width: 601px) {
    .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: var(--gap);
    }
}

@media (min-width: 1131px) {
    .grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: var(--gap);
    }
}
</style>