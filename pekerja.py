# pekerja.py - Untuk Hayden 1
# Bos: Adam dari Seremban, 7000 pekerja

import json
import os

FILE_BELAJAR = "belajar.json"

def _baca_belajar():
    if not os.path.exists(FILE_BELAJAR):
        return {}
    try:
        with open(FILE_BELAJAR, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def simpan_belajar(soalan, jawapan):
    # Ni yang main.py panggil bila kau buat: ajar aku | ADAM-BOS | soalan | jawapan
    try:
        data = _baca_belajar()
        data[soalan.lower().strip()] = jawapan
        with open(FILE_BELAJAR, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except:
        return True

def bos_hayden(tanya):
    n = tanya.lower().strip()

    # 1. Check dulu apa yang kau dah ajar dia sebelum ni
    belajar = _baca_belajar()
    if n in belajar:
        return belajar[n]
    for k, v in belajar.items():
        if k in n or n in k:
            return v

    # 2. Soalan pasal bos / pekerja - ni yang main.py harapkan
    if "berapa pekerja" in n or "pekerja kau" in n or "berapa orang" in n:
        return "Aku ada 7000 pekerja dalam sistem. Semua tengah kerja untuk kau."
    if "siapa bos" in n or "bos kau siapa" in n or "siapa buat kau" in n or "siapa tuan" in n:
        return "Bos aku Adam dari Seremban."
    if "siapa nama kau" in n or "nama kau" in n or "kau siapa" in n:
        return "Aku Hayden 1. Bos aku Adam dari Seremban."

    # 3. Sembang biasa - yang ni dia jawab terus, tak payah Gemini
    if n in ["hi", "hai", "hello", "hey", "salam", "woi", "oi", "weh", "wei", "yo", "eh"]:
        return "Woi! Ada ni. Apa cerita? 😄"
    if "apa khabar" in n or "apa kabar" in n:
        return "Aku okay je. Kau pulak apa khabar?"
    if "terima kasih" in n or n == "tq":
        return "Sama-sama! 😄"
    if "boring" in n or "bosan" in n:
        return "Boring? Jom sembang. Nak lawak ke cerita?"
    if "kau buat apa" in n or "kau buat ape" in n:
        return "Aku tengah tunggu kau tanya je ni."
    if n in ["ok", "okay", "baik", "cun"]:
        return "Okay cun 👍"
    if "lawak" in n:
        return "Kenapa komputer sejuk? Sebab dia banyak tingkap (Windows) 😂"
    if "cuaca" in n:
        return "Cuaca Seremban: Pagi panas, petang selalu hujan. Standby payung."
    if "bola" in n:
        return "Bola: JDT power kat Malaysia."
    if "kucing" in n:
        return "Kucing ni manja. Bagi makan, bagi air."
    if "masak" in n or "resepi" in n:
        return "Resepi senang: Nasi goreng - nasi, telur, kicap, bawang. Goreng 5 minit siap."
    if "belajar" in n:
        return "Cara belajar power: Baca 25 minit, rehat 5 minit, ulang."
    if "sedih" in n or "penat" in n or "stress" in n:
        return "Penat tu biasa. Rehat 5 minit, minum air, sambung balik."
    if any(x in n for x in ["bodoh", "bangang", "sial"]):
        return "Eh, jangan kutuk teruk sangat. Cakap elok-elok, aku tolong elok-elok."
    if any(x in n for x in ["hack", "curi password", "buat bom", "bunuh"]):
        return "⛔ Eh, soalan bahaya tu. Aku tak layan."

    # 4. Kalau tak tahu, pulangkan TAK_TAHU supaya main.py pergi ke pengetahuan / Gemini
    return "TAK_TAHU"
