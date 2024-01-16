from django import forms


class EditRoomForm(forms.Form):
    name = forms.CharField(label='Name of room', required=True)
    capacity = forms.IntegerField(label='Capacity of room', required=True, min_value=1)
    projector = forms.BooleanField(label='Projector accessibility', required=False)
