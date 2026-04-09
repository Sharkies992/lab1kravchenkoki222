from google import genai
import os

# Створюємо клієнта
client = genai.Client(api_key="AIzaSyCNFuTWmRfcsAb7ezosUN2BNXioVSdJ8UU")

# Запит до моделі
response = client.models.generate_content(
    model="gemini-2.0-flash", # Використовуємо актуальну модель 2.0
    contents="Напиши код для простого сайту-візитки студента. "
             "Мені потрібен окремо вміст для index.html та окремо для style.css."
)

print(response.text)