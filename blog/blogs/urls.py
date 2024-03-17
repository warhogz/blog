from django.urls import path
from .views import BlogList, PostUpdate, DeleteView, PostCreate, CustomLoginView, RegisterPage, PostDetail
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path("", BlogList.as_view(), name="posts"),
    path('post/<int:pk>/', PostDetail.as_view(), name='post'),
    path('post-update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('post-delete/<int:pk>/', DeleteView.as_view(), name='post-delete'),
    path('post-create/', PostCreate.as_view(), name='post-create'),
]
