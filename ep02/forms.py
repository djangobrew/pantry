from crispy_bulma.layout import Submit
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field
from django import forms

from ep02 import models


class BasicForm(forms.Form):
    """
    A basic form example with some custom field validation.
    """

    favorite_color = forms.CharField(max_length=100)

    def clean_favorite_color(self):
        color = self.cleaned_data.get("favorite_color")

        if color == "bad":
            raise forms.ValidationError("Oopsie! That's a bad color!")

        return color


class EmployeeForm(forms.ModelForm):
    """
    A model form for our `Employee` model.

    This form contains validation checks on specific fields
    as well as multiple fields together to show how the form
    validation process works.
    """

    class Meta:
        model = models.Employee
        exclude = ["hired_on"]

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        if first_name.lower() == "bad":
            raise forms.ValidationError("Woah! Bad employee first name!")

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")

        if last_name.lower() == "bad":
            raise forms.ValidationError("Hold up! Bad employee last name!")

        return last_name

    def clean_job(self):
        job = self.cleaned_data.get("job")

        if job.lower() == "bad":
            raise forms.ValidationError("Oh boy! Bad employee job name!")

        return job

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        job = cleaned_data.get("job")

        # need to check if all the fields exist in `cleaned_data` first,
        # since it's possible that some are missing and there are already
        # field specific errors, check `self.errors`
        if all([first_name, last_name, job]):
            if (
                (first_name.lower() == "spongebob")
                and (last_name.lower() == "squarepants")
                and (job.lower() != "fry cook")
            ):
                raise forms.ValidationError("Spongebob must be a fry cook!")

        return cleaned_data


class EmployeeForm2(forms.ModelForm):
    """
    A model form for our `Employee` model.

    This form overrides the default field validators from the model
    by increasing the original max length of some fields.

    The purpose here is to showcase how custom form validators cannot
    override model validation.
    """

    class Meta:
        model = models.Employee
        exclude = ["hired_on"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Modify widgets to exceed default max length
        fname_widget = self.fields["first_name"].widget
        lname_widget = self.fields["last_name"].widget
        job_widget = self.fields["job"].widget

        fname_widget.attrs.update(maxlength=int(fname_widget.attrs["maxlength"]) + 50)
        lname_widget.attrs.update(maxlength=int(lname_widget.attrs["maxlength"]) + 50)
        job_widget.attrs.update(maxlength=int(job_widget.attrs["maxlength"]) + 50)


class BasicForm2(forms.Form):
    """
    A basic form example with multiple fields.
    """

    favorite_color = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=1, max_value=100)
    nickname = forms.CharField(max_length=100)
    bio = forms.CharField(widget=forms.Textarea)

    def clean_favorite_color(self):
        color = self.cleaned_data.get("favorite_color")

        if color == "bad":
            raise forms.ValidationError("Oopsie! That's a bad color!")

        return color

    def clean_age(self):
        age = self.cleaned_data.get("age")

        if age == 100:
            raise forms.ValidationError("Yoikes...questionable age...")

        return age

    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")

        if nickname == "bad":
            raise forms.ValidationError("Oh no! That's a bad nickname...")

        return nickname

    def clean_bio(self):
        bio = self.cleaned_data.get("bio")

        if bio == "bad":
            raise forms.ValidationError("Yikes! Invalid bio!")

        return bio

    def clean(self):
        cleaned_data = super().clean()

        nickname = self.cleaned_data.get("nickname")
        bio = self.cleaned_data.get("bio")

        if nickname and bio:
            if (nickname.lower() == "spongebob") and ("sponge" not in bio.lower()):
                raise forms.ValidationError("Spongebob needs to declare he is a sponge in bio!")

        return cleaned_data


class BasicForm3(BasicForm2):
    """
    The same fields as `BasicForm2` except we're adding
    some crispy-form helpers in the `__init__`!
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # crispy-forms helper!
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field("favorite_color", placeholder="hot pink"),
            Field("age", placeholder=200),
            Field("nickname", placeholder="Squidward"),
            Field("bio", placeholder="Hiya!"),
            Submit("submit", "Submit!!"),
        )


class CommentForm(forms.Form):
    """
    A basic form to capture a comment.
    """

    comment = forms.CharField(
        max_length=50,
    )
    author = forms.CharField(
        max_length=20,
    )

    def clean_comment(self):
        comment = self.cleaned_data.get("comment")

        if comment == "bad":
            raise forms.ValidationError("Whoops! That's a bad comment!")

        return comment

    def clean_author(self):
        author = self.cleaned_data.get("author")

        if author == "bad":
            raise forms.ValidationError("Nope! Bad author alert!")

        return author
