from django.urls import path

from apps.blog.views import BlogList, BlogCreateView

urlpatterns = [

    path('', BlogList.as_view(), name="blog-list"),
    path('create-new-blog/', BlogCreateView.as_view(), name="blog-create-view"),
]

