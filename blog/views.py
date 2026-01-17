from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Tag, Post, Comment

def get_common_context():
    """Sidebar ve ortak alanlar için veriyi tek merkezden alıyoruz."""
    return {
        'categories': Category.objects.annotate(post_count=Count('posts')),
        'tags': Tag.objects.filter(posts__status='published').distinct(),
        'popular_posts': Post.objects.filter(status='published').order_by('-views_count')[:5]
    }

def post_view(request, category_slug=None, tag_slug=None):
    posts = Post.objects.filter(status='published')
    selected_category = None
    selected_tag = None

    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=selected_category)

    if tag_slug:
        selected_tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags=selected_tag)

    context = get_common_context()
    context.update({
        'posts': posts,
        'selected_category': selected_category,
        'selected_tag': selected_tag,
    })
    return render(request, 'blog.html', context)

def post_detail_view(request, slug):
    # Yazıyı getir ve izlenme sayısını artır
    post = get_object_or_404(Post, slug=slug, status='published')
    post.views_count += 1
    post.save(update_fields=['views_count'])

    # Sadece bu yazıya ait onaylanmış yorumları getir
    comments = post.comments.filter(is_approved=True)
    comment_count = comments.count()

    context = get_common_context()
    context.update({
        'post': post,
        'comments': comments,
        'comment_count': comment_count,
    })
    return render(request, 'single-blog.html', context)