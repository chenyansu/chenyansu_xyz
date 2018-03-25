from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
from haystack.query import SearchQuerySet
# from django.template.backends import django

def post_list(request, tag_slug=None):
    """
    列表页数据
    """
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page':page, 'posts':posts, 'tag':tag})

# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    """
    详情页数据
    """
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                            publish__month=month, publish__day=day)

    comments = post.comments.filter(active=True) #  Comment 模型（ model）中使用 related_name 关系属性为 comments 定义
    new_comment = None

    # 评论
    if request.method == 'POST': # 填写完表单是POST
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False) # save()创建了一个表单链接的 model 的实例，保存数据到数据库
            new_comment.post = post
            new_comment.save() # save()保存数据到数据库
    else: # 首先是GET 请求
        comment_form = CommentForm()

    # 相同帖子推荐
    post_tags_ids = post.tags.values_list('id', flat=True) # 获取同标签帖子列表
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id) #除去本帖
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4] # 截取前4
 
    return render(request, 'blog/post/detail.html', 
            {'post':post, 'comments':comments, 'new_comment':new_comment, 
                'comment_form':comment_form,'similar_posts':similar_posts})

def post_share(request, post_id):
    """
    分享页数据(通过email)
    """
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST': # POST 提交表单
        form = EmailPostForm(request.POST)
        if form.is_valid(): # 如果数值有效，则将cd 赋值为表单的干净的数据
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends your reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url,cd['name'], cd['comments'])
            send_mail(subject, message, 'chenyu_pub@sina.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm() # GET 如果是GET请求，我们需要一个空表单以便填写，通常我们达到分享页后第一件是就是GET
    return render(request, 'blog/post/share.html', {'post':post, 'form':form, 'sent':sent})


def post_search(request):
    form = SearchForm()
    cd = None
    results = None
    total_results = 0
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Post).filter(content=cd['query']).load_all()
            total_results = results.count()
            # print('cd is '+str(cd) + ' ' + 'results is ' + str(results) + ' ' + 'total_results is ' + str(total_results))
    print('cd is '+str(cd) + '\n' + 'results is ' + str(results) + '\n' + 'total_results is ' + str(total_results))
    return render(request, 'blog/post/search.html', {'form':form, 'cd':cd, 'results':results, 'total_results':total_results})


# Create your views here.
