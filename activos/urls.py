from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.Comments.as_view(), name='comments'),
    path('comments/create/', views.CreateComment.as_view(), name='create_comment'),
    path('comments/<int:pk>/', views.DisplayComment.as_view(), name='display_comment'),
    path('comments/<int:pk>/edit/', views.EditComment.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', views.DeleteComment.as_view(), name='delete_comment')
]
