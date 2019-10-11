from django import forms
from .models import Reservation

class ReservationPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['title'].widget = forms.TextInput()
        self.fields['title'].widget.attrs = {'class': "form-control", 'placeholder': "예약합니다."}

        self.fields['name'].label = "입금자명"
        self.fields['name'].widget = forms.TextInput()
        self.fields['name'].widget.attrs = {'class': "form-control", 'placeholder': "입금자명"}

        self.fields['date_to'].label = "시작시간"

        self.fields['date_to'].label = "종료시간"

        self.fields['num_people'].label = "인원"
        self.fields['num_people'].widget.attrs = {'class': "form-control", 'placeholder': "인원을 선택해주세요"}

        self.fields['amount'].label = "입금 금액"
        self.fields['amount'].widget = forms.TextInput()
        self.fields['amount'].widget.attrs = {'class': "form-control", 'placeholder': "입금 금액"}

        self.fields['contact'].label = "연락처"
        self.fields['contact'].widget = forms.TextInput()
        self.fields['contact'].widget.attrs = {'class': "form-control", 'placeholder': "ex) 010-0000-0000"}

        self.fields['email'].label = "Email"
        self.fields['email'].widget.attrs = {'class': "form-control", 'placeholder': "ex) email@email.com"}

        self.fields['rental'].label = "대여물품"
        self.fields['rental'].widget = forms.TextInput()
        self.fields['rental'].widget.attrs = {'class': "form-control", 'placeholder': "대여할 물품을 입력해주세요"}

        self.fields['password'].label = "비밀번호"
        self.fields['password'].widget = forms.PasswordInput()