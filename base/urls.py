from django.urls import path
from . import views

# mtbets/


urlpatterns = [
    path(""                             , views.home            , name='home'),

    path("area-personal/"               , views.areaPersonal    , name='area_personal'),

    path("academia/"                    , views.academia        , name='academia'),
    path("academia/matchedbetting/"     , views.academiaMB      , name='academiaMB'),
    path("academia/surebetting/"        , views.academiaSB      , name='academiaSB'),
    
    path("servicios/"                   , views.servicios       , name='servicios'),
    path("servicios/matchedbetting/"    , views.serviciosMB     , name='serviciosMB'),
    path("servicios/surebetting/"       , views.serviciosSB     , name='serviciosSB'),

    path("login/"                       , views.loginPage       , name='login'),
    path("registro/"                    , views.registerPage    , name='registro'),
    path("logout/"                      , views.logoutUser      , name='logout'),
]