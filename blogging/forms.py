from django.forms import ModelForm
from blogging.models import Post, Category

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'published_date']

        #   Created date and modified date removed because they cannot be changed


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'posts']