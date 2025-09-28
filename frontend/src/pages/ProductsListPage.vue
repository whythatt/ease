<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import axios from 'axios'
import Search from '@/components/Search.vue'
import ProductsList from '@/components/ProductsList.vue'

const goods = ref([])
const page = ref(1)
const limit = 30
const loading = ref(false)
const noMore = ref(false)
const bottom = ref(null)
const canLoadMore = ref(false)
const imageUrl = ref('')

const onSearch = (newImageUrl) => {
    imageUrl.value = newImageUrl
    goods.value = []
    page.value = 1
    noMore.value = false
    canLoadMore.value = true // разрешаем подгрузку по скроллу
    fetchGoods()
}

const fetchGoods = async () => {
    if (loading.value || noMore.value) return

    loading.value = true
    try {
        const { data } = await axios.get('https://ease-vojh.onrender.com/goods/', {
            params: { image_url: imageUrl.value, page: page.value, limit }
        })
        console.log(data)
        if (data.products.length < limit) noMore.value = true
        goods.value.push(...data.products)
        page.value++
    } catch (e) {
        console.error(e)
    } finally {
        loading.value = false
    }
}

const observerCallback = (entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !loading.value && !noMore.value && canLoadMore.value) {
            fetchGoods()
        }
    })
}

let observer = null

onMounted(() => {
    observer = new IntersectionObserver(observerCallback, {
        root: null,
        threshold: 1.0
    })
    if (bottom.value) observer.observe(bottom.value)
})

onBeforeUnmount(() => {
    if (observer && bottom.value) observer.unobserve(bottom.value)
})
</script>

<template>
    <Search @search="onSearch" />
    <div class="frame">
        <ProductsList :products="goods" />
    </div>
    <div ref="bottom" style="height: 1px;"></div>
    <div v-if="loading">Загрузка...</div>
</template>

<style>
.frame {
    margin: 20px 10px;
}
</style>