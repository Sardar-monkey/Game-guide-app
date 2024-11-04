from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('allgames/', views.allgames_page, name='allgames_page'),
    path('allguides/', views.allguides_page, name='allguides_page'),
    path('myguides/', views.myguides_page, name='myguides_page'),
    path('post/detail/<int:pk>/', views.description_page, name='description_page'),
    path('allgames/category/<slug:slug>/', views.guides_by_category_page, name='guides_by_category_page'),
    path('myguides/create/', views.create_page, name='create_page'),
    path('registration/', views.sign_up_page, name='sign_up_page'),
    path('authorization/', views.login_page, name='login_page'),
    path('logout/', views.logout_action, name='logout_action'),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

