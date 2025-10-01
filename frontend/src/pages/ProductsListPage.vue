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
const imageFile = ref('')

const onSearch = (payload) => {
    if (typeof payload === 'string') {
        // Поиск по URL
        imageUrl.value = payload
        imageFile.value = null
    } else {
        // Поиск по файлу
        imageFile.value = payload
        imageUrl.value = ''
    }
    goods.value = []
    page.value = 1
    noMore.value = false
    canLoadMore.value = true
    fetchGoods()
}

const fetchGoods = async () => {
    if (loading.value || noMore.value) return
    loading.value = true
    try {
        let response
        if (imageFile.value && !imageUrl.value) {
            const formData = new FormData()
            formData.append('file', imageFile.value)
            console.log('делаю это опять')
            response = await axios.post('https://ease-vojh.onrender.com/goods/', formData)
            imageUrl.value = response.data.image_url
        }
        response = await axios.get('https://ease-vojh.onrender.com/goods/', {
            params: { image_url: imageUrl.value, page: page.value, limit }
        })
        const data = response.data
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
    <div v-if="loading" class="loading">Загрузка...</div>
    <div ref="bottom" style="height: 1px;"></div>
</template>

<style>
.frame {
    margin: 20px 10px;
}

.loading {
    margin: 10px auto;
    width: fit-content
}
</style>