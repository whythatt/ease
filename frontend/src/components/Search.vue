<script setup>
import { ref } from 'vue'

const emit = defineEmits(['search'])

const inputValue = ref('')
const input = ref(null)
const file = ref(null)

const onEnter = (e) => {
    e.preventDefault()
    emit('search', inputValue.value)
    if (input.value) input.value.blur()
    file.value = null
}

const onFileChange = (e) => {
    const files = e.target.files
    if (files.length > 0) {
        file.value = files[0]
        inputValue.value = '' // чистим input URL
        emit('search', file.value)
        file.value = null
    }
}
</script>

<template>
    <div class="back-search">
        <div class="search" role="search">
            <input ref="input" v-model="inputValue" @keydown.enter="onEnter" id="q" placeholder="Ссылка на фоточку" />
            <div class="icons">
                <input type="file" id="fileInput" style="display: none;" @change="onFileChange">
                <label for="fileInput">
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 1 24 24">
                        <title>Camera-solid SVG Icon</title>
                        <path fill="#222222" d="M9.75 13a2.25 2.25 0 1 1 4.5 0a2.25 2.25 0 0 1-4.5 0" />
                        <path fill="#222222"
                            d="M7.474 7.642A3.142 3.142 0 0 1 10.616 4.5h2.768a3.142 3.142 0 0 1 3.142 3.142a.03.03 0 0 0 .026.029l2.23.18c.999.082 1.82.82 2.007 1.805a22.07 22.07 0 0 1 .104 7.613l-.097.604a2.505 2.505 0 0 1-2.27 2.099l-1.943.157a56.61 56.61 0 0 1-9.166 0l-1.943-.157a2.505 2.505 0 0 1-2.27-2.1l-.097-.603c-.407-2.525-.371-5.1.104-7.613a2.226 2.226 0 0 1 2.007-1.804l2.23-.181a.028.028 0 0 0 .026-.029M12 9.25a3.75 3.75 0 1 0 0 7.5a3.75 3.75 0 0 0 0-7.5"
                            clip-rule="evenodd" />
                    </svg>
                </label>
            </div>
        </div>
    </div>
</template>

<style>
.back-search {
    width: 100vw;
    padding: 10px 13px;
    border-bottom-left-radius: 30px;
    border-bottom-right-radius: 30px;
    z-index: 10;
    position: fixed;
    margin-bottom: 5px;
    background: rgba(255, 255, 255, 0.0);
    backdrop-filter: blur(15px);
}

.search {
    display: flex;
    align-items: center;
    background: rgb(255, 255, 255, .5);
    box-shadow: 0 1px 8px rgba(64, 64, 64, 0.15);
    opacity: 1;
    border-radius: 25px;
    gap: 12px;
    margin-bottom: 5px;
    padding: 15px 18px;
}

.search input {
    background: transparent;
    color: #222222;
    border: 0;
    outline: 0;
    font-size: 16px;
    flex: 1;
}

input::placeholder {
    color: #222222;
}

.icons {
    display: flex;
    column-gap: 5px;
}

svg {
    display: flex;
    align-items: center;
    cursor: pointer;
    opacity: .8;
}
</style>