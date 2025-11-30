import { useState } from "react";

export default function Home() {
  const [steamid, setSteamid] = useState("");
  const [items, setItems] = useState([]);

  const fetchInventory = async () => {
    const res = await fetch(
      `https://<your-render-backend-url>/inventory/${steamid}`
    );
    const data = await res.json();
    setItems(data.descriptions || []);
  };

  return (
    <div className="p-10 text-center">
      <h1 className="text-3xl font-bold">CS2 库存面板</h1>

      <input
        value={steamid}
        onChange={(e) => setSteamid(e.target.value)}
        className="mt-5 p-2 w-80 border"
        placeholder="输入 SteamID64"
      />
      <button onClick={fetchInventory} className="ml-3 px-4 py-2 bg-blue-500 text-white">
        查询
      </button>

      <div className="grid grid-cols-5 gap-4 mt-10">
        {items.map((item, idx) => (
          <div key={idx} className="p-4 bg-[#0f172a] text-white rounded-xl shadow">
            <img src={item.icon_url_large ? 
              `https://steamcommunity-a.akamaihd.net/economy/image/${item.icon_url_large}`
              : ""} />

            <div className="mt-2 font-bold">{item.market_hash_name}</div>

            <div className="text-pink-400 mt-3">Buff 实时价：查询中...</div>
            <div className="text-green-400">Steam 价：查询中...</div>
          </div>
        ))}
      </div>
    </div>
  );
}
