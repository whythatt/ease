<script setup>
import axios from 'axios'
import { ref } from 'vue'

const emit = defineEmits(['goodsData'])

const image_url = defineModel('image_url')
const searchInput = ref(null)
const fetchGoods = async () => {
    try {
        const data = await axios.get('https://ease-vojh.onrender.com/goods/', {
            params: {
                image_url: image_url.value
            }
        })
        emit('goodsData', data.data)
        if (searchInput.value) searchInput.value.blur()
    } catch (err) {
        console.log(err)
    }
}

const onEnter = (event) => {
    event.preventDefault()
    fetchGoods()
}
</script>

<template>
    <div class="search" role="search">
        <input ref="searchInput" v-model="image_url" @keydown.enter="onEnter" id="q" placeholder="link to the image" />
        <svg @click="fetchGoods" width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden>
            <path d="M21 21l-4.35-4.35" stroke="#666" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            <circle cx="11" cy="11" r="6" stroke="#666" stroke-width="2" stroke-linecap="round"
                stroke-linejoin="round" />
        </svg>
    </div>
</template>

<style>
.search {
    display: flex;
    align-items: center;
    border: rgba(213, 213, 213, 0.9) 1px solid;
    border-radius: 999px;
    background: linear-gradient(180deg,
            rgba(255, 255, 255, 0.9),
            rgba(250, 250, 250, 0.9));
    gap: 12px;
    margin-bottom: 13px;
    padding: 15px 18px;
}

.search input {
    background: transparent;
    color: #333;
    border: 0;
    outline: 0;
    font-size: 16px;
    flex: 1;
}

svg {
    cursor: pointer;
}
</style>