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
    background: white;
    font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto,
        "Helvetica Neue", Arial;
    padding-top: env(safe-area-inset-top);
    padding-bottom: env(safe-area-inset-bottom);
}
</style>
