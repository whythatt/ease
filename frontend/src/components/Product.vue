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
    cursor: pointer;
    border-radius: 18px;
    overflow: hidden;
    background: var(--tg-theme-bg-color);
    box-shadow: 0 6px 18px rgba(10, 10, 10, 0.06);
    position: relative;
}

.image-wrapper {
    position: relative;
    width: 100%;
    max-height: 180px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    background: var(--tg-theme-bg-color);
}

.image-wrapper .image {
    width: 100%;
    height: auto;
    max-height: 100%;
    object-fit: contain;
    object-position: center;
    display: block;
}

.card .meta {
    position: absolute;
    bottom: 10px;
    left: 10px;
    z-index: 2;
    background: var(--tg-theme-bg-color);
    opacity: 0.4;
    color: var(--tg-theme-text-color);
    padding: 5px 5px;
    border-radius: 8px;
    max-width: 90%;
}

.price {
    color: var(--tg-theme-text-color);
    border-radius: 10px;
    font-weight: 600;
    font-size: 11px;
}

.source {
    font-size: 10px;
    color: var(--tg-theme-text-color);
}


@media (min-width: 374px) {
    .image-wrapper {
        max-height: 220px;
    }

    .source {
        font-size: 10px;
    }

    .price {
        font-size: 11px;
    }
}

@media (min-width: 427px) {
    .image-wrapper {
        max-height: 150px;
    }

    .source {
        font-size: 10px;
    }

    .price {
        font-size: 11px;
    }
}

@media (min-width: 501px) {
    .image-wrapper {
        max-height: 200px;
    }
}

@media (min-width: 601px) {
    .image-wrapper {
        max-height: 180px;
    }

    .source {
        font-size: 10px;
    }

    .price {
        font-size: 11px;
    }
}

@media (min-width: 701px) {
    .image-wrapper {
        max-height: 210px;
    }
}

@media (min-width: 831px) {
    .image-wrapper {
        max-height: 255px;
    }

    .source {
        font-size: 12px;
    }

    .price {
        font-size: 13px;
    }
}

@media (min-width: 911px) {
    .image-wrapper {
        max-height: 285px;
    }

    .source {
        font-size: 15px;
    }

    .price {
        font-size: 16px;
    }
}

@media (min-width: 1385px) {
    .image-wrapper {
        max-height: 350px;
    }

    .source {
        font-size: 18px;
    }

    .price {
        font-size: 19px;
    }
}
</style>