# from haystack import indexes
# from .models import Post

# class PostIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     publish = indexes.DateTimeField(model_attr='publishe')

#     def get_model(self):
#         return Post

#     # 继承得来的函数，将所有已发布的文章加入索引队列
#     def index_queryset(self, using=None):
#         return self.get_model().published.all()

from haystack import indexes
from .models import Post
 
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    publish = indexes.DateTimeField(model_attr='publish')
 
    def get_model(self):
        return Post
 
    def index_queryset(self, using=None):
        return self.get_model().published.all()