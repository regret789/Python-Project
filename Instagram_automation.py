from instabot import Bot
bot=Bot()

bot.login(username="kushwahashambhu.7311",password="12345")
bot.follow("wscubetech")
bot.upload_photo("C:\97798\PycharmProjects\pythonProject\two.png")
bot.unfollow("wscubetech")
bot.send_message("please scan me")

followers=bot.get_user_followers("kushwahashambhu.7311")
for folloe in followers:
    print(bot.get_user_info(followers))

    following=bot.get_user_following("kushwahashambhu.7311")
    for Following in following:
        print(bot.get_user_info(following))