Smart Farm API Loyihasi Tushuntirishi
Loyiha Nima Haqida?
Bu Smart Farm (Aqlli Ferma) boshqaruv tizimi uchun API. Loyiha fermerlar yoki qishloq xo'jaligi korxonalari uchun mo'ljallangan. Tizim orqali fermadagi sensorlar va qurilmalarni masofadan boshqarish va monitoring qilish mumkin.

Asosiy Komponentlar:
1. Sensor (Sensor)
Vazifasi: Atrof-muhit parametrlarini o'lchash

Turlari:

Harorat sensor - temperature

Namlik sensor - humidity

Tuproq namligi sensor - soil_moisture

Yorug'lik sensor - light

Qanday ishlaydi: Har bir sensor ma'lum vaqt oralig'ida o'lchovlar olib, ma'lumotlar bazasiga yozadi

2. SensorData (Sensor Ma'lumotlari)
Vazifasi: Sensorlardan kelgan ma'lumotlarni saqlash

Qanaqa ma'lumotlar: Har bir o'lchov qiymati (value) va vaxt belgisi (timestamp)

Misollar:

Harorat: 25.5°C

Tuproq namligi: 60%

Yorug'lik darajasi: 1200 lux

3. Device (Qurilma)
Vazifasi: Fermani avtomatik boshqarish

Turlari:

Nasos (suv pompası) - pump

Ventilyator - fan

Yoritgich - light

Isitgich - heater

Qanday ishlaydi: API orqali yoqish/o'chirish (is_active) bilan boshqariladi

Haqiqiy Dunyoda Qanday Ishlasa Bo'ladi?
Misol: Tomatlar yetishtiriladigan issiqxona

Sensorlar doimiy harorat, namlik va tuproq holatini o'lchaydi

API orqali fermer:

Ma'lumotlarni ko'radi (telefon yoki kompyuterda)

Harorat 30°C dan oshsa - ventilyatorni yoqadi

Tuproq qurisa - nasosni yoqib suv beradi

Tun bo'lsa - yoritgichlarni yoqadi

API Endpointlar:
GET /api/sensors/ - Barcha sensorlarni ko'rish

POST /api/sensors/ - Yangi sensor qo'shish

GET /api/sensor-data/ - Barcha o'lchovlarni ko'rish

GET /api/devices/ - Barcha qurilmalarni ko'rish

PUT /api/devices/1/ - Qurilmani yoqish/o'chirish

Loyihani Rivojlantirish Mumkin:
Telegram bot qo'shish (ogohlantirishlar yuborish)

Mobile app yaratish

Ma'lumotlarni grafikalarda ko'rsatish

Avtomatik boshqarish qoidalari qo'shish

Bu loyiha haqiqatan ham fermerlar va qishloq xo'jaligi uchun foydali bo'lishi mumkin! 🌱🚜
