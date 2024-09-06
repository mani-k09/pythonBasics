from userClass import User
from post import Post
app_user_two = User("Mani","logintomani@gmail.com","Integration","topSecret")
app_user_two.get_user_info()
app_user_two.change_email("newEmail@gmail.com")
app_user_two.get_user_info()

post_Action = Post("We will pass through this situation","Mani")
post_Action.publish_message()
