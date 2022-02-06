from .models import Setting
from account.models import Profile
from django.shortcuts import get_object_or_404

def access_settings(request):
    """ returns a dictionary """
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting}
    if request.user.id is not None:
        userprofile = get_object_or_404(Profile, user=request.user)
        context['userprofile'] = userprofile
    
    return context