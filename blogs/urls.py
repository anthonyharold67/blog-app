from django.urls import path

from .views import BlogDeleteView,  BlogUpdateView, blog_create, blog_detail, blog_like

urlpatterns = [
    path('add',blog_create,name='blog_add'),
    path("update/<int:pk>",BlogUpdateView.as_view(),name="blog_update"),
    path("delete/<int:pk>",BlogDeleteView.as_view(),name="blog_delete"),
    path("detail/<int:id>",blog_detail,name="blog_detail"),
    path("like/<int:id>",blog_like,name="blog_like"),

]
