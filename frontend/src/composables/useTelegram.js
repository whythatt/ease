import { ref, onMounted } from "vue";

export function useTelegram() {
  const tg = window.Telegram?.WebApp;

  // Данные пользователя
  const user = ref(null);

  // Инициализация
  const init = () => {
    // Расширяем на весь экран
    tg.expand();

    // Получаем данные пользователя
    if (tg.initDataUnsafe?.user) {
      user.value = tg.initDataUnsafe.user;
      console.log("Данные пользователя:", user.value);
    } else {
      console.log("Данные пользователя не получены");
    }

    return true;
  };

  // Отправить данные в бота
  const sendData = (data) => {
    if (tg) {
      tg.sendData(JSON.stringify(data));
    }
  };

  onMounted(() => {
    init();
  });

  return {
    user,
    sendData,
    tg,
  };
}
