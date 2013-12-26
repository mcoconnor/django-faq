# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect

from django.views.generic.list import ListView

from faq.models import Topic, Question


def _fragmentify(model, slug, url=None):
    get_object_or_404(model.objects.published().filter(slug=slug))
    url = url or reverse('faq-topic-list')
    fragment = '#%s' % slug

    return redirect(url + fragment, permanent=True)


class TopicListView(ListView):
    model = Topic

    def get_template_names(self):
        return ['faq/topic_list.html']


def topic_detail(request, slug):
    """
    A detail view of a Topic

    Simply redirects to :view:`faq.views.topic_list` with the addition of
    a fragment identifier that links to the given :model:`faq.Topic`.
    E.g., ``/faq/#topic-slug``.

    """
    return _fragmentify(Topic, slug)


def question_detail(request, topic_slug, slug):
    """
    A detail view of a Question.

    Simply redirects to :view:`faq.views.topic_list` with the addition of
    a fragment identifier that links to the given :model:`faq.Question`.
    E.g. ``/faq/#question-slug``.

    """
    return _fragmentify(Question, slug)
