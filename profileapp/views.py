from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # 위의 검증이 모두 성공했을때 실행되는 함수
        form.instance.user = self.request.user
        # form이 들고있는 검증된 데이터를 instance(profile)에 넣어줌?
        return super().form_valid(form)
    # def form_invalid(self, form):
        # 위의 검증 중 하나가 실패했을때 실행되는 함수


class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'