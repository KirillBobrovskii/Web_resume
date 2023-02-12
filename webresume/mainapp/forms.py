from django import forms


class EmailForm(forms.Form):
    message = forms.CharField(label='Заинтересовало резюме? Вы можете отправить письмо автору.',
                              widget=forms.Textarea)
