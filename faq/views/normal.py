# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView

from faq.models import Topic, Question
from faq.views.shallow import _fragmentify


class TopicDetailView(DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['question_list'] = Question.objects.published().filter(
            topic__slug=context['topic'].slug
        )
        return context

    def get_template_names(self):
        return ['faq/topic_detail.html']


def question_detail(request, topic_slug, slug):
    """
    A detail view of a Question.

    Simply redirects to a detail page for the related :model:`faq.Topic`
    (:view:`faq.views.topic_detail`) with the addition of a fragment
    identifier that links to the given :model:`faq.Question`.
    E.g. ``/faq/topic-slug/#question-slug``.

    """
    url = reverse('faq-topic-detail', kwargs={'slug': topic_slug})
    return _fragmentify(Question, slug, url)
