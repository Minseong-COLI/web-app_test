from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    # 장고에서 제공하는 ModelForm 을 상속 받아옴
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
        # field 순서대로 입력 창이 나온다
        # user는 target_user를 고려해야 하기 때문에 다른곳에서 처리?