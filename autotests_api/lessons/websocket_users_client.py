import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"  # Сообщение, которое отправит клиент
        print(f"Отправка: {message}")
        await websocket.send(message)  # Отправляем сообщение
        for i in range(1, 6):
            response = await websocket.recv()  # Получаем ответ от сервера
            print(f"Ответ от сервера: {i} {response}")

asyncio.run(client())