from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .models import NippoModel
from .forms import NippoFormModel
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

class OwnerOnly(UserPassesTestMixin):
    def test_func(self):
        nippo_instance = self.get_object()
        return nippo_instance.user == self.request.user
    
    def handle_no_permission(self):
        messages.error(self.request, "ご自身の日報でのみ編集・削除可能です。")
        return redirect("nippo-detail", pk=self.kwargs["pk"])
    

class NippoListView(ListView):
    template_name = "nippo/nippo-list.html"
    #model = NippoModel
    def get_queryset(self):
        return NippoModel.objects.all()
    
    def get_context_data(self):
        ctx = super().get_context_data()
        ctx["site_name"] = "itc.tokyo"
        return ctx

# def nippoListView(request):
#     template_name = "nippo/nippo-list.html"
#     ctx = {}
#     qs = NippoModel.objects.all()
#     ctx['object_list'] = qs
#     return render(request, template_name, ctx)

class NippoDetailView(DetailView):
    template_name = "nippo/nippo-detail.html"
    model = NippoModel

# def nippoDetailView(request,pk):
#     template_name = "nippo/nippo-detail.html"
#     ctx = {}
#     #q = NippoModel.objects.get(pk=pk)
#     q = get_object_or_404(NippoModel, pk=pk)
#     ctx['object'] = q
#     return render(request, template_name, ctx)


class NippoCreateFormView(CreateView):
    template_name="nippo/nippo-form.html"
    form_class=NippoFormModel
    success_url=reverse_lazy("nippo-list")

    def get_form_kwargs(self):
        kwgs = super().get_form_kwargs()
        kwgs["user"] = self.request.user
        return kwgs

# class NippoCreateFormView(FormView):
#     template_name = "nippo/nippo-form.html"
#     form_class = NippoFormClass
#     success_url = reverse_lazy("nippo-list")

#     # def get_success_url(self):
#     #     return reverse("nippo-list")

#     def form_valid(self, form):
#         data = form.cleaned_data
#         obj = NippoModel(**data)
#         obj.save()
#         return super().form_valid(form)

# def nippoCreateView(request):
#     template_name = "nippo/nippo-form.html"
#     form = NippoFormClass(request.POST or None)
#     ctx = {"form": form}
#     if form.is_valid():
#         title = form.cleaned_data["title"]
#         content = form.cleaned_data["content"]
#         obj = NippoModel(title=title, content=content)
#         obj.save()
#         if request.POST:
#             return redirect("nippo-list")
#     return render(request, template_name, ctx)


class NippoUpdateView(OwnerOnly, UpdateView):
    template_name="nippo/nippo-form.html"
    model=NippoModel
    form_class=NippoFormModel
    success_url=reverse_lazy("nippo-list")

# def nippoUpdateView(request, pk):
#     template_name = "nippo/nippo-form.html"
#     #obj = NippoModel.objects.get(pk=pk)
#     obj = get_object_or_404(NippoModel, pk=pk)
#     initial_value = {"title": obj.title, "content": obj.content}
#     form = NippoFormClass(request.POST or initial_value)
#     ctx = {"form": form}
#     ctx['object'] = obj
#     if form.is_valid():
#         title = form.cleaned_data["title"]
#         content =form.cleaned_data["content"]
#         obj.title = title
#         obj.content = content
    #     obj.save()
    #     if request.POST:
    #        return redirect("nippo-list")

    # return render(request, template_name, ctx)


class NippoDeleteView(OwnerOnly,DeleteView):
    template_name="nippo/nippo-delete.html"
    model=NippoModel
    success_url=reverse_lazy("nippo-list")

# def nippoDeleteView(request, pk):
#     template_name = "nippo/nippo-delete.html"
#     obj = get_object_or_404(NippoModel, pk=pk)
#     ctx = {"object": obj}
#     if request.POST:
#         obj.delete()
#         return redirect("nippo-list")
#     return render(request, template_name, ctx)
