from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


# Inline Mode
@Client.on_inline_query()
async def answer(_, inline_query):
	await inline_query.answer(
		results=[
			InlineQueryResultArticle(
				title=f"✅ Your Telegram ID is {inline_query.from_user.id}",
				input_message_content=InputTextMessageContent(
					f"✅ My Telegram ID is `{inline_query.from_user.id}`"
				),
				description="Tap to send your ID to current chat 🙃",
				thumb_url="https://telegra.ph/file/6939525d1291f0ec13c02.jpg",
			)
		],
		cache_time=1,
	)
