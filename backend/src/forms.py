from django import forms


class FileUpload(forms.Form):
    excel_file = forms.FileField(
        label='Excel File', required=True)
