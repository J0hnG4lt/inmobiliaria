import { Injectable } from '@angular/core';
import { Filtros } from './filtros.component.js'

/*
Este servicio pasa los filtros desde filtros.component al app.component y app.component se lo
pasa a cada grid.component como argumento en el template
*/

@Injectable()
export class FiltrosService {
	public filtrosAplicados: Filtros;
	
	public event : Event;

	constructor(){
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

	
}