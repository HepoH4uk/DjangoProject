from django.forms import ModelForm, BooleanField
from catalog.models import Products
from django.core.exceptions import ValidationError


forbidden_words= [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin,ModelForm):
    class Meta:
        model = Products
        exclude = ('views_counter',)

    def clean_name(self):
        name = self.cleaned_data["name"]
        lowered = name.lower()
        for word in forbidden_words:
            if word in lowered:
                raise ValidationError(f'В названии есть запрещенное слово: "{word}".')
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        lowered = description.lower()
        for word in forbidden_words:
            if word in lowered:
                raise ValidationError(f'В описании есть запрещенное слово: "{word}".')
        return description

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data["purchase_price"]
        if purchase_price is not None and purchase_price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return purchase_price
