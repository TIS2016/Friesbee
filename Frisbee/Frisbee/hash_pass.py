import django
try:
        from django.contrib.auth.models import User
        from django.contrib.auth.hashers import make_password

        users = User.objects.all()

        for user in users:
                if 'pbkdf2_sha256' not in user.password:
                        user.password = (make_password(password=user.password,salt=None,hasher='pbkdf2_sha256'))
                        user.save()
except django.db.utils.ProgrammingError:
        pass
