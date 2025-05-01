from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect

class OwnerOnly(UserPassesTestMixin):
    def test_func(self):
        nippo_instance = self.get_object()
        return nippo_instance.user == self.request.user
    
    def handle_no_permission(self):
         messages.error(self.request, "ご自身の日報でのみ編集・削除可能です。")
         return redirect("nippo-detail", pk=self.kwargs["pk"])

class OwnProfileOnly(UserPassesTestMixin):
    def test_func(self):
        profile_obj = self.get_object()
        return profile_obj == self.request.user.profile