import json
import random

# Günlük kelime havuzu
word_pool = [
    {"fr": "Apprendre", "tr": "Öğrenmek", "example": "J'aime apprendre le français."},
    {"fr": "Voyager", "tr": "Seyahat etmek", "example": "Nous aimons voyager en France."},
    {"fr": "Manger", "tr": "Yemek yemek", "example": "Je veux manger un croissant."},
    {"fr": "Parler", "tr": "Konuşmak", "example": "Parlez-vous français?"},
    {"fr": "Écouter", "tr": "Dinlemek", "example": "J'écoute de la musique française."},
    {"fr": "Comprendre", "tr": "Anlamak", "example": "Je comprends très bien."}
]

def update_daily_data():
    try:
        # Mevcut data.json dosyasını oku
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        data = {"kategoriler": []}

    # Günün kelimesini rastgele seçip güncelle
    selected_word = random.choice(word_pool)
    data["gunun_kelimesi"] = selected_word

    # Güncellenmiş veriyi tekrar dosyaya yaz
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Günün kelimesi başarıyla güncellendi: {selected_word['fr']}")

if __name__ == "__main__":
    update_daily_data() 