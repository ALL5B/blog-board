from django import forms
from .models import Chat,Board

class ChatCreateForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ('name', 'text')
        # 少しツウな書き方
        widgets = {
            'name': forms.TextInput(attrs={  # <input type="text" class="form-control"
                'class': 'form-control',
            }),
            'text': forms.Textarea(attrs={  # <textarea class="form-cotrol"
                'class': 'form-control',

            }),
        }



class BoardCreateForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title','text','junle')

        widgets = {
            'title': forms.TextInput(attrs={  # <input type="text" class="form-control"
                'class': 'form-control',
            }),
            'junle': forms.Select(attrs={  # <textarea class="form-cotrol"
                'class': 'form-control',
            }),
            'test': forms.Textarea(attrs={  # <textarea class="form-cotrol"
                'class': 'form-control',

            }),

        }

