<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import axios from 'axios'
import debounce from 'lodash/debounce'
import Search from '@/components/Search.vue'
import ProductsList from '@/components/ProductsList.vue'

const goods = ref([])
const page = ref(1)
const limit = 30
const loading = ref(false)
const noMore = ref(true)
const bottom = ref(null)
const imageUrl = ref('')
const imageFile = ref('')

const onSearch = (payload) => {
    if (typeof payload === 'string') {
        imageUrl.value = payload
        imageFile.value = null
    } else {
        imageFile.value = payload
        imageUrl.value = ''
    }
    goods.value = []
    page.value = 1
    noMore.value = false
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
            response = await axios.post('https://ease-d09bf.web.app/goods/', formData)
            imageUrl.value = response.data.image_url
        }
        response = await axios.get('https://ease-d09bf.web.app/goods/', {
            params: { image_url: imageUrl.value, page: page.value, limit },
        })
        const data = response.data
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

const debouncedFetchGoods = debounce(fetchGoods, 150)

const observerCallback = (entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting && !loading.value && !noMore.value) {
            debouncedFetchGoods()
        }
    })
}

let observer = null

onMounted(() => {
    observer = new IntersectionObserver(observerCallback, {
        root: null,
        threshold: 0.1,
    })
    if (bottom.value) observer.observe(bottom.value)
    // УБРАН вызов fetchGoods() из onMounted, загрузка только по поиску
})

onBeforeUnmount(() => {
    debouncedFetchGoods.cancel()
    if (observer && bottom.value) observer.unobserve(bottom.value)
})
</script>

<template>
    <Search @search="onSearch" />
    <div class="frame">
        <ProductsList :products="goods" />
    </div>
    <div v-if="loading" class="loading">Загрузка...</div>
    <div ref="bottom" style="height: 1px;" id="for-scroll"></div>
</template>

<style>
.frame {
    margin: 20px 10px;
}

.loading {
    margin: 10px auto;
    width: fit-content;
}
</style>