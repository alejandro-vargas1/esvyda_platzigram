#platzigram urls module

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include

from posts import views as posts_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),

    #Views de la app users
    #path('users/',include(('users.urls','posts'),namespace='users')),
    path('users/login',users_views.login_view, name='login'),
    path('users/logout', users_views.logout_view, name='logout'),
    path('users/signup', users_views.signup, name='signup'),
    path('users/me/profile', users_views.update_profile, name='update_profile'),

    #Views de la app posts
    #path('', include(('posts.urls','posts'),namespace='posts')),
    #include((nombre_tupla,aplicacion),namespace=aplicacion) 

    path('', posts_views.list_posts, name='feed'),
    path('posts/new', posts_views.create_post, name='create_post'),  


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
