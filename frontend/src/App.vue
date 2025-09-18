<script setup>
</script>

<template>
    <RouterView />
</template>

<style>
:root {
    --bg: #eef1f3;
    --card-radius: 18px;
    --gap: 5px;
}

* {
    box-sizing: border-box;
}

html,
body {
    height: 100%;
    margin: 0;
    font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto,
        "Helvetica Neue", Arial;
    color: #222;
}

body {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    display: flex;
    align-items: flex-start;
    justify-content: center;
}
</style>
