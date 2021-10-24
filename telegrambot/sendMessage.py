import requests
from .models import TelegramSetting

def setTelegram(tg_name, tg_phone):
    if TelegramSetting.objects.get(pk=1):
        settings = TelegramSetting.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_text)

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part1 = text[0:text.find('{')]
            part2 = text[text.find('}')+1:text.rfind('{')]
            part3 = text[text.rfind('}'):-1]

            message_slice = part1 + tg_name + part2 + tg_phone + part3
        else:
            message_slice = text

        try:
            api = 'https://api.telegram.org/bot'
            method = api + token + '/sendMessage'

            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': message_slice
            })
        except:

            pass
        finally:

            if req.status_code != 200:
                print('Ошибка отправки!')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Все в порядке, сообщение отправлено')
    else:
        pass
