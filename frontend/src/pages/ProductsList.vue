<script setup>
import { ref } from 'vue'
import Search from '@/components/Search.vue'
import Product from '@/components/Product.vue'

const goodsData = ref({})

const handleGoodsData = (data) => {
    goodsData.value = data
    console.log(data)
}
</script>

<template>
    <div class="frame">
        <Search @goods-data="handleGoodsData"></Search>
        <div class="grid">
            <Product v-for="product in goodsData.products" :key="product.id" :image_url="product.image_url"
                :price="product.price" :shop_url="product.shop_url" :shop_domain="product.shop_domain" />
        </div>
    </div>
</template>

<style>
.frame {
    width: 380px;
    background: rgba(255, 255, 255, 0.7);
}

.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--gap);
}

@media (max-width: 420px) {
    .frame {
        width: 92vw;
        padding: 14px;
    }
}
</style>