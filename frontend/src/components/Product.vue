<script setup>
const props = defineProps({
    image_url: String,
    price: String,
    shop_url: String,
    shop_domain: String
})

const openShopUrl = (shop_url) => {
    window.open(shop_url, '_blank', 'noopener,noreferrer')
}
</script>

<template>
    <div class="card" @click="openShopUrl(shop_url)">
        <div class="image-wrapper">
            <img :src="image_url" alt="Product image" class="image" />
        </div>
        <div class="meta">
            <div class="price">{{ price }} ₽</div>
            <div class="source">{{ shop_domain }}</div>
        </div>
    </div>
</template>

<style>
.card {
    border-radius: 18px;
    overflow: hidden;
    background: white;
    box-shadow: 0 6px 18px rgba(10, 10, 10, 0.06);
    position: relative;
}

.image-wrapper {
    position: relative;
    width: 100%;
    height: auto;
    max-height: 200px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: flex-end;
}

.image-wrapper .image {
    width: 100%;
    height: auto;
    margin: auto 0px;
    max-height: 200px;
    object-fit: contain;
    object-position: center;
    display: block;
}

.card .meta {
    position: absolute;
    bottom: 10px;
    left: 10px;
    z-index: 2;
    background: rgba(0, 0, 0, 0.4);
    color: white;
    padding: 5px 5px;
    border-radius: 8px;
    max-width: 90%;
}

.price {
    color: white;
    border-radius: 10px;
    font-weight: 600;
    font-size: 14px;
}

.source {
    font-size: 13px;
    color: white;
}


@media (max-width: 420px) {
    .source {
        font-size: 10px;
    }

    .price {
        font-size: 11px;
    }
}
</style>