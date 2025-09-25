<script setup>
import axios from 'axios'

const emit = defineEmits(['goodsData'])

const image_url = defineModel('image_url')
const fetchGoods = async () => {
    try {
        const data = await axios.get('https://ease-vojh.onrender.com/goods/', {
            params: {
                image_url: image_url.value
            }
        })
        emit('goodsData', data.data)
    } catch (err) {
        console.log(err)
    }
}
</script>

<template>
    <div class="search" role="search">
        <svg @click="fetchGoods" width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden>
            <path d="M21 21l-4.35-4.35" stroke="#666" stroke-width="1.6" stroke-linecap="round"
                stroke-linejoin="round" />
            <circle cx="11" cy="11" r="6" stroke="#666" stroke-width="1.6" stroke-linecap="round"
                stroke-linejoin="round" />
        </svg>
        <input @keyup.enter="fetchGoods" v-model="image_url" id="q" placeholder="link to the image" />
    </div>
</template>

<style>
.search {
    display: flex;
    align-items: center;
    background: linear-gradient(180deg,
            rgba(255, 255, 255, 0.9),
            rgba(250, 250, 250, 0.9));
    border-radius: 999px;
    padding: 12px 16px;
    gap: 12px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(10, 10, 10, 0.06) inset;
}

.search input {
    border: 0;
    outline: 0;
    background: transparent;
    font-size: 15px;
    flex: 1;
    color: #333;
}

svg {
    cursor: pointer;
}
</style>