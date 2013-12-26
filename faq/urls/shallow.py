# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from faq.views.shallow import TopicListView, topic_detail, question_detail

# Include these patterns if you want URLs like:
#
#   /faq/
#   /faq/#topic
#   /faq/#question
#

urlpatterns = patterns('',
    url(r'^$', topic_list, name='faq-topic-list'),
    url(r'^#(?P<slug>[-\w]+)$', topic_list, name='faq-topic-detail'),
    url(r'^#(?P<slug>[-\w]+)$', topic_list,
        name='faq-question-detail'),
)
