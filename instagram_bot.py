from instabot import Bot

my_bot = Bot()
#login
my_bot.login(username="pratyushah", password="")

#follow a user
#my_bot.follow("python_app_projects")
#follow multiple users
#my_bot.follow_users(["coding_for_beginners_", "python.app", "py_beginners"])
#unfollow the non followers
#my_bot.unfollow_non_followers ()

#upload an image
#my_bot.upload_photo("dog.jpg", caption="Pytube | Create your own youtube video downloader using python")

#send message to user
my_bot.send_message("Where are you from", "ridesh779")
print(Exception)

sleep(60)
#like a post
#try:
 #   my_bot.like_user("rkraj6369", amount=2, filteration=False)
#except Exception:
 #   print(Exception)

#comment
#try:
 #   user_id =my_bot.get_user_id_from_username("rkraj6369")
  #  media_id = my_bot.get_last_user_medias(user_id, 1)
   # my_bot.comment(media_id[0], "this is nice")
#except Exception:
 #   print(Exception)

#sleep(20)
#get list of followers of anyone
#followers_list = my_bot.get_user_followers ("rkraj6369")
#following_list = my_bot.get_user_following("rkraj6369")

#for count, each_follower in enumerate(followers_list):
 #   if count>4:
  #      continue
   # sleep (5)
    #print(my_bot.get_username_from_user_id(each_follower))
#for count, each_follow in following_list:
 #   if count>4:
  #      continue
  #  print(my_bot.get_username_from_user_id(each_follow))
my_bot.logout()