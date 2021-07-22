from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        # objects.all()을 사용하면 모든 객체를 가져오고 get()을 사용하면 선택한 객체를 가져옴
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
            # 금지된 경로 접근 알림
    return decorated
