import { Component, OnInit } from '@angular/core';
import { InmuebleService } from './grid.service.js';
import { Inmueble } from './inmueble_resumen/inmueble.component.js';


/*
  id_inmueble: number;
  descripcion: string;
  precio:number;
  direccion:string;
  areaConstruccion:number;
  areaTerreno:number;
  numeroHabitaciones:number;
  numeroBanyos:number;
  numeroEstacionamientos:number;
  tipoInmueble:string;
  urlImagenPrincipal : string;
  urlImagenesSecundarias : string[];

*/

function construirInmuebles(datos:any){
	let inmuebles : Inmueble[] = [];
	let i = 0;
	for(var objeto of datos){
		let inmueble = new Inmueble();
		inmueble.descripcion = objeto.fields.descripcion;
		inmueble.precio = objeto.fields.precio;
		inmueble.direccion = objeto.fields.direccion;
		inmueble.areaConstruccion = objeto.fields.metrosDeConstruccion;
		inmueble.areaTerreno = objeto.fields.metrosDeTerreno;
		inmueble.numeroBanyos = objeto.fields.numeroDeBanyos;
		inmueble.numeroHabitaciones = objeto.fields.numeroDeHabitaciones;
		inmueble.numeroEstacionamientos = objeto.fields.numeroDeEstacionamientos;
		inmueble.tipoInmueble = objeto.fields.tipoDeInmueble;
		inmueble.urlImagenPrincipal = objeto.fields.fotoPrincipalURL;
		inmueble.urlImagenesSecundarias = [];
		inmuebles.push(inmueble);
		i++;
	}
	return inmuebles;
}

@Component({
  selector: 'my-inmuebles',
  template: `
  	<div id="grid_de_inmuebles">  
  			<div class="inmueble" *ngFor="let inmuebl of inmuebles">
  				<my-inmueble [inmuebleActual]="inmuebl" ></my-inmueble>
  			</div>
  	</div>
  	`,
  providers: [InmuebleService]
})
export class GridComponent implements OnInit { 
	
	inmuebles : any[];

	constructor(private inmuebleService : InmuebleService){


	}

	getInmuebles():void{
		this.inmuebleService.getInmuebles().then(Inmuebles => this.inmuebles = Inmuebles);
		alert("HOLA");
	}


	ngOnInit(): void {
	    this.inmuebleService.loaddata().subscribe(data => {
      		// do something with the data
      		this.inmuebles = construirInmuebles(data);
    	})
	}

}