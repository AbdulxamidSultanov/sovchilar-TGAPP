import { useEffect } from "react";

function App() {
    useEffect(() => {
        const WebApp = window.Telegram.WebApp;
        WebApp.ready();
        WebApp.expand();
    }, []);

    return (
        <div>
            <h1>Привет, {window.Telegram.WebApp?.initDataUnsafe?.user?.first_name || "Гость"}!</h1>
            <button onClick={() => window.Telegram.WebApp.close()}>Закрыть</button>
        </div>
    );
}

export default App;
