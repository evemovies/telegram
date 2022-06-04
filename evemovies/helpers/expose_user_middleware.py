import requests
from dotenv import dotenv_values
from telegram import Update
from telegram.ext import filters, CallbackContext, MessageHandler

BASE_URL = dotenv_values()['API_BASE_URL']


async def _expose_user_to_context(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    if 'user' in context.user_data:
        return

    user_id = update.message.from_user.id
    token_response = requests.get(f'{BASE_URL}/api/v1/users/{update.message.from_user.id}/token').json()

    try:
        token = token_response['data']['token']
        user_response = requests.get(f'{BASE_URL}/api/v1/users/{user_id}',
                                     headers={"Authorization": f"Bearer {token}"}).json()

        context.user_data['user'] = user_response['data']
    except AttributeError:
        print("Can't expose token to the context")


expose_user_handler = MessageHandler(filters.TEXT, _expose_user_to_context)
