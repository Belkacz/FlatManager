import pytest
from django.test import TestCase

from django.test import Client
from django.urls import reverse, resolve

from .conftest import *
from .models import *
from .views import *

@pytest.mark.djnago_db
def test_home():
    c = Client()
    response = c.get("/home/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_Owner_List_get_logged(user, ownerfixture):
    client = Client()
    client.force_login(user)
    response = client.get("/home/owner-list")
    assert response.status_code == 200
    # assert response.context['object'] == ownerfixture

@pytest.mark.django_db
def test_Owner_List_get_not_logged(user):
    client = Client()
    response = client.get("/home/owner-list")
    assert response.status_code == 302


@pytest.mark.django_db
def test_Create_OwnerGET_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("owner_create"))
    assert response.status_code == 200

@pytest.mark.django_db
def test_Create_OwnerGET_not_logged(user):
    client = Client()
    response = client.get(reverse("owner_create"))
    assert response.status_code == 302

@pytest.mark.django_db
def test_Create_OwnerPOST_logged(user):
    client = Client()
    client.force_login(user)
    data = {"first_name" : "Janusz", "last_name" : "Zamożny", "pesel" : 64010709887, "date_of_birth": '1964-01-07',
                         "contact_number": 653754788}

    response = client.post(reverse("owner_create"), data)
    of = Owner.objects.first()
    assert response.status_code == 302
    assert of.first_name == data['first_name']
    assert Owner.objects.count() == 1

@pytest.mark.django_db
def test_Update_Owner_View_get_loged(user, ownerfixture):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("owner_update", args=(ownerfixture.id,)))
    assert response.status_code == 200
    assert response.context['object'] == ownerfixture

@pytest.mark.django_db
def test_Update_Owner_View_post_logged(user, ownerfixture):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("owner_update", args=(ownerfixture.id,)))

    assert response.status_code == 200
    of = Owner.objects.first()
    assert of.first_name == ownerfixture.first_name
    assert response.context['object'] == ownerfixture

@pytest.mark.django_db
def test_get_update_Owner_not_login(ownerfixture):
    client = Client()
    response = client.get(reverse("owner_update", args=(ownerfixture.id,)))
    assert response.status_code == 302
    login_url = reverse('login')
    assert response.url.startswith(login_url)

@pytest.mark.django_db
def test_DeleteTweetView_get(user, ownerfixture):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("owner_delete", args=(ownerfixture.id,)))
    assert response.status_code == 302
    assert Owner.objects.count() == 0

@pytest.mark.django_db
def test_DeleteTweetView_get_not_logged(user, ownerfixture):
    client = Client()
    response = client.post(reverse("owner_delete", args=(ownerfixture.id,)))
    assert response.status_code == 302

@pytest.mark.django_db
def test_Owner_List_get_logged(user, ownerfixture):
    client = Client()
    client.force_login(user)
    response = client.get("/home/owner-list")
    assert response.status_code == 200
    # assert response.context['object'] == ownerfixture

@pytest.mark.django_db
def test_Owner_List_get_not_logged(user):
    client = Client()
    response = client.get("/home/owner-list")
    assert response.status_code == 302


@pytest.mark.django_db
def test_Create_OwnerGET_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("owner_create"))
    assert response.status_code == 200

@pytest.mark.django_db
def test_Create_OwnerGET_not_logged(user):
    client = Client()
    response = client.get(reverse("owner_create"))
    assert response.status_code == 302

@pytest.mark.django_db
def test_Create_OwnerPOST_logged(user):
    client = Client()
    client.force_login(user)
    data = {"first_name" : "Janusz", "last_name" : "Zamożny", "pesel" : 64010709887, "date_of_birth": '1964-01-07',
                         "contact_number": 653754788}

    response = client.post(reverse("owner_create"), data)
    of = Owner.objects.first()
    assert response.status_code == 302
    assert of.first_name == data['first_name']
    assert Owner.objects.count() == 1

@pytest.mark.django_db
def test_Update_Owner_View_get_loged(user, ownerfixture):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("owner_update", args=(ownerfixture.id,)))
    assert response.status_code == 200
    assert response.context['object'] == ownerfixture

@pytest.mark.django_db
def test_Update_Owner_View_post_logged(user, ownerfixture):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("owner_update", args=(ownerfixture.id,)))

    assert response.status_code == 200
    of = Owner.objects.first()
    assert of.first_name == ownerfixture.first_name
    assert response.context['object'] == ownerfixture

@pytest.mark.django_db
def test_get_update_Owner_not_login(ownerfixture):
    client = Client()
    response = client.get(reverse("owner_update", args=(ownerfixture.id,)))
    assert response.status_code == 302
    login_url = reverse('login')
    assert response.url.startswith(login_url)

@pytest.mark.django_db
def test_DeleteOwnerView_get(user, ownerfixture):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("owner_delete", args=(ownerfixture.id,)))
    assert response.status_code == 302
    assert Owner.objects.count() == 0

@pytest.mark.django_db
def test_DeleteOwnerView_get_not_logged(user, ownerfixture):
    client = Client()
    response = client.post(reverse("owner_delete", args=(ownerfixture.id,)))
    assert response.status_code == 302

###########

@pytest.mark.django_db
def test_Agent_List_get_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get("/home/agent-list")
    assert response.status_code == 200

@pytest.mark.django_db
def test_Agent_List_get_not_logged(user):
    client = Client()
    response = client.get("/home/agent-list")
    assert response.status_code == 302


@pytest.mark.django_db
def test_Create_AgentGET_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("agent_create"))
    assert response.status_code == 200

@pytest.mark.django_db
def test_Create_AgentGET_not_logged(user):
    client = Client()
    response = client.get(reverse("agent_create"))
    assert response.status_code == 302

@pytest.mark.django_db
def test_Create_AgentPOST_logged(user):
    client = Client()
    client.force_login(user)
    data = {"first_name" : "Agent", "last_name" : "Tomel", "agency" : "tajna", "contact_number": 43213}

    response = client.post(reverse("agent_create"), data)
    ag = Agent.objects.first()
    assert response.status_code == 302
    assert ag.first_name == data['first_name']
    assert Agent.objects.count() == 1

@pytest.mark.django_db
def test_Update_Agent_View_get_loged(user, agentfixture):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("agent_update", args=(agentfixture.id,)))
    assert response.status_code == 200
    assert response.context['object'] == agentfixture

@pytest.mark.django_db
def test_Update_Agent_View_post_logged(user, agentfixture):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("agent_update", args=(agentfixture.id,)))

    assert response.status_code == 200
    af = Agent.objects.first()
    assert af.first_name == agentfixture.first_name
    assert response.context['object'] == agentfixture

@pytest.mark.django_db
def test_get_update_Agent_not_login(agentfixture):
    client = Client()
    response = client.get(reverse("agent_update", args=(agentfixture.id,)))
    assert response.status_code == 302
    login_url = reverse('login')
    assert response.url.startswith(login_url)

@pytest.mark.django_db
def test_DeleteAgentView_get(user, agentfixture):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("agent_delete", args=(agentfixture.id,)))
    assert response.status_code == 302
    assert Agent.objects.count() == 0

@pytest.mark.django_db
def test_DeleteAgentView_get_not_logged(user, agentfixture):
    client = Client()
    response = client.post(reverse("agent_delete", args=(agentfixture.id,)))
    assert response.status_code == 302

################################


@pytest.mark.django_db
def test_Agent_Flat_get_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get("/home/flat-list")
    assert response.status_code == 200

@pytest.mark.django_db
def test_Agent_Flat_get_not_logged():
    client = Client()
    response = client.get("/home/flat-list")
    assert response.status_code == 302


@pytest.mark.django_db
def test_Create_Flat_GET_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("flat_create"))
    assert response.status_code == 200

@pytest.mark.django_db
def test_Create_Flat_GET_not_logged(user):
    client = Client()
    response = client.get(reverse("flat_create"))
    assert response.status_code == 302

@pytest.mark.django_db
def test_Create_Flat_POST_logged(user):
    client = Client()
    client.force_login(user)
    ow = {"first_name": "Janusz", "last_name": "Zamożny", "pesel": 64010709887, "date_of_birth": '1964-01-07',
            "contact_number": 653754788}
    data = {"city":"Łódź", "street":"pomorska", "house_number":69, "flat_number":96, "post_code":120123,
                            "flat_surface":31, "basic_flat_rental_cost":500, "owner" : ow}

    response = client.post(reverse("flat_create"), data)
    fl = Flat.objects.first()
    # assert response.status_code == 302
    # assert fl.city == data['city']
    # assert Flat.objects.count() == 1

@pytest.mark.django_db
def test_Update_Flat_View_get_loged(user, flatfixture):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("flat_update", args=(flatfixture.id,)))
    assert response.status_code == 200
    assert response.context['object'] == flatfixture

@pytest.mark.django_db
def test_Update_Flat_View_post_logged(user, flatfixture):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("flat_update", args=(flatfixture.id,)))

    assert response.status_code == 200
    fl = Flat.objects.first()
    assert fl.city == flatfixture.city
    assert response.context['object'] == flatfixture

@pytest.mark.django_db
def test_get_update_Flat_not_login(flatfixture):
    client = Client()
    response = client.get(reverse("flat_update", args=(flatfixture.id,)))
    assert response.status_code == 302
    login_url = reverse('login')
    assert response.url.startswith(login_url)

@pytest.mark.django_db
def test_DeleteFlatView_get(user, flatfixture):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("flat_delete", args=(flatfixture.id,)))
    assert response.status_code == 302
    assert Flat.objects.count() == 0

@pytest.mark.django_db
def test_DeleteFlatView_get_not_logged(user, flatfixture):
    client = Client()
    response = client.post(reverse("flat_delete", args=(flatfixture.id,)))
    assert response.status_code == 302

#################

@pytest.mark.django_db
def test_Rentier_List_get_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get("/home/rentier-list")
    assert response.status_code == 200

@pytest.mark.django_db
def test_Rentier_List_get_not_logged(user):
    client = Client()
    response = client.get("/home/rentier-list")
    assert response.status_code == 302


@pytest.mark.django_db
def test_Create_RentierGET_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("rentier_create"))
    assert response.status_code == 200

@pytest.mark.django_db
def test_Create_AgentGET_not_logged(user):
    client = Client()
    response = client.get(reverse("rentier_create"))
    assert response.status_code == 302

@pytest.mark.django_db
def test_Create_RentierPOST_logged(user):
    client = Client()
    client.force_login(user)
    data = {"first_name" : "Kamil", "last_name" : "Biedny", "pesel" : "9995578849", "contact_number": 43213,
            "date_of_birth":'1999-01-07'}

    response = client.post(reverse("rentier_create"), data)
    re = Rentier.objects.first()
    assert response.status_code == 302
    assert re.first_name == data['first_name']
    assert Rentier.objects.count() == 1

@pytest.mark.django_db
def test_Update_Rentier_View_get_loged(user, rentierfixture):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("rentier_update", args=(rentierfixture.id,)))
    assert response.status_code == 200
    assert response.context['object'] == rentierfixture

@pytest.mark.django_db
def test_Update_Rentier_View_post_logged(user, rentierfixture):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("rentier_update", args=(rentierfixture.id,)))

    assert response.status_code == 200
    re = Rentier.objects.first()
    assert re.first_name == rentierfixture.first_name
    assert response.context['object'] == rentierfixture

@pytest.mark.django_db
def test_get_update_Rentier_not_login(rentierfixture):
    client = Client()
    response = client.get(reverse("rentier_update", args=(rentierfixture.id,)))
    assert response.status_code == 302
    login_url = reverse('login')
    assert response.url.startswith(login_url)

@pytest.mark.django_db
def test_DeleteRentierView_get(user, rentierfixture):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("rentier_delete", args=(rentierfixture.id,)))
    assert response.status_code == 302
    assert Agent.objects.count() == 0

@pytest.mark.django_db
def test_DeleteRentierView_get_not_logged(user, rentierfixture):
    client = Client()
    response = client.post(reverse("rentier_delete", args=(rentierfixture.id,)))
    assert response.status_code == 302


###############
#
@pytest.mark.django_db
def test_LeaseAgreement_List_get_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get("/home/leaseagreement-list")
    assert response.status_code == 200

@pytest.mark.django_db
def test_LeaseAgreement_List_get_not_logged(user):
    client = Client()
    response = client.get("/home/leaseagreement-list")
    assert response.status_code == 302


# class TestViews(TestCase,user,ownerfixture):
#     def setUp(self):
#         self.client = Client().force_login(user)
#         self.crate_owner_url = reverse('owner_create')
#
#     def test_Create_Owner(self.crate_owner_url, user, ownerfixture):
#         response = client.get(reverse(crate_owner_url))
#         self.assertEquals(response.status_code, 200)


# @pytest.mark.django_db
# def test_CreateFlat_get(user):
#     client = Client()
#     client.force_login(user)
#     response = client.get(reverse("flat_create"))
#     assert response.status_code == 200


# @pytest.mark.djnago_db
# def test_view_LeaseAgreementList():
#     client = Client()
#     client.force_login(user)
#     response = client.get(reverse('lease_agreement_list'))
#     assert response.status_code == 200


# @pytest.mark.djnago_db
# class TestView(TestCase):
#     def test_view_LeaseAgreementList(self):
#         client = Client()
#         client.force_login(user)
#         response = client.get(reverse('lease_agreement_list'))
#         self.assertEquals(response.status_code, 200)

# class Test_URLS(TestCase):
#     @pytest.mark.djnago_db
#     def test_url_LeaseAgreementCreate(self):
#         url = reverse('index')
#         r = resolve(url).func
#         self.assertEquals(r.__module__, url.__module__ )


