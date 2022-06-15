from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


til = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton("🇺🇸 English", callback_data="en"),
      InlineKeyboardButton("🇷🇺 Русский", callback_data="ru"),
      InlineKeyboardButton("🇹🇷 Turkish", callback_data="tr")
    ],
    [
      InlineKeyboardButton("🇫🇷 French", callback_data="fr"),
      InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="uz"),
      InlineKeyboardButton("🇩🇪 German", callback_data="de"),
    ]
  ],
)