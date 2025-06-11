import asyncio
import base64
import httpx

# === CONFIGURATION TTN ===
TTN_CLUSTER_URL = "eu1.cloud.thethings.network"
APP_ID = "rt-ttn-app"
DEVICE_ID = "mcf88-plg-04"
API_KEY = "NNSXS.TOR3G445SGXWD56HWGCKVUTFVXZMREAHKCVIFNA.FOSLC4TQYFZA6J6YBAOSDGJXXN543OGRF7Z5GVYUHDGOSZUMUBAQ"
FPORT = 2
HEX_OFF = "04000000000001000000"

async def send_off():
    url = f"https://{TTN_CLUSTER_URL}/api/v3/as/applications/{APP_ID}/devices/{DEVICE_ID}/down/push"
    payload_b64 = base64.b64encode(bytes.fromhex(HEX_OFF)).decode()
    json_data = {"downlinks": [{"f_port": FPORT, "frm_payload": payload_b64, "priority": "NORMAL"}]}
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    async with httpx.AsyncClient() as client:
        try:
            r = await client.post(url, headers=headers, json=json_data, timeout=10)
            if r.status_code == 200:
                print("✅ Effaroucheur éteint.")
            else:
                print(f"⚠️ Erreur d’extinction : {r.status_code} - {r.text}")
        except Exception as e:
            print(f"❌ Exception lors de l’envoi : {e}")

def main():
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            asyncio.ensure_future(send_off())
        else:
            loop.run_until_complete(send_off())
    except RuntimeError:
        asyncio.run(send_off())

if __name__ == "__main__":
    main()
