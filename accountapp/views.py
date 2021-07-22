from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.models import HelloWorld
from accountapp.forms import AccountCreationForm


@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(request):
    # if request.user.is_authenticated:
        # 로그인 여부 확인
    if request.method == "POST":
        temp = request.POST.get('input_text')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        # 객체를 DB에 저장    # temp와 다르게 DB에 저장됨(왼쪽 파일 목록 db.sqlite3)
        # settings.py의 DATABASE 내용 확인 해보면 지정된걸 확인할수있음

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

        # hello_world_list = HelloWorld.objects.all()
        # # DB의 모든 데이터를 hello_world_list에 넣어줌
        #
        # return render(request, 'accountapp/hello_world.html',
        #               context={'hello_world_list': hello_world_list})
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})
    # else:
    #     return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):
    model = User
    # user 객체를 읽어온다
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    # 완료 후 이동 페이지
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    # user 객체를 읽어온다
    context_object_name = 'target_user'
    # user를 타겟으로 가져온다
    template_name = 'accountapp/detail.html'


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
    success_url = reverse_lazy('accountapp:detail')
    # 완료 후 이동 페이지
    # pk를 입력해줘야 구동이 됨
    template_name = 'accountapp/update.html'

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
    success_url = reverse_lazy('accountapp:hello_world')
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

