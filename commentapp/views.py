from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.article_id = self.request.POST.get('article_pk')
        return super().form_valid(form)
    # 검증이 완료 되고 나서 comment 작성자, 작성자 id 를 user와 article_pk로부터 받아오기

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})


@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
