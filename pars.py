
from selenium import webdriver


def dzyt(bot, chat_id, message):
    driver = webdriver.Chrome()
    bot.send_message(chat_id, "Введите YouTube канал")
    bot.register_next_step_handler(message, search_from_channel, bot=bot, driver=driver)

def search_from_channel(message, bot, driver):
    bot.send_message(message.chat.id, "Начинаю поиск")
    driver.get(message.text + "/videos")
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 1:
            break
    driver.close()