from django import forms
from .models import Provider

class ProviderForm(forms.ModelForm):
	class Meta:
		model = Provider
		fields = ['ruc','businessName','status','province','distric','registrationDate','address','phone','effectiveTime','email','contactName','contactPhone']
		error_messages = {' businessName': {'max_length': ("This provider's name is too long."),},}


	def __init__(self,*args, **kwargs):
		super(ProviderForm,self).__init__(*args,**kwargs)
		self.fields['ruc'].widget.attrs.update({'class' : 'form-control','id' : 'ruc','name' : 'ruc', 'type' : 'text', 'placeholder' : 'Ingrese el RUC..'})
		self.fields['businessName'].widget.attrs.update({'class' : 'form-control','id' : 'businessName','name' : 'businessName', 'type' : 'text', 'placeholder' : 'Ingrese el nombre de su compañía..'})
		self.fields['status'].widget.attrs.update({'class' : 'form-control','id' : 'status','name' : 'status', 'size' : '1',  'placeholder' : 'Seleccione un estado..'})
		self.fields['province'].widget.attrs.update({'class' : 'form-control','id' : 'province','name' : 'province', 'type' : 'text', 'placeholder' : 'Ingrese la provincia..'})
		self.fields['distric'].widget.attrs.update({'class' : 'form-control','id' : 'distric','name' : 'distric', 'type' : 'text', 'placeholder' : 'Ingrese el distrito..'})
		self.fields['registrationDate'].widget.attrs.update({'class' : 'js-datepicker form-control', 'data-date-format' : 'yyyy-mm-dd', 'id' : 'registrationDate','name' : 'registrationDate', 'placeholder' : 'Ingrese una fecha..'})
		self.fields['address'].widget.attrs.update({'class' : 'form-control','id' : 'address','name' : 'address', 'type' : 'text', 'placeholder' : 'Ingrese la dirección..'})
		self.fields['phone'].widget.attrs.update({'class' : 'form-control','id' : 'phone','name' : 'phone', 'type' : 'text', 'placeholder' : 'Ingrese el teléfono..'})
		self.fields['effectiveTime'].widget.attrs.update({'class' : 'form-control','id' : 'effectiveTime','name' : 'effectiveTime', 'type' : 'text', 'placeholder' : 'Ingrese el tiempo de vigencia..'})
		self.fields['email'].widget.attrs.update({'class' : 'form-control','id' : 'email','name' : 'email', 'type' : 'text', 'placeholder' : 'Ingrese el email..'})
		self.fields['contactName'].widget.attrs.update({'class' : 'form-control','id' : 'contactName','name' : 'contactName', 'type' : 'text', 'placeholder' : 'Ingrese nombre de contacto..'})
		self.fields['contactPhone'].widget.attrs.update({'class' : 'form-control','id' : 'contactPhone','name' : 'contactPhone', 'type' : 'text', 'placeholder' : 'Ingrese el número de contacto..'})

