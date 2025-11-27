# import logging
#
# from aiogram import Router, F
# from aiogram.filters import CommandStart
# from aiogram.types import Message
# from aiogram.fsm.context import FSMContext
#
# from bot.keyboards.default.default import language, city, menu, phone_number
# from django.contrib.auth import get_user
#
# from bot.keyboards.default.menu import buyurtma, sozlamalar, aloqa, buyurtma_location, buyurtma_yetkazish
# from bot.states.order import Order
# from bot.states.register import RegisterState
#
# # from bot.models import UserImage
#
# logger = logging.getLogger(__name__)
# router = Router()
#
#
# @router.message(CommandStart())
# async def cmd_start(message: Message, state: FSMContext):
#     logger.info(f"🔔 /start qabul: {message.from_user.first_name}")
#     try:
#         await message.answer(
#             "Assalomu alaykum! Les Ailes yetkazib berish xizmatiga xush kelibsiz."
#             "Здравствуйте! Добро пожаловать в службу доставки Les Ailes."
#             "Hello! Welcome to Les Ailes delivery service.",
#             parse_mode=None, reply_markup=language
#         )
#         await state.set_state(RegisterState.language)
#         logger.info("✅ Javob yuborildi!")
#     except Exception as e:
#         logger.error(f"❌ Xatolik: {e}", exc_info=True)
#
# @router.message(RegisterState.language)# bu tushirilgan steatedan ma'lumot olosh
# async def language_handler(message: Message, state: FSMContext):
#     await state.update_data(language=message.text)  # bu steatedagi ma'lumotlarni oladi va
#     if message.text == "🇺🇿 O'zbekcha":
#         text = "Qaysi shaharda yashaysiz?\nIltimos, shaharni tanlang:"
#     elif message.text == "🇷🇺 Русский":
#         text = "В каком городе Вы живёте?\nПожалуйста, выберите город:"
#     else:
#         text = "Where do you live?\nPlease,choose the city"
#     await message.answer(text=text, reply_markup=city)
#     await state.set_state(RegisterState.location)
#
#
# @router.message(RegisterState.location)
# async def location_handler(message: Message, state: FSMContext):
#     await state.update_data(location=message.text)
#     await message.answer("Bosh menyu", reply_markup=menu)
#     await state.set_state(RegisterState.menu)
#
# @router.message(RegisterState.menu)
# async def menu_handler(message: Message, state: FSMContext):
#     if message.text == "🛍 Buyurtma berish":
#         text = "Buyurtmani o'zingiz 🙋‍♂️ olib keting yoki Yetkazib berishni 🚙 tanlang"
#         await message.answer(text=text, reply_markup=buyurtma)
#         await state.set_state(RegisterState.order)   # buyurma uchun qilinadi
#
#     elif message.text == "📖 Buyurtmalar tarixi":
#         if get_user(phone_number=message.phone_number):
#             text = "Sizning buyurtmalaringiz yo'q\nBosh menyu"
#             await message.answer(text=text, reply_markup=menu)
#             await state.set_state(RegisterState.menu)
#         else:
#             text = "Avval ro'yxatdan o'ting.\nRo'yxatdan o'tish uchun telefon raqamingizni kiriting!\nMisol uchun, +998xx xxx xx xx\nBosh menyu"
#             await message.answer(text=text, reply_markup=phone_number)
#             await state.set_state(Order.Order_register)
#         await state.set_state(RegisterState.menu)
#     elif message.text == "⚙️Sozlash ℹ️ Ma'lumotlar":
#         text = "Harakatni tanlang:"
#         await message.answer(text=text, reply_markup=sozlamalar)
#         await state.set_state(RegisterState.settings)
#     elif message.text == "🔥 Aksiya":
#         text = "Shahringizda hali aksiyalar mavjud emas"
#         await message.answer(text=text, reply_markup=menu)
#         await state.set_state(RegisterState.menu)
#     elif message.text == "🙋🏻‍♂️ Jamoamizga qo'shiling":
#         text = "Ahil jamoamizda ishlashga taklif qilamiz! Telegramdan chiqmay, shu yerning o'zida anketani to'ldirish uchun quyidagi tugmani bosing."
#         await message.answer(text=text, reply_markup=menu)
#         await state.set_state(RegisterState.menu)
#     elif message.text == "☎️ Les Ailes bilan aloqa":
#         text = "Agar siz bizga yozsangiz yoki sharh qoldirmoqchi bo'lsangiz, xursand bo'lamiz."
#         await message.answer(text=text, reply_markup=aloqa)
#         await state.set_state(RegisterState.about)
#     else:
#         await message.answer(text="Iltmos Menudan tanlang", reply_markup=menu)
#         await state.set_state(RegisterState.menu)
#
#
# @router.message(RegisterState.order)
# async def order_handler(message: Message, state: FSMContext):
#     await state.update_data(order=message.text)
#     if message.text == "🏃 Olib ketish":
#         text = "Qayerdasiz 👀? Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni aniqlaymiz"
#         await message.answer(text=text, reply_markup=buyurtma_location)
#         await state.set_state(Order.Order_location) #   Order_location javobi
#     elif message.text == "🚙 Yetkazib berish":
#         text = "Buyurtmangizni qayerga yetkazib berish kerak 🚙?\nAgar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni va yetkazib berish xarajatlarini aniqlaymiz 💵"
#         await message.answer(text=text, reply_markup=buyurtma_yetkazish)
#         await state.set_state(Order.Order_yetkazish)
#
# """
# bu ortga qaytish handleri
# """
# @router.message(F.text == "⬅️ Ortga", RegisterState.order, RegisterState.settings)
# async def back_handler(message: Message, state: FSMContext):
#     await state.set_state(RegisterState.menu)
#     await message.answer("Orqaga qaytdik", reply_markup=menu)
#
#
#
# # @router.message(Order.Order_register)
# # async def order_register(message: Message, state: FSMContext):
# #     await state.update_data(phone_number=message.text)
# #     if get_user()
#
# #
# # @router.message(F.photo)
# # async def handle_photo(message: Message):
# #     """Handle incoming photos"""
# #     try:
# #         photo = message.photo[-1]
# #
# #         logger.info(f"Received photo from user {message.from_user.id}")
# #
# #         # Save to database
# #         image = await sync_to_async(UserImage.objects.create)(
# #             user_id=message.from_user.id,
# #             username=message.from_user.username,
# #             file_id=photo.file_id,
# #             file_unique_id=photo.file_unique_id,
# #             caption=message.caption
# #         )
# #
# #         logger.info(f"Image saved with ID: {imagei.d}")
# #
# #         # Simple response without parse mode
# #         await message.answer(
# #             f"✅ Image saved!\n\n"
# #             f"ID: {image.id}\n"
# #             f"File ID: {photo.file_id}\n"
# #             f"Size: {photo.width}x{photo.height}",
# #             parse_mode=None
# #         )
# #
# #         # Send the image back
# #         await message.answer_photo(
# #             photo=photo.file_id,
# #             caption="Here's your image using the saved file_id!"
# #         )
# #
# #     except Exception as e:
# #         logger.error(f"Error: {e}", exc_info=True)
# #         await message.answer("❌ Error saving image", parse_mode=None)
# #
# #
# # @router.message(F.text)
# # async def echo_handler(message: Message):
# #     logger.info(f"Received: {message.text}")
# #     # Escape markdown special characters
# #     if message.text:
# #         # Replace markdown special chars to avoid parsing errors
# #         safe_text = message.text.replace('_', '\\_').replace('*', '\\*').replace('[', '\\[').replace('`', '\\`')
# #         await message.answer(f"Echo: {safe_text}")
# #     else:
# #         await message.answer("Echo: (empty)", parse_mode=None)
# #
# #
# # @router.message()
# # async def other_types_handler(message: Message):
# #     await message.answer("Please send me a photo or text message", parse_mode=None)