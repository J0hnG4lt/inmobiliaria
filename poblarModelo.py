# -*- coding: utf-8 -*-

from vinmuebles.models import TipoDeInmueble
from vinmuebles.models import TipoDeOperacion
from vinmuebles.models import Divisa
from vinmuebles.models import Pais
from vinmuebles.models import Estado
from vinmuebles.models import PrimeraDivisionAdministrativa
from vinmuebles.models import Foto
from vinmuebles.models import OfertaDeInmueble
from vinmuebles.models import FotosSecundariasURLs
from vinmuebles.models import CaracteristicasAdicionales
from vinmuebles.models import InstalacionesComodidades
from vinmuebles.models import Cercanias
from vinmuebles.models import Detalles 
from vinmuebles.models import Usuario

# IMPORTANTE:
# Para ejecutar este script, correr python manage.py shell
# una vez allí dentro, usar la siguiente función execfile("poblarModelo.py")


# TODO: determinar si hay una manera más segura de poblar el modelo
	# VER: https://docs.djangoproject.com/en/dev/ref/models/querysets/#update-or-create

TipoDeInmueble.objects.all().delete()
TipoDeOperacion.objects.all().delete()
Divisa.objects.all().delete()
Pais.objects.all().delete()
Estado.objects.all().delete()
PrimeraDivisionAdministrativa.objects.all().delete()
Foto.objects.all().delete()
OfertaDeInmueble.objects.all().delete()
FotosSecundariasURLs.objects.all().delete()
CaracteristicasAdicionales.objects.all().delete()
InstalacionesComodidades.objects.all().delete()
Cercanias.objects.all().delete()
Detalles.objects.all().delete()
Usuario.objects.all().delete()



def guardarInstancias(listaDeInstancias):
	for instancia in listaDeInstancias :
		instancia.save()


tiposDeInmuebles = [TipoDeInmueble(nombreTipoDeInmueble=u"Casa"),
					TipoDeInmueble(nombreTipoDeInmueble=u"Apartamento"), 
					TipoDeInmueble(nombreTipoDeInmueble=u"Quinta"),
					TipoDeInmueble(nombreTipoDeInmueble=u"Terreno"),
					TipoDeInmueble(nombreTipoDeInmueble=u"Local"),
					TipoDeInmueble(nombreTipoDeInmueble=u"Comercio"),
					TipoDeInmueble(nombreTipoDeInmueble=u"Oficina"),
					TipoDeInmueble(nombreTipoDeInmueble=u"Informal")]

guardarInstancias(tiposDeInmuebles)



tipoDeOperaciones = [TipoDeOperacion(nombreDelTipoDeOperacion=u"Venta"),
					 TipoDeOperacion(nombreDelTipoDeOperacion=u"Alquiler")]

guardarInstancias(tipoDeOperaciones)


divisas = [Divisa(nombreMoneda=u"Bolívar",simbolo=u"BS"),
		   Divisa(nombreMoneda=u"US Dollar",simbolo=u"$")]

guardarInstancias(divisas)

DivisaBolivarID = Divisa.objects.filter(nombreMoneda=u"Bolívar")[0]
DivisaDollarID = Divisa.objects.filter(nombreMoneda=u"US Dollar")[0]

paises = [Pais(nombrePais=u"Venezuela",
			   divisa=DivisaBolivarID,
			   nacionalidad=u"Venezolano"),
		  Pais(nombrePais=u"United States",
			   divisa=DivisaDollarID,
			   nacionalidad="American")]

guardarInstancias(paises)

venezuelaID = Pais.objects.filter(nombrePais=u"Venezuela")[0]

estados = [Estado(nombreEstado=u"Miranda",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Carabobo",
				  pais=venezuelaID),
		   Estado(nombreEstado="Lara",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Mérida",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Trujillo",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Distrito Capital",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Nueva Esparta",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Cojedes",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Apure",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Delta Amacuro",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Bolívar",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Amazonas",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Falcón",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Portuguesa",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Aragua",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Vargas",
				  pais=venezuelaID),
		   Estado(nombreEstado="Zulia",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Barinas",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Guárico",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Sucre",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Táchira",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Yaracuy",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Anzoátegui",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Monagas",
				  pais=venezuelaID),
		   Estado(nombreEstado=u"Dependencias Federales",
				  pais=venezuelaID)]

guardarInstancias(estados)

caracasID = Estado.objects.filter(nombreEstado=u"Distrito Capital")[0]
mirandaID = Estado.objects.filter(nombreEstado=u"Miranda")[0]

primerasDivisiones = [PrimeraDivisionAdministrativa(nombreDivision=u"Libertador",estado=caracasID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Acevedo",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Andrés Bello",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Baruta",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Brión",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Bolívar",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Buroz",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Carrizal",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Chacao",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"El Hatillo",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Guaicaipuro",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Gual",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Independencia",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Lander",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Los Salias",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Páez",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Paz Castillo",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Plaza",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Rojas",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Sucre",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Urdaneta",estado=mirandaID),
					  PrimeraDivisionAdministrativa(nombreDivision=u"Zamora",estado=mirandaID)]

guardarInstancias(primerasDivisiones)

fotos = [Foto(titulo="certConf",fotoPrincipalURL="static/img/certConf.jpg")]

guardarInstancias(fotos)

casaID = TipoDeInmueble.objects.filter(nombreTipoDeInmueble=u"Casa")[0]
tipoOperacionID = TipoDeOperacion.objects.filter(nombreDelTipoDeOperacion=u"Venta")[0]

hatilloID = PrimeraDivisionAdministrativa.objects.filter(nombreDivision=u"El Hatillo")[0]

ofertasInmuebles = [OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 1", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa 2", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 2", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 3", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 4", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 5", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 6", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 7", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 8", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 9", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 10", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 11", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 12", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 13", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 14", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 15", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 16", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 17", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 18", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 19", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 20", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False),
					OfertaDeInmueble(precio=200000000, 
									 divisa=DivisaBolivarID, 
									 descripcion=u"Mi Casa", 
									 tipoDeInmueble=casaID, 
									 tipoDeOperacion=tipoOperacionID, 
									 antiguedadDeInmueble=50,
									 numeroDeHabitaciones=3, 
									 numeroDeBanyos=3, 
									 nombreDelInmueble=u"Casa 21", 
									 numeroDeEstacionamientos=1, 
									 metrosDeConstruccion=600, 
									 metrosDeTerreno=700, 
									 direccion=u"Direccion de la casa",
									 pais=venezuelaID,
									 estado=mirandaID,
									 municipio=hatilloID,
									 fotoPrincipalURL ="static/img/certConf.jpg", 
									 sePuedeMostrar=True, 
									 comprado=False)]

guardarInstancias(ofertasInmuebles)

miCasaInmuebleID = OfertaDeInmueble.objects.filter(nombreDelInmueble=u"Casa 8")[0]

fotosSecundarias = [FotosSecundariasURLs(fotosSecundariaURL="static/img/certConf.jpg",
										 inmueble=miCasaInmuebleID)]

guardarInstancias(fotosSecundarias)

caracteristicasAdicionales = [CaracteristicasAdicionales(caracteristica=u"Tiene de todo",
														 inmueble=miCasaInmuebleID)]

guardarInstancias(caracteristicasAdicionales)

instalacionesComodidades = [InstalacionesComodidades(instalacion=u"Tiene ascensor",
													 inmueble=miCasaInmuebleID)]

guardarInstancias(instalacionesComodidades)

cercanias = [Cercanias(cercania=u"Puesto de tequeños",
					   inmueble=miCasaInmuebleID)]

guardarInstancias(cercanias)

detalles = [Detalles(detalle=u"Es perfecto",
					 inmueble=miCasaInmuebleID)]

guardarInstancias(detalles)

fotoID = Foto.objects.filter(titulo=u"certConf")[0]

usuarios = [Usuario(nombres="Georvic Alejandro",
					apellidos="Tur Rojas",
					cedula=25367182,
					nacionalidad=venezuelaID,
					direccion="Una dirección",
					telefono="4324243243",
					correo="alexanderstower@gmail.com",
					foto=fotoID)]

guardarInstancias(usuarios)

