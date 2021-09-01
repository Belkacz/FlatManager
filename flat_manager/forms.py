from django import forms
from django.forms import SelectDateWidget

from flat_manager.models import LeaseAgreement, Rentier, Owner, Room, Flat, Agent


class LeaseAgreementForm(forms.ModelForm):
    class Meta:
        model = LeaseAgreement
        widgets = {"end_of_contract" : SelectDateWidget(years=range(1990, 2100)),
                   "contract_date" : SelectDateWidget(years=range(1990, 2100))}
        fields = "__all__"
        labels = { "contract_number" : "numer umowy",
                   "contract_date" : "data poczatku umowy",
                   "end_of_contract" : "data końca umowy",
                   "date_of_payment" : "termin płatności",
                   "monthly_cost" : "miesieczy koszt",
                   "agent_provision" : "prowizja agenta",
                   "number_of_keys" : "liczba kompletóþw kluczy",
                   "damage_desc" : "opis uszkodzeń",
                   "deposit" : "kaucja",
                   "owner" : "właściciel",
                   "flat" : "mieszkanie",
                   "rooms" : "pokoje",
                   }
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("contract_date")
        end_date = cleaned_data.get("end_of_contract")
        deposit = cleaned_data.get("deposit")
        number_of_keys = cleaned_data.get("number_of_keys")
        agent_provision = cleaned_data.get("agent_provision")
        if end_date < start_date:
            raise forms.ValidationError("poącztek umowy nie moze być przed jej zakończeniem.")
        if deposit < 0:
            raise forms.forms.ValidationError("Kaucja nie mozę być ujemna.")
        if number_of_keys < 0:
            raise forms.forms.ValidationError("Musi być przynajmniej jedna para kluczy.")
        if agent_provision < 0:
            raise forms.forms.ValidationError("Prowizja nie mozę być ujemna.")

class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = "__all__"
        labels = {"city": " miasto",
                  "street": "ulica",
                  "house_number": "nr. budynku",
                  "flat_number": "nr. mieszkania",
                  "post_code": "kod pocztowy",
                  "flat_surface": "powierzchnia mieszkania",
                  "basic_flat_rental_cost": "cena najmu",
                  "owner": "właściciel",
                  }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        labels = {"basic_room_rental_cost": "cena najmu pokoju",
                  "room_surface": "powierzchnia pokoju",
                  "flat": "mieszkanie",
                  "room_number": "nr. pokoju",
                  }

class RentierForm(forms.ModelForm):
    class Meta:
        model = Rentier
        widgets = {}
        fields = "__all__"
        widgets = {"date_of_birth" : SelectDateWidget(years=range(1900, 2100))}
        labels = {"first_name": "imię",
                  "last_name": "nazwisko",
                  "pesel": "pesel",
                  "contact_number": "nr. telfonu",
                  "date_of_birth": "data urodzenia",
                  }

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        widgets = {}
        fields = "__all__"
        widgets = {"date_of_birth" : SelectDateWidget(years=range(1900, 2100))}
        labels = {"first_name": "imię",
                  "last_name": "nazwisko",
                  "pesel": "pesel",
                  "contact_number": "nr. telfonu",
                  "date_of_birth": "data urodzenia",
                  }


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        widgets = {}
        fields = "__all__"
        labels = {"first_name": "imię",
                  "last_name": "nazwisko",
                  "pesel": "pesel",
                  "contact_number": "nr. telfonu",
                  "agency": "agencja",
                  }

# class RoomCreateForm(forms.ModelForm):
#     class Meta:
#         model = Room
#         widgets = {}
#         fields = "__all__"