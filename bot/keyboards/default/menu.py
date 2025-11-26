from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buyurtma = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏃 Olib ketish"), KeyboardButton(text="🚙 Yetkazib berish")],
        [KeyboardButton(text="⬅️ Ortga")]
    ], resize_keyboard=True
)

buyurtma_location = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️ Ortga"), KeyboardButton(text="Eng yaqin filialni aniqlash")],
        [KeyboardButton(text="Bu yerda buyurma berish🌐"), KeyboardButton(text="Filialni tanla")],
    ]
)

buyurtma_yetkazish = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Eng yaqin filialni aniqlash")],
        [KeyboardButton(text="⬅️ Ortga"), KeyboardButton(text="🗺 Mening manzillarim")],
    ], resize_keyboard=True
)

sozlamalar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ismni o'zgartirish"), KeyboardButton(text="📱 Raqamni o'zgartirish")],
        [KeyboardButton(text="🏙 Shaharni o'zgartirish"), KeyboardButton(text="🇺🇿 Tilni o'zgartirish")],
        [KeyboardButton(text="ℹ️ Filallar haqida ma'lumotlar"), KeyboardButton(text="📄 Ommaviy taklif")],
        [KeyboardButton(text="⬅️ Ortga")]
    ], resize_keyboard=True
)

aloqa = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💬 Biz bilan aloqaga chiqing"), KeyboardButton(text="✍️ Fikr bildirish")],
        [KeyboardButton(text="⬅️ Ortga")]
    ], resize_keyboard=True
)