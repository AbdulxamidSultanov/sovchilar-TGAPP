import React from 'react'
import { useTelegram } from "@vkruglikov/react-telegram-web-app";

function App() {
  const { WebApp } = useTelegram();

    useEffect(() => {
        WebApp.ready();  // Инициализация WebApp API
        WebApp.expand(); // Разворачивает WebApp на весь экран
    }, []);
  return (
    <div>
    <h1>Привет, {WebApp.initDataUnsafe?.user?.first_name || "Гость"}!</h1>
    <button onClick={() => WebApp.close()}>Закрыть</button>
</div>
  )
}

export default App