import { Injectable } from '@angular/core';
import { Filtros } from './filtros.component.js'
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import 'rxjs/Rx';
import {Observable} from 'rxjs/Rx'

/*
Este servicio pasa los filtros desde filtros.component al app.component y app.component se lo
pasa a cada grid.component como argumento en el template
*/


@Injectable()
export class FiltrosService {
	public filtrosAplicados: Filtros;
	
	public event : Event;

	server_url = "http://127.0.0.1:8000/vinmuebles/";
	serviceData : any;

	constructor(public http: Http){
		this.event = new Event("filtroSubmitted");
	}
	
	// Actualiza los filtros
	compartirDatos(datos: Filtros): void{
		this.filtrosAplicados = datos;
		window.dispatchEvent(this.event);

	}

	// Obtengo los filtros
	obtenerDatos(): Filtros {
		
		return this.filtrosAplicados;
	}

	private extractData(res : any) {

		if (res.status < 200 || res.status >= 300) {
		  throw new Error('Bad response status: ' + res.status);
		}

		
		this.serviceData = (res.json());
		return this.serviceData || {};
	}

	public cargarPaises(): Observable<any> {
		
		return this.http.get(this.server_url+"obtener_paises").map(this.extractData);
		
	}

	public cargarEstados(pais : string): Observable<any> {
		
		return this.http.get(this.server_url+"obtener_estados/"+pais).map(this.extractData);
		
	}

	public cargarMunicipios(pais : string, estado : string): Observable<any> {
		
		return this.http.get(this.server_url+"obtener_municipios/"+pais+"/"+estado).map(this.extractData);
		
	}

}