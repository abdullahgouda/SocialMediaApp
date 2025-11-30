from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView , UpdateView
from django.views.generic.list import ListView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.utils.decorators import method_decorator





# Create your views here.

@method_decorator(login_required(login_url='login'), name='dispatch')
class Profile(ListView):

    model = Post
    template_name = 'profile.html'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user = user ).order_by('-created_date')

# creation of users

class SignUpView(CreateView):

    model = User
    form_class = CustomUserCreationForm
    template_name = 'Signup.html'

    def form_invalid(self, form):
        print("❌ Form Errors:", form.errors)
        return self.render_to_response(self.get_context_data(form=form))
        
    def form_valid(self, form): 
        user = form.save()
        login(self.request , user)
        return redirect('profile')
    #if i logging in already no need for sign up page so her i disactivate it 
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        # super her is about mro techniqe (go back to oop )
        return super(SignUpView,self).get(*args, **kwargs)
    

# Log In
def login_view(request):

    # if i loggin in already i disactivate the login page
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "GET":
            return render(request, "login.html")
        
        elif request.method == "POST":
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username ,password=password)

            if user is not None:
                login(request , user)
                return redirect('home-page')
            else:
                print('no user found!!!')
                return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')



@method_decorator(login_required(login_url='login'), name='dispatch')
class AccountSettingView(UpdateView):

    model = User
    fields = ['username' ,'first_name' ,'last_name' ,'profile_picture' ,'bio']
    template_name = 'account_settings.html'
    success_url = '/profile/'


    def get_object(self):
        return self.request.user
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreatePostView(CreateView):

    model = Post
    fields =['caption']
    template_name = 'new_post.html'
    success_url = '/profile/'

    # to link the post to the user who created it
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)
    



@method_decorator(login_required(login_url='login'), name='dispatch')
class FriendProfile(ListView):

    model = Post
    template_name = 'friend-profile.html'
    paginate_by = 2


    def get(self, *args, **kwargs):
        friend_username = self.kwargs['username']
        user_username = self.request.user.username
        if friend_username == user_username:
            return redirect('profile')
        else:
            return super(FriendProfile, self).get(*args,**kwargs)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        friend_username = self.kwargs['username']
        friend = User.objects.get(username=friend_username)
        context['friend'] = friend
        is_following = self.request.user.is_following(friend)
        context['is_following'] = is_following
        return context
    
    def get_queryset(self):
        friend_username = self.kwargs['username']
        friend = User.objects.get(username=friend_username)
        return Post.objects.filter(user = friend ).order_by('-created_date')


class SearchResult(ListView):
    model = User
    template_name = 'search-result.html'
    paginate_by = 5


    def get_queryset(self):
        search_term= self.request.GET['search-term']
        qs = User.objects.filter(username__contains =search_term)
        return qs

login_required(login_url='login')
def follow_user(request , id):

    user_A = request.user
    user_B = User.objects.get(id=id)
    new_friend = Friend(user_A = user_A , user_B = user_B)
    new_friend.save()

    return redirect('/user/'+ user_B.username)

login_required(login_url='login')
def unfollow_user(request , id):

    user_B = User.objects.get(id = id)
    user_A = request.user

    Friend.objects.filter(user_A = user_A , user_B = user_B).delete()

    return redirect('/user/'+user_B.username)



@method_decorator(login_required(login_url='login'), name='dispatch')
class HomePage(ListView):
    model = Post
    template_name = 'home-page.html'
    paginate_by = 5

    def get_queryset(self):
        
        following = self.request.user.get_following()
        return Post.objects.filter(user_id__in = following).order_by('-created_date')