from django.forms import inlineformset_factory
from django.contrib.auth.models import User

from .models import Profile

ProfileInlineFormSet = inlineformset_factory(User, Profile,
                                             exclude=('friends',),
                                             can_delete=False,
                                             extra=1,
                                             max_num=1)
