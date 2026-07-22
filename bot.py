import requests

TOKEN = " 8479783686:AAEjLz-nc8jULTTnHOJQeMKMt06GqeFLJak"
CHAT_ID = "5840426117"

message = "ربات طلا فعال شد ✅"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.get(url, params={
    "chat_id": CHAT_ID,
    "text": message
})

print("Message sent")
