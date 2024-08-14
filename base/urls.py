from django.urls import path, include
from . import views

# mtbets/


urlpatterns = [
    path(""                             , views.prueba          , name='prueba'),

    path("area-personal/"               , views.areaPersonal    , name='area personal'),

    path("academia/"                    , views.academia        , name='academia'),
    path("academia/matchedbetting/"     , views.academiaMB      , name='academiaMB'),
    path("academia/surebetting/"        , views.academiaSB      , name='academiaSB'),
    
    path("servicios/"                   , views.servicios       , name='servicios'),
    path("servicios/matchedbetting/"    , views.serviciosMB     , name='serviciosMB'),
    path("servicios/surebetting/"       , views.serviciosSB     , name='serviciosSB'),

    path("login/"                       , views.login           , name='login'),
    path("registro/"                    , views.register        , name='registro'),
    
]