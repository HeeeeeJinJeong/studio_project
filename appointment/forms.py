from django import forms
from .models import Appointment

class AppointmentPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['title'].widget = forms.TextInput()
        self.fields['title'].widget.attrs = {'class': "form-control", 'placeholder': "예약합니다."}

        self.fields['name'].label = "입금자명"
        self.fields['name'].widget = forms.TextInput()
        self.fields['name'].widget.attrs = {'class': "form-control", 'placeholder': "입금자명"}

        self.fields['amount'].label = "입금 금액"
        self.fields['amount'].widget = forms.TextInput()
        self.fields['amount'].widget.attrs = {'class': "form-control", 'placeholder': "입금 금액"}

        self.fields['contact'].label = "연락처"
        self.fields['contact'].widget = forms.TextInput()
        self.fields['contact'].widget.attrs = {'class': "form-control", 'placeholder': "ex) 010-0000-0000"}

        self.fields['text'].label = "대여물품"
        self.fields['text'].widget = forms.TextInput()
        self.fields['text'].widget.attrs = {'class': "form-control", 'placeholder': "대여할 물품을 입력해주세요"}

        self.fields['password'].label = "비밀번호"
        self.fields['password'].widget = forms.PasswordInput()

        self.fields['num_people'].label = "인원"
        self.fields['num_people'].widget.attrs = {'class': "form-control", 'placeholder': "인원을 선택해주세요"}

        self.fields['email'].label = "Email"
        self.fields['email'].widget.attrs = {'class': "form-control", 'placeholder': "ex) email@email.com"}

        self.fields['date'].label = "이용날짜"
        self.fields['date'].widget = forms.TextInput()
        self.fields['date'].widget.attrs = {'class': "form-control", 'placeholder': "이용하실 날짜를 입력해주세요"}

        self.fields['time'].label = "이용시간"
        self.fields['time'].widget = forms.TextInput()
        self.fields['time'].widget.attrs = {'class': "form-control", 'placeholder': "이용하실 시간을 입력해주세요"}