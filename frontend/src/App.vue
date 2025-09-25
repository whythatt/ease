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
    font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto,
        "Helvetica Neue", Arial;
    color: var(--tg-theme-text-color);
    background: var(--tg-theme-bg-color);
    padding-top: calc(40px + env(safe-area-inset-top));
    padding-bottom: calc(12px + env(safe-area-inset-bottom));
}
</style>
