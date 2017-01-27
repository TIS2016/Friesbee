def save(self, commit=True):
    # Save the provided password in hashed format
    user = super(MyForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password"])
    if commit:
        user.save()
    return user
