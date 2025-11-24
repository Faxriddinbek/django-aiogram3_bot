from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="🇺🇿 O'zbekcha"),
        KeyboardButton(text="🇷🇺 Русский"),
        KeyboardButton(text="🇺🇸 English"),
    ]], resize_keyboard=True
)

city = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Toshkent"), KeyboardButton(text="Farg'ona")],
        [KeyboardButton(text="Marg'ilon"), KeyboardButton(text="Chirchiq")],
        [KeyboardButton(text="Andijon"), KeyboardButton(text="Buxoro")],
        [KeyboardButton(text="Nukus"), KeyboardButton(text="Qo'qon")],
    ],
    resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Buyurtma berish")],
        [KeyboardButton(text="📖 Buyurtmalar tarixi")],
        [KeyboardButton(text="⚙️Sozlash ℹ️ Ma'lumotlar"), KeyboardButton(text="🔥 Aksiya")],
        [KeyboardButton(text="🙋🏻‍♂️ Jamoamizga qo'shiling"), KeyboardButton(text="☎️ Les Ailes bilan aloqa")],
    ], resize_keyboard=True
)

phone_number = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Ulashish ☎️", request_contact=True)]], resize_keyboard=True
)