from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from localflavor.us.forms import USPhoneNumberField, USStateField, USZipCodeField, USStateSelect
from generic.forms import CountryField, CountrySelect  

USDA_ZONE_CHOICES = (
	('-', '-'),
	('1a', '1a'),
	('1b', '1b'),
	('2a', '2a'),
	('2b', '2b'),
	('3a', '3a'),
	('3b', '3b'),
	('4a', '4a'),
	('4b', '4b'),
	('5a', '5a'),
	('5b', '5b'),
	('6a', '6a'),
	('6b', '6b'),
	('7a', '7a'),
	('7b', '7b'),
	('8a', '8a'),
	('8b', '8b'),
	('9a', '9a'),
	('9b', '9b'),
	('10a', '10a'),
	('10b', '10b'),
	('11a', '11a'),
	('11b', '11b'),
	('12a', '12a'),
	('12b', '12b')
)

def as_table_func(self):
	return self._html_output(
		normal_row = '<tr%(html_class_attr)s><th>%(label)s</th><td>%(field)s%(errors)s%(help_text)s</td></tr>',
		error_row = '<tr><td colspan="2">%s</td></tr>',
		row_ender = '</td></tr>',
		help_text_html = '<br /><span class="helptext">%s</span>',
		errors_on_separate_row = False)

class SeedNetworkBaseForm(forms.Form):
	def as_table(self):
		"Returns this form rendered as HTML <tr>s -- excluding the <table></table>."
		return as_table_func(self)

class ModifiedUserCreationForm(UserCreationForm):
	required_css_class = 'required'


class MemberInfoForm(SeedNetworkBaseForm):
	required_css_class = 'required'
	first_name = forms.CharField(max_length=150, required=True)
	last_name = forms.CharField(max_length=150, required=True)
	usda_zone =forms.ChoiceField(required=False, choices=USDA_ZONE_CHOICES)
	email = forms.CharField(max_length=150, required=True)
	email_is_public = forms.BooleanField(required=False, initial=True)
	phone = USPhoneNumberField(max_length=150, required=False)
	phone_is_public = forms.BooleanField(required=False, initial=True)
        
        country_code = CountryField(required=True, widget=CountrySelect, label=None, initial='US', help_text='', error_messages=None, show_hidden_initial=False, validators=[], localize=False, disabled=False, label_suffix=None)
        street_line = forms.CharField(widget=forms.Textarea(attrs={'rows'    :'3', 'cols':'60'}), required=False)
        state = USStateField(required=False, widget=USStateSelect, label=None, initial=None, help_text='', error_messages=None, show_hidden_initial=False, validators=[], localize=False, disabled=False, label_suffix=None)
        zipcode = USZipCodeField(max_length=None, min_length=None, required=False)
	street_address_is_public = forms.BooleanField(required=False, initial=True)
        
	mailing_address = forms.CharField(widget=forms.Textarea(attrs={'rows':'3', 'cols':'60'}), required=False, help_text="(Optional for US addresses)")
	mailing_address_is_public = forms.BooleanField(required=False, initial=True)

	about_me = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="i.e. Describe your work, interests, projects, growing conditions, etc")
	include_in_member_profiles = forms.BooleanField(required=False, initial=True)

	def clean(self):
    		cleaned_data = super(MemberInfoForm, self).clean()
    		country_code = cleaned_data.get("country_code")
    		zipcode = cleaned_data.get("zipcode")
                state = cleaned_data.get("state")
    		if country_code == "US"  and (not zipcode or not state):
        		raise forms.ValidationError("zipcode and state are required fields for US addresses.")
    		return cleaned_data

class SeedNetworkAuthForm(AuthenticationForm):
	def as_table(self):
		return as_table_func(self)

class SeedNetworkPasswordChangeForm(PasswordChangeForm):
	def as_table(self):
		return as_table_func(self)

