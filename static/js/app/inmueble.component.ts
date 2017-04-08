import { Component, OnInit } from '@angular/core';
import { InmuebleService } from './inmueble.service.js'


export class Inmueble {
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
}


@Component({
  selector: 'my-inmuebles',
  template: `
  	<div id="grid_de_inmuebles">  
  			<div class="inmueble" *ngFor="let inmuebl of inmuebles">
  				{{inmuebl.descripcion}}
  			</div>
  	</div>
  	`,
  providers: [InmuebleService]
})
export class InmuebleComponent implements OnInit { 
	
	inmuebles : Inmueble[];

	constructor(private inmuebleService : InmuebleService){

	}

	getInmuebles():void{
		this.inmuebleService.getInmuebles().then(Inmuebles => this.inmuebles = Inmuebles);
	}

	ngOnInit(): void {
	    this.getInmuebles();
	}

}