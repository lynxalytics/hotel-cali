from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.CommentListView.as_view(),
        name="comment-list"
    ),
    path(
        "create/new",
        views.CommentCreateView.as_view(),
        name="comment-create"
    ),
    path(
        "update/<int:pk>/",
        views.CommentUpdateView.as_view(),
        name="comment-update"
    ),
    path(
        "delete/<int:pk>/",
        views.CommentDeleteView.as_view(),
        name="comment-delete"
    ),
]
