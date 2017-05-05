import { Injectable } from '@angular/core';
import { Filtros } from './filtros.component.js'



@Injectable()
export class FiltrosService {
	public filtrosAplicados: Filtros;
	
	constructor(){}
	
	compartirDatos(datos: Filtros): void{
		this.filtrosAplicados = datos;
		console.log("Ya fue pasado el formulario al filtros.service.ts");
		console.log(this.filtrosAplicados);
	}

	obtenerDatos(): Filtros {
		
		console.log("Aplicando obtenerDatos()");
		console.log(this.filtrosAplicados);
		return this.filtrosAplicados;
	}

	
}