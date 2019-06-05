import telegram
my_token = '889082229:AAHdaKayoSHvJLWE1Qq8yT8GBci-lXT-CeI'
my_chat_id = '792271018'
bot = telegram.Bot(token=my_token)
bot.sendMessage(chat_id=my_chat_id, text="지하철 분실물 검색 봇입니다.")