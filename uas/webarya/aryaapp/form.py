from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    pesan = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print(f"email dari {self.cleaned_data['email']} dengan pesan: {self.cleaned_data['pesan']}")
