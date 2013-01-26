import django.forms as forms

class NewGameForm(forms.Form):
    player_name = forms.CharField(max_length = 100)
    password = forms.CharField(max_length = 100)

class JoinGameForm(forms.Form):
    player_name = forms.CharField(max_length = 100)
    game_id = forms.IntegerField(min_value = 0)
    password = forms.CharField(max_length = 100)
    
class SetBPMForm(forms.Form):
    bpm = forms.IntegerField(min_value = 0)
    game_id = forms.IntegerField(min_value = 0)
    player_name = forms.CharField(max_length = 100)

class SetMasterBPMForm(forms.Form):
    bpm = forms.IntegerField(min_value = 0)
    game_id = forms.IntegerField(min_value = 0)
