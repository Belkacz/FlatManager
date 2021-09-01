import pytest
from django.contrib.auth.models import User

from flat_manager.models import *


@pytest.fixture
def user():
    u = User()
    u.username = "belka"
    u.save()
    return u

@pytest.fixture
def ownerfixture():
    ow = Owner.objects.create(first_name="Janusz", last_name="Zamożny", pesel=64010709887, date_of_birth='1964-01-07',
                         contact_number=653754788)
    return ow

@pytest.fixture
def agentfixture():
    ag = Agent.objects.create(first_name="Agent", last_name="Tomel", agency='tajna', contact_number = 43213)
    return ag

@pytest.fixture
def flatfixture():
    ow = Owner.objects.create(first_name="Janusz", last_name="Zamożny", pesel=64010709887, date_of_birth='1964-01-07',
                              contact_number=653754788)
    fl = Flat.objects.create(city="Łódź", street="pomorska", house_number=69, flat_number =96, post_code=65485,
                            flat_surface=31, basic_flat_rental_cost=500, owner = ow)
    return fl

@pytest.fixture
def rentierfixture():
    re = Rentier.objects.create(first_name="Kamil", last_name="Biedny", pesel=9995578849, date_of_birth='1999-01-07',
                              contact_number=653754788)
    return re

# @pytest.fixture
# def LeaseAgreement():
#     la = LeaseAgreement
#     LeaseAgreement.objects.create(contract_number=1, date_of_payment=10, end_of_contract='2025-01-01',
#                                   contract_date='2020-01-01', monthly_cost=500, agent_provision=500,
#                                   damage_desc="brudne ściany", )