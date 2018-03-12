from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import Post

# Create your views here.


def post_list_view(request):
    list_objects = Post.published.all()
    paginator = Paginator(list_objects, 12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})

# potential to add in search capability
# def get_queryset(self):
#     """
#     Search for a post by title or text
#     """
#     qs = Blog.objects.published()
#
#     keywords = self.request.GET.get('q')
#     if keywords:
#         query = SearchQuery(keywords)
#         title_vector = SearchVector('title', weight='A')
#         content_vector = SearchVector('content', weight='B')
#         vectors = title_vector + content_vector
#         qs = qs.annotate(search=vectors).filter(search=query)
#         qs = qs.annotate(rank=SearchRank(vectors, query)).order_by('-rank')
#
#     return qs

def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
