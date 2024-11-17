from django import forms


class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=True)


class ExampleForm(forms.Form):
    """
    A sample form for demonstration purposes.
    Add your fields here based on requirements.
    """
    title = forms.CharField(
        max_length=100, 
        required=True, 
        help_text="Enter the title of the book"
    )
    description = forms.CharField(
        widget=forms.Textarea, 
        required=False, 
        help_text="Optional: Provide a brief description"
    )
    publish_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        help_text="Optional: Specify the publish date"
    )
