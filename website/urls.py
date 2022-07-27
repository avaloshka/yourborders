from django.urls import path
from .import views


urlpatterns = [
	path('', views.home, name='home'),
	path('belarus_poland', views.belarus_poland, name='belarus_poland'),
	path('grigorov', views.grigorov, name='grigorov'),
	path('urbany', views.urbany, name='urbany'),
	path('vidzy', views.vidzy, name='vidzy'),
	path('kotlovka', views.kotlovka, name='kotlovka'),
	path('losha', views.losha, name='losha'),
	path('kamenny_log', views.kamenny_log, name='kamenny_log'),
	path('beniakoni', views.beniakoni, name='beniakoni'),
	path('privalka', views.privalka, name='privalka'),
	path('bruzgi', views.bruzgi, name='bruzgi'),
	path('berestovitsa', views.berestovitsa, name='berestovitsa'),
	path('peschatka', views.peschatka, name='peschatka'),
	path('kozlovichi', views.kozlovichi, name='kozlovichi'),
	path('brest', views.brest, name='brest'),
	path('domachevo', views.domachevo, name='domachevo'),
	path('tomashovka', views.tomashovka, name='tomashovka'),
	path('oltush', views.oltush, name='oltush'),
	path('mokrany', views.mokrany, name='mokrany'),
	path('mohro', views.mohro, name='mohro'),
	path('nevel', views.nevel, name='nevel'),
	path('verhni_terebezhev', views.verhni_terebezhev, name='verhni_terebezhev'),
	path('glushkevichi', views.glushkevichi, name='glushkevichi'),
	path('novaya_rudnya', views.novaya_rudnya, name='novaya_rudnya'),
	path('aleksandrovka', views.aleksandrovka, name='aleksandrovka'),
	path('komarin', views.komarin, name='komarin'),
	path('novaya_guta', views.novaya_guta, name='novaya_guta'),
	path('veselovka', views.veselovka, name='veselovka'),
	path('uznat_svou_ochered', views.uznat_svou_ochered, name='uznat_svou_ochered'),
	path('poland', views.poland, name='poland'),
	path('error', views.error, name='error'),
	path('feedback', views.feedback, name='feedback')
]