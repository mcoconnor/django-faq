# -*- coding: utf-8 -*-

from faq.models import Topic, Question

from django.views.generic.detail import DetailView


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['topic'] = Topic.objects.published().get(
            slug=context['question'].topic.slug
        )
        return context

    def get_template_names(self):
        return ['faq/question_detail.html']
