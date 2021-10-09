
from .models import Product
from bootstrap_modal_forms.forms import BSModalModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ProductCreationForm(BSModalModelForm):
    class Meta:
        model = Product
        fields = ['name','price','desc','img','stock']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Product Name"
        self.fields['price'].label = "Product Price"
        self.fields['img'].label = "Upload Product Image"
        self.fields['desc'].label = "Product Description"
        self.fields['desc'].widget.attrs['rows'] = 4
        self.fields['stock'].label = "Product Stock"
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Row(
                Column('price', css_class='form-group col-md-6 mb-0'),
                Column('stock', css_class='form-group col-md-6 mb-0 text-center'),
                css_class='form-row justify-content-between align-items-center'
            ),
            'img',
            'desc',
            Row(
                Column(Submit('submit', 'Submit',css_class='btn btn-success w-100'),css_class='modal-footer col mb-0')
            )
            

        )

