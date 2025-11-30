from django.urls import path 
from .views import *

urlpatterns = [
    path("", login_view , name= "login"),
    path('profile/', Profile.as_view(), name= 'profile'),
    path('signup/', SignUpView.as_view() , name= 'signup'),
    path('logout/', logout_user , name= 'logout'),
    path('account-setting/', AccountSettingView.as_view() , name= 'account-setting'),
    path('new-post/', CreatePostView.as_view() , name='new_post'),
    path('user/<str:username>/', FriendProfile.as_view(), name= 'friend-profile'),
    path('search/', SearchResult.as_view(), name='search'),
    path('follow/<int:id>',follow_user , name='follow-user'),
    path('unfollow/<int:id>' , unfollow_user , name = 'unfollow-user'),
    path('home/' , HomePage.as_view() , name = 'home-page')

]
