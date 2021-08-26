from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.models import HelloWorld
from accountapp.forms import AccountCreationForm
from articleapp.models import Article


class AccountCreateView(CreateView):
    model = User
    # user 객체를 읽어온다
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    # 완료 후 이동 페이지
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    # user 객체를 읽어온다
    context_object_name = 'target_user'
    # user를 타겟으로 가져온다
    template_name = 'accountapp/detail.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        # writer = target_user 와 동일: 작성자 인식
        return super().get_context_data(object_list=article_list, **kwargs)


has_ownership = [login_required, account_ownership_required]
# method_decorator 는 단일 데코레이터 뿐 아니라 리스트 데코레이터도 받을 수 있음


# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    # ID는 수정되지 않도록 AccountCreationForm 클래스를 정의해줌(forms.py)
    context_object_name = 'target_user'
    # success_url = reverse_lazy('accountapp:detail')
    # 완료 후 이동 페이지
    # pk를 입력해줘야 구동이 됨
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})


    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         # 1. 로그인 되었는지 확인
    #         # 2. request.user(로그인 된 ID)가 get_object(target_user)와 동일한지 확인
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden()
    #         # 금지된 경로로 들어갔다는걸 알림
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         # 1. 로그인 되었는지 확인
    #         # 2. request.user(로그인 된 ID)가 get_object(target_user)와 동일한지 확인
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden()
    #         # 금지된 경로로 들어갔다는걸 알림


# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         # 1. 로그인 되었는지 확인
    #         # 2. request.user(로그인 된 ID)가 get_object(target_user)와 동일한지 확인
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden()
    #         # 금지된 경로로 들어갔다는걸 알림
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         # 1. 로그인 되었는지 확인
    #         # 2. request.user(로그인 된 ID)가 get_object(target_user)와 동일한지 확인
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden()
    #         # 금지된 경로로 들어갔다는걸 알림

