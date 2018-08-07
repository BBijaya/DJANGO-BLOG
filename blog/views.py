from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
# Taggit
from taggit.models import Tag
from django.db.models import Count
# Create your views here.
"""
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
"""
def post_list(request, tag_slug=None):
    """

    """
    object_list = Post.published.all()
    tag = None

    search_term = ''

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    
    if 'search' in request.GET:
        search_term = request.GET['search']
        object_list = object_list.filter(title__icontains=search_term)

    
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page,
                                                   'posts': posts,
                                                   'tag':tag,
                                                   'search_term':search_term,
                                                   })












def post_detail(request, year, month, day, post):
    """ post detail view"""
    post = get_object_or_404(Post, slug = post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    #return render(request,'blog/post/detail.html', {'post': post})

    # list of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # a comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # creates comment objecct but doesnt commit to database
            new_comment = comment_form.save(commit=False)
            # Assign the current post ot the comment
            new_comment.post = post
            #save the coment ot the database
            new_comment.save()
            comment_form = CommentForm()
            new_comment = False 
            
            

    else:
        comment_form = CommentForm()
        new_comment = False 

    # list of similar posts
    post_tags_ids = post.tags.values_list('id',flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags',
                    '-publish')[:4]

    return render(request,'blog/post/details.html',
                    {'post':post,
                    'comments':comments,
                    'comment_form':comment_form,
                    'similar_posts':similar_posts,
                    'new_comment':new_comment})

def about_me(request):
    return render(request,'about.html')