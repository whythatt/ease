<script setup>
const props = defineProps({
    image_url: String,
    price: String,
    shop_url: String,
    shop_domain: String
})

const openShopUrl = () => {
    window.open(shop_url, '_blank', 'noopener,noreferrer')
}
</script>

<template>
    <div class="card" @click="openShopUrl">
        <img :src="image_url" alt="Product image" />
        <div class="meta">
            <div class="price">{{ price }}</div>
            <div class="source">{{ shop_domain }}</div>
        </div>
    </div>
</template>

<style>
.card {
    border-radius: 18px;
    overflow: hidden;
    background: white;
    display: flex;
    flex-direction: column;
    /* justify-content: flex-end; */
    box-shadow: 0 6px 18px rgba(10, 10, 10, 0.06);
}

img {
    width: 100%;
    height: auto;
    display: block;
}

.meta {
    position: relative;
    z-index: 2;
    padding: 12px 14px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
}

.price {
    background: linear-gradient(90deg, rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.55));
    color: white;
    padding: 6px 10px;
    border-radius: 10px;
    font-weight: 600;
    font-size: 15px;
}

.source {
    font-size: 14px;
    color: white;
}


@media (max-width: 420px) {
    .source {
        font-size: 12px;
    }

    .price {
        font-size: 13px;
    }
}
</style>