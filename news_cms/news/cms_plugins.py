from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import Article

@plugin_pool.register_plugin
class LatestArticlesPlugin(CMSPluginBase):
    module = _("Articles")
    name = _("Latest Articles")
    render_template = "news/latest_articles.html"

    def render(self, context, instance, placeholder):
        context['articles'] = Article.objects.order_by('-publication_date')[:5]
        return context
