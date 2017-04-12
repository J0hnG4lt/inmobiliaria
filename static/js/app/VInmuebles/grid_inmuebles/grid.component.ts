import { Component, OnInit } from '@angular/core';
import { InmuebleService } from './grid.service.js';
import { Inmueble } from './inmueble_resumen/inmueble.component.js';


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