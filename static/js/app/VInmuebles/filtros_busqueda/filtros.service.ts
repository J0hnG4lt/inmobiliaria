import { Injectable } from '@angular/core';
import { Filtros } from './filtros.component.js'



@Injectable()
export class FiltrosService {
	public filtrosAplicados: Filtros;
	public reiniciado: boolean = false;
	public nuevoFiltro: boolean = false;
	constructor(){}
	
	compartirDatos(datos: Filtros): void{
		this.filtrosAplicados = datos;
		this.reiniciado = false;
		this.nuevoFiltro = true;
	}

	obtenerDatos(): Filtros {
		
		return this.filtrosAplicados;
	}

	reiniciar():void{
		this.reiniciado = true;
		this.nuevoFiltro = false;
	}

	
}