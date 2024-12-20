from django import forms

class FeedBackForm(forms.Form):
	name=forms.CharField()
	rollno=forms.IntegerField()
	email=forms.EmailField()
	FeedBack=forms.CharField(widget=forms.Textarea)
	def clean_name(self):
		n=self.cleaned_data['name']
		if len(n)<4:
			raise forms.ValidationError("Min no of Characters must be >=4")
		return n
	def clean_rollno(self):
		r=self.cleaned_data['rollno']
		if r<=0:
			raise forms.ValidationError("Rollno must be positive value")
		return r