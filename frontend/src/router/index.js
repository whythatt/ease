import { createMemoryHistory, createRouter } from "vue-router";

const router = createRouter({
  history: createMemoryHistory(),
  routes: [
    {
      path: "/",
      name: "goodsList",
      component: () => import("@/pages/ProductsList.vue"),
    },
  ],
});

export default router;
