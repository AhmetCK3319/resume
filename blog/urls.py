from django.urls import path
from .views import post_view, post_detail_view


urlpatterns = [
    path("blog_page/", post_view, name="blog_page"),
    path("blog_page/category/<slug:category_slug>/", post_view, name="blog_page_by_category"),
    path("blog_page/tag/<slug:tag_slug>/", post_view, name="blog_page_by_tag"),
    path("blog_page/category/<slug:category_slug>/tag/<slug:tag_slug>/", post_view, name="blog_page_by_category_and_tag"),
    path("blog_page/post/<slug:slug>/", post_detail_view, name="blog_page_detail"),
]
