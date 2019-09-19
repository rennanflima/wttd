from django.views.generic import DetailView, ListView

from eventex.core.models import Course, Speaker, Talk

home = ListView.as_view(template_name='index.html',
                        model=Speaker)

speaker_detail = DetailView.as_view(model=Speaker)


talk_list = ListView.as_view(model=Talk)
