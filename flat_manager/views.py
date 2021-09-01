from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, DetailView

from flat_manager.forms import LeaseAgreementForm, RoomForm, OwnerForm, RentierForm, FlatForm, AgentForm
from flat_manager.models import LeaseAgreement, Flat, Rentier, Owner, Agent, Room
from flat_manager.filters import FlatFilter


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html',)

class SearchView(View):
    def get(self, request):
        flats = Flat.objects.all()
        flatfilter = FlatFilter(request.GET, queryset=flats)
        flats = flatfilter.qs
        return render(request, 'search.html',context={'flatfilter':flatfilter, 'flats': flats})


    # def get(self, request):
    #     type = request.GET.get("type")
    #     phrase = request.GET.get("phrase")
    #     if type == "flat":
    #         results = Flat.objects.filter(street__contains=phrase)
    #         return render(request, "search.html", context={"results": results})
    #     return render(request, "search.html")

class LeaseAgreementList(LoginRequiredMixin, ListView):
    model = LeaseAgreement
    template_name = 'list_view.html'

class LeaseAgreementCreate(LoginRequiredMixin, CreateView):
    form_class = LeaseAgreementForm
    template_name = "form.html"
    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse('lease_agreement_list')

class LeaseAgreementUpdate(LoginRequiredMixin, UpdateView):
    model = LeaseAgreement
    fields = "__all__"
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('leaseagreement_list')

class LeaseAgreementDelete(LoginRequiredMixin, DeleteView):
    model = LeaseAgreementForm
    fields = "__all__"
    template_name = 'form.html'

class LeaseAgreementDetails(LoginRequiredMixin,DetailView):
    model = LeaseAgreement
    template_name = "flat_lease_agreement.html"
    ordering = ['end_of_contract']
    # def get(self, request, pk):
    #     leaseagreement = LeaseAgreement.objects.get(pk=pk)
    #
    #     return render(request, "leaseagreement_detail.html" ,
    #                   context = { "leaseagreement": leaseagreement,
    #                               })
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return get_object_or_404(LeaseAgreement, pk=pk)

class FlatList(LoginRequiredMixin,ListView):
    model = Flat
    template_name = 'list_view.html'
    ordering = ['city']

class FlatCreate(LoginRequiredMixin, CreateView):
    form_class = FlatForm
    template_name = "form.html"
    success_url = reverse_lazy('flat_list')

class FlatUpdate(LoginRequiredMixin, UpdateView):
    model = Flat
    fields = "__all__"
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('flat_list')

class FlatDelete(LoginRequiredMixin, DeleteView):
    model = Flat
    fields = "__all__"
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('flat_list')

class RoomCreate(LoginRequiredMixin, CreateView):
    form_class = RoomForm
    template_name = "form.html"
    success_url = reverse_lazy('flat_list')

class RoomDelete(LoginRequiredMixin, DeleteView):
    model = Room
    fields = "__all__"
    template_name = 'form.html'


class RentierList(LoginRequiredMixin,ListView):
    model = Rentier
    template_name = 'list_view.html'
    ordering = ['last_name']

class RentierCreate(LoginRequiredMixin, CreateView):
    form_class = RentierForm
    template_name = "form.html"
    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse('rentier_list')

class RentierUpdate(LoginRequiredMixin, UpdateView):
    model = Rentier
    fields = "__all__"
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('rentier_list')

class RentierDelete(LoginRequiredMixin, DeleteView):
    model = Rentier
    fields = "__all__"
    template_name = 'form.html'
    success_url = "rentier_list"


class OwnerList(LoginRequiredMixin,ListView):
    model = Owner
    template_name = 'list_view.html'
    ordering = ['last_name']

class OwnerCreate(LoginRequiredMixin,CreateView):
    form_class = OwnerForm
    template_name = "form.html"
    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse('owner_list')

class OwnerUpdate(LoginRequiredMixin, UpdateView):
    model = Owner
    fields = "__all__"
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('owner_list')

class OwnerDelete(LoginRequiredMixin, DeleteView):
    model = Owner
    fields = "__all__"
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('owner_list')


class AgnetList(LoginRequiredMixin,ListView):
    model = Agent
    template_name = 'list_view.html'
    ordering = ['last_name']

class AgnetCreate(LoginRequiredMixin, CreateView):
    form_class = AgentForm
    template_name = "form.html"
    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse('agent_list')

class AgentUpdate(LoginRequiredMixin, UpdateView):
    model = Agent
    fields = "__all__"
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('agent_list')

class AgentDelete(LoginRequiredMixin, DeleteView):
    model = Agent
    fields = "__all__"
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('agent_list')

class RoomCreate(LoginRequiredMixin, CreateView):
    form_class = RoomForm
    template_name = "form.html"
    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse('flat_list')