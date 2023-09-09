from django.urls import path
from .views import home, contact, about
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    # Ruta URL para la página de inicio. La función 'home' es la vista asociada y se le asigna el nombre 'home'.

    path('contact/', contact, name='contact'),
    # Ruta URL para la página de contacto. La función 'contact' es la vista asociada y se le asigna el nombre 'contact'.

    path('about/', about, name='about'),
    # Ruta URL para la página de contacto. La función 'contact' es la vista asociada y se le asigna el nombre 'contact'.

    # path('login_1/', GeneralLoginView.as_view(), name='login_1'),
    # Ruta URL para la página de inicio de sesión. La vista basada en clase 'GeneralLoginView' se utiliza como vista y se le asigna el nombre 'login_1'.

    # path('logout_1/', LogoutView.as_view(next_page='login_1'), name='logout_1'),
    # Ruta URL para la página de cierre de sesión. La vista basada en clase 'LogoutView' se utiliza como vista y se le asigna el nombre 'logout_1'.

    # path('register_1/', GeneralRegisterPage.as_view(), name='register_1'),
    # Ruta URL para la página de registro. La vista basada en clase 'GeneralRegisterPage' se utiliza como vista y se le asigna el nombre 'register_1'.
]
