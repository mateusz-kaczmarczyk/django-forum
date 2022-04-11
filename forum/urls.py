from django.urls import path
from .views import SubforumDetailView
from .views import ThreadCreateView, ThreadDetailView, ThreadUpdateView, ThreadDeleteView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='forum-home'),
    path('subforum/<int:pk>/', SubforumDetailView.as_view(), name='subforum-detail'),
    path('subforum/<int:subforum_id>/thread/new/', ThreadCreateView.as_view(), name='thread-create'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread-detail'),
    path('thread/<int:pk>/update/', ThreadUpdateView.as_view(), name='thread-update'),
    path('thread/<int:pk>/delete/', ThreadDeleteView.as_view(), name='thread-delete'),
    path('thread/<int:thread_id>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('thread/<int:thread_id>/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('thread/<int:thread_id>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

]
