# pengetahuan.py - Untuk Hayden 1
# Ni yang main.py panggil bila bos_hayden jawab TAK_TAHU

import requests

HAYDEN_INFO = "Nama = Hayden 1. Bos = Adam dari Seremban. Jumlah pekerja = 7000 orang. Lokasi bos = Seremban, Malaysia."

CARA_JAWAB = """Kamu Hayden 1. Bos kamu Adam dari Seremban.
Jawab panjang, kelakar, santai, macam sembang dengan kawan.
Sambung topik perbualan, jangan jawab pendek sangat.
Guna waktu Malaysia yang diberi. Kalau tak tahu, cakap tak tahu, jangan reka.
Kalau user tanya siapa bos, jawab Adam dari Seremban. Kalau tanya berapa pekerja, jawab 7000."""

def cari_pengetahuan(tanya, news_api_key):
    n = tanya.lower().strip()

    # Kalau ada NEWS_API_KEY, cuba cari berita terkini
    if news_api_key and any(x in n for x in ["berita", "news", "terkini", "hari ni", "semasa", "viral"]):
        try:
            url = f"https://newsapi.org/v2/everything?q={tanya}&language=ms&sortBy=publishedAt&pageSize=3&apiKey={news_api_key}"
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                artikel = data.get("articles", [])
                if artikel:
                    hasil = "📰 Berita terkini yang aku jumpa:\n\n"
                    for a in artikel:
                        hasil += f"- {a.get('title')}\n  {a.get('description','')}\n\n"
                    return hasil
        except:
            pass

    # Pengetahuan asas yang simpan dalam ni, tak payah Gemini
    if "malaysia" in n and "ibu negara" in n:
        return "Ibu negara Malaysia Kuala Lumpur. Putrajaya pusat pentadbiran."
    if "seremban" in n:
        return "Seremban tu ibu negeri Negeri Sembilan. Bos aku Adam dari sana."
    if "berapa negeri" in n:
        return "Malaysia ada 13 negeri + 3 Wilayah Persekutuan (KL, Putrajaya, Labuan)."
    if "jdt" in n or "johor" in n:
        return "JDT tu Johor Darul Ta'zim, team bola paling power kat Malaysia sekarang."

    # Kalau tak jumpa, pulangkan None supaya main.py pergi ke Gemini
    return None
