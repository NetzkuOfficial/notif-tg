import os
from dotenv import load_dotenv
from telethon import TelegramClient, events, errors
import asyncio

# Memuat variabel dari file .env
load_dotenv()

# Mengambil variabel dari environment dan memastikan semuanya ada
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
bot_token = os.getenv('BOT_TOKEN')
log_file = "processed_messages.log"

# Cek apakah semua variabel lingkungan sudah diatur
if not all([api_id, api_hash, phone_number, bot_token]):
    raise ValueError("Pastikan semua variabel lingkungan API_ID, API_HASH, PHONE_NUMBER, dan BOT_TOKEN sudah diatur di file .env")

# Membuat klien untuk akun pengguna
client_user = TelegramClient('sesi-user', api_id, api_hash)

# Membuat klien untuk bot
client_bot = TelegramClient('sesi-bot', api_id, api_hash).start(bot_token=bot_token)

# Fungsi untuk memeriksa apakah pesan sudah diproses
def is_message_processed(chat_id, message_id):
    # Kombinasi unik dari chat_id dan message_id
    unique_id = f"{chat_id}_{message_id}"
    try:
        with open(log_file, "r") as file:
            processed_ids = file.read().splitlines()
            return unique_id in processed_ids
    except FileNotFoundError:
        return False

# Fungsi untuk mencatat pesan yang sudah diproses
def log_message(chat_id, message_id):
    unique_id = f"{chat_id}_{message_id}"
    with open(log_file, "a") as file:
        file.write(unique_id + "\n")
    # Batasi ukuran file log
    manage_log_file_size()

# Fungsi untuk mengelola ukuran file log
def manage_log_file_size():
    max_size = 2 * 1024 * 1024  # 2MB
    reset_size = 5 * 1024 * 1024  # 5MB

    if os.path.getsize(log_file) > reset_size:
        # Baca seluruh konten log
        with open(log_file, "r") as file:
            lines = file.readlines()
            
        # Ambil hanya entri terbaru hingga batas 2MB
        with open(log_file, "w") as file:
            file.writelines(lines[-max_size//len(lines[0]):])

# Fungsi untuk mendapatkan id kita menggunakan client_user
async def get_user_id(client):
    # Mendapatkan informasi pengguna
    me = await client.get_me()
    # Mengembalikan ID pengguna sebagai integer
    return me.id

@client_user.on(events.NewMessage)
async def my_event_handler(event):
    # Mendapatkan ID chat dan teks pesan
    chat_id = event.chat_id
    message_id = event.message.id
    sender_id = event.sender_id
    message_text = event.message.message

    # Periksa apakah pesan dikirim oleh bot sendiri
    if sender_id == (await client_bot.get_me()).id:
        return  # Jika pesan dikirim oleh bot sendiri, abaikan

    # Periksa apakah pesan sudah diproses sebelumnya
    if is_message_processed(chat_id, message_id):
        return  # Jika sudah diproses, tidak perlu memproses lagi

    # Catat pesan yang sudah diproses
    log_message(chat_id, message_id)

    # Membuka file dan membaca isinya per baris
    with open("daftar_id.txt", "r") as file:
        id_identifikasi = [line.strip() for line in file]

    # Memeriksa apakah incoming_message mengandung salah satu id sender
    if any(id_ in message_text for id_ in id_identifikasi):
        print(f"Pesan diterima dari: {chat_id}, dengan isi pesan: {message_text}")
        try:
            # Mengambil ID pengguna dari sesi user (bukan bot)
            user_id = await get_user_id(client_user)
            # Mengirim ulang pesan ke akun pengguna utama menggunakan bot
            await client_bot.send_message(user_id, f"Dari `{sender_id}`\nIsi : `{message_text}`")
            print(f"Pesan telah dikirim ulang ke: {user_id} atas nama bot")
        except Exception as e:
            print(f"Error saat mengirim pesan: {e}")

async def start_clients():
    try:
        await client_user.start(phone_number)
        print("Klien pengguna sudah berjalan...")
        await client_bot.start()  # Menjalankan bot
        print("Klien bot sudah berjalan...")
        await client_user.run_until_disconnected()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        await asyncio.sleep(5)  # Tunggu beberapa detik sebelum mencoba kembali
        await start_clients()  # Coba ulangi koneksi

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_clients())
