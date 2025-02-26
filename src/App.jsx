import React, { useEffect } from "react";

function App() {
    useEffect(() => {
        const WebApp = window.Telegram.WebApp;
        WebApp.ready();
        WebApp.expand();
    }, []);

    return (
        <div className="bg-white h-[100vh] ">
            <h1>Привет, {window.Telegram.WebApp?.initDataUnsafe?.user?.first_name || "Гость"}!</h1>
            <button className="border px-4 py-2 rounded-md text-white bg-black" onClick={() => window.Telegram.WebApp.close()}>Закрыть</button>
        </div>
    );
}

export default App;

