# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# TODO: actualizar las nacionalidades del class usuario
# TODO: discutir si se puede usar esto https://github.com/SmileyChris/django-countries/
# TODO: actualizar el tipo de divisa en class ofertadeinmueble
# TODO: discutir si es buena idea colocar el tipo de divisa
# TODO: determinar como usar el FileField con las fotos o el FilePathField o el ImageField
# TODO: usar los validadores
# TODO: especificar los unique fields
# TODO: discutir si se agregan fields de parroquia y municipio
# TODO: agregar los mensajes de error de los fields (Field.error_messages)


# TODO: discutir sobre el ISO-3166 # https://en.wikipedia.org/wiki/ISO_3166-1_numeric
# https://coderwall.com/p/2z_e5g/import-iso-3166-1-countries-names-and-codes-in-a-django-model

"""

TESTS para el shell de django

from vinmuebles.models import OfertaDeInmueble, Usuario

usu = Usuario(nombres="Georvic Alejandro",apellidos="Tur Rojas",cedula=25367182,nacionalidad="VE",direccion="Una dirección",telefono="4324243243",correo="alexanderstower@gmail.com")

edi = OfertaDeInmueble(precio="200000000", divisa="BS", descripcion="Mi Apartamento", tipoDeInmueble="AP", tipoDeOperacion="VE", antiguedadDeInmueble="50",numeroDeHabitaciones="3", numeroDeBanyos="3", nombreDelInmueble="Edificio 8", numeroDeEstacionamientos="1", metrosDeConstruccion="600", metrosDeTerreno="700", direccion="Direccion del edificio",fotoPrincipalURL ="static/img/certConf.jpg", sePuedeMostrar=True, comprado=False)

"""

"""
	tipoDeInmueble = models.CharField( max_length=2,
									   choices=( ("CA","Casa"),
									   			 ("AP","Apartamento"),
									   			 ("QU","Quinta"),
									   			 ("TE","Terreno"),
									   			 ("LO","Local"),
									   			 ("CO","Comercio"),
									   			 ("OF","Oficina"),
									   			 ("IN","Informal") ),
									   default="CA",
									   null=False,
									   blank=False,
									   verbose_name= u"Tipo de Inmueble",
									   help_text= u"Usar una de las opciones")
"""

class TipoDeInmueble(models.Model) :

	nombreTipoDeInmueble = models.CharField(max_length=20,
										   null=False,
										   blank=False,
										   verbose_name=u"Nombre del tipo de inmueble",
										   help_text=u"Coloque el nombre de un tipo de inmueble")



"""
	tipoDeOperacion = models.CharField( max_length=2,
									   choices=( ("VE","Venta"),
									   			 ("AL","Alquiler") ),
									   default="VE",
									   verbose_name= u"Tipo de Operación",
									   help_text= u"Usar una de las opciones")
"""

class TipoDeOperacion(models.Model) :

	nombreDelTipoDeOperacion = models.CharField(max_length=20,
										   null=False,
										   blank=False,
										   verbose_name=u"Nombre del tipo de operación",
										   help_text=u"Coloque el nombre de un tipo de operación")


class Divisa(models.Model) :

	nombreMoneda = models.CharField(max_length=20,
							   null=False,
							   blank=False,
							   verbose_name=u"Nombre de la moneda",
							   help_text=u"Coloque el nombre de una divisa")

	simbolo = models.CharField(max_length=20,
							   null=True,
							   blank=True,
							   verbose_name=u"Símbolo de la moneda",
							   help_text=u"Coloque el símbolo de una divisa. Si es vacío se usa el nombre.")



class Pais(models.Model) :

	nombrePais = models.CharField(max_length=20,
							   null=False,
							   blank=False,
							   verbose_name=u"Nombre del país",
							   help_text=u"Coloque el nombre de un país")

	divisa = models.ForeignKey(Divisa,
								null=True,
								blank=True)




class Estado(models.Model) :

	nombreEstado = models.CharField(max_length=20,
							   null=False,
							   blank=False,
							   verbose_name=u"Nombre del estado",
							   help_text=u"Coloque el nombre de un estado")

	pais = models.ForeignKey(Pais)



class PrimeraDivisionAdministrativa(models.Model) :

	nombreDivision = models.CharField(max_length=20,
							   null=False,
							   blank=False,
							   verbose_name=u"Nombre de la división administrativa (Ej: Municipio) siguiente a Estado o Provincia",
							   help_text=u"Coloque el nombre de una división administrativa siguiente a Estado o Provincia")

	estado = models.ForeignKey(Estado)

class Foto(models.Model) :
	titulo = models.CharField(       max_length=20,
									 blank=False,
									 null=False,
									 verbose_name= u"Título de la foto",
									 help_text= u"Colocar el título de una foto")

	fotoPrincipalURL = models.TextField(      verbose_name= u"Foto principal del inmueble",
											  null=False,
											  blank=False,
											  help_text= u'Dirección de la foto en el servidor')



class OfertaDeInmueble(models.Model) :

	# Atributos Obligatorios del Modelo

	precio = models.DecimalField(   max_digits=20, 
									decimal_places=2,
									null=False,
									blank=False,
									verbose_name= u"Precio del inmueble",
									help_text= u"Usar el formato <em>321.32</em>")

	divisa = models.ForeignKey(		 Divisa,
									 blank=False,
							 		 null=False,
									 verbose_name= u"Moneda en la que se oferta el inmueble",
									 help_text= u"Usar el nombre de la divisa")	

	descripcion = models.TextField( null=False,
									blank=False,
									verbose_name= u"Breve descripción")


	tipoDeInmueble = models.ForeignKey(TipoDeInmueble,
							 blank=False,
							 null=False)

	tipoDeOperacion = models.ForeignKey(TipoDeOperacion,
							 blank=False,
							 null=False)

	antiguedadDeInmueble = models.PositiveSmallIntegerField( max_length=3,
												null=False,
												blank=False,
												verbose_name= u"Cantidad de años desde su construcción",
												help_text= u"Usar un entero positivo")

	numeroDeHabitaciones = models.PositiveSmallIntegerField( max_length=3,
												null=False,
												blank=False,
												verbose_name= u"Cantidad de habitaciones",
												help_text= u"Usar un entero positivo")

	numeroDeBanyos = models.PositiveSmallIntegerField( max_length=3,
												null=False,
												blank=False,
												verbose_name= u"Cantidad de baños",
												help_text= u"Usar un entero positivo")

	nombreDelInmueble = models.CharField( max_length=40,
										  null=False,
										  blank=False,
										  verbose_name= u"Nombre del inmueble",
										  help_text= u"Colocar el nombre del inmueble")

	numeroDeEstacionamientos = models.PositiveSmallIntegerField( max_length=3,
													null=False,
													blank=False,
													verbose_name= u"Número de estacionamientos",
													help_text= u"Usar un entero positivo")

	metrosDeConstruccion = models.PositiveIntegerField( max_length=10,
													null=False,
													blank=False,
													verbose_name= u"Metros cuadrados de construcción",
													help_text= u"Usar un entero positivo")

	metrosDeTerreno = models.PositiveIntegerField(  max_length=10,
													null=False,
													blank=False,
													verbose_name= u"Metros cuadrados de terreno",
													help_text= u"Usar un entero positivo")

	direccion = models.TextField(         null=False,
										  blank=False,
										  verbose_name= u"Dirección completa del inmueble con país, estado, municipio, parroquia y avenida.",
										  help_text= u"Colocar la dirección del inmueble")

	pais = models.ForeignKey(Pais,
							 blank=False,
							 null=False)

	estado = models.ForeignKey(Estado,
							 blank=False,
							 null=False)

	municipio = models.ForeignKey(PrimeraDivisionAdministrativa,
							 blank=False,
							 null=False)

	# No usar el otro field para URLs
	fotoPrincipalURL = models.TextField(  verbose_name= u"Foto principal del inmueble",
										  null=False,
										  blank=False)

	sePuedeMostrar =  models.BooleanField(  default=True,
										    verbose_name= u"Si se puede mostrar a los visitantes",
										    help_text= u"Usar un valor booleano")

	#Atributos No asociados al API

	fechaDeCreacion = models.DateField( auto_now_add=True)

	fechaDeUltimaActualizacion = models.DateField(  auto_now=True)

	comprado = models.BooleanField(  default=False,
								     verbose_name= u"Si ya fue comprado",
								     help_text= u"Usar un valor booleano")


class FotosSecundariasURLs(models.Model) :

	fotosSecundariaURL = models.TextField(verbose_name= u"Foto secundaria del inmueble",
										  null=False,
										  blank=False)

	inmueble = models.ForeignKey(         OfertaDeInmueble,
										  on_delete=models.CASCADE)

class CaracteristicasAdicionales(models.Model) :
	caracteristica = models.CharField(    max_length=40,
										  default="",
										  blank=True,
										  verbose_name= u"Característica especial del inmueble")

	inmueble = models.ForeignKey(         OfertaDeInmueble,
										  on_delete=models.CASCADE)

class InstalacionesComodidades(models.Model) :
	instalacion = models.CharField(       max_length=40,
										  default="",
										  blank=True,
										  verbose_name= u"Instalaciones adicionales")

	inmueble = models.ForeignKey(         OfertaDeInmueble,
										  on_delete=models.CASCADE)

class Cercanias(models.Model) :
	cercania = models.CharField(          max_length=40,
										  default="",
										  blank=True,
										  verbose_name= u"Sitios notables cercanos al inmueble")

	inmueble = models.ForeignKey(         OfertaDeInmueble,
										  on_delete=models.CASCADE)

class Detalles(models.Model) :
	detalle = models.CharField(           max_length=40,
										  default="",
										  blank=True,
										  verbose_name= u"Detalles adicionales")

	inmueble = models.ForeignKey(         OfertaDeInmueble,
										  on_delete=models.CASCADE)


class Usuario(models.Model) :

	nombres = models.CharField( 	max_length=40,
									blank=False,
									null=False,
									verbose_name= u"Nombres del usuario")

	apellidos = models.CharField( 	max_length=40,
									blank=False,
									null=False,
									verbose_name= u"Apellidos del usuario")

	cedula = models.IntegerField(   max_length=20,
									blank=False,
									null=False,
									verbose_name= u"Cédula o identificación del usuario",
									unique=True)

	nacionalidad = models.CharField( max_length=20,
									 blank=False,
									 null=False,
									 verbose_name= u"Nacionalidad del usuario" )

	direccion = models.TextField(     null=False,
								      blank=False,
									  verbose_name= u"Dirección completa del usuario",
									  unique=True,
									  help_text= u"Colocar la dirección completa del usuario.")
	
	telefono = models.CharField(blank=False, 
								unique=True,
								max_length=15)

	correo = models.EmailField(	 max_length=254,
								 verbose_name= u"Correo electrónico del usuario",
								 unique=True)

	foto = models.ForeignKey(Foto,
								null=True,
								blank=True)


