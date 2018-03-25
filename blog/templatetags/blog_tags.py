from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

"""
自定义标签 ----{% %}
"""

# 计数器
@register.simple_tag
def total_posts():
    return Post.published.count()

# 最新文章
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

# 最多评论文章
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

# markdown
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text)) # Django默认不信赖任何html语句，mark_safe使其加入信赖