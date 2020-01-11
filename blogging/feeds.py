from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestEntriesFeed(Feed):
    title = "My blog site news"
    link = "/sitenews/"
    description = "Updates on my blog!"

    def posts(self):
        return Post.objects.order_by('-pub_date')[:5]

    def post_title(self, post):
        return post.title

    def post_description(self, post):
        return post.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
