import { Injectable } from '@angular/core';
import { Inmueble } from './inmueble_resumen/inmueble.component.js';


import { Http, Response } from '@angular/http';
import 'rxjs/Rx';
import {Observable} from 'rxjs/Rx'

@Injectable()
export class InmuebleService {

	server_url = "http://127.0.0.1:8000/vinmuebles/";
	serviceData : any;
	constructor(public http: Http) { }


	private extractData(res : any) {

		if (res.status < 200 || res.status >= 300) {
		  throw new Error('Bad response status: ' + res.status);
		}

		// console.log(res.json());
		this.serviceData = (res.json());
		return this.serviceData || {};
	}

	loaddata(pagina=0): Observable<any> {
		return this.http.get(this.server_url+pagina.toString(10)).map(this.extractData);
	}
	
}