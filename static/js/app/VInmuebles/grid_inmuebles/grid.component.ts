import { Component, OnInit, HostListener, Input } from '@angular/core';
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
	let listaDeInmuebles : any[] = datos.slice(0, -1);
	for(var objeto of listaDeInmuebles){
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
  	<div class="grid_de_inmuebles">  
  			<div class="inmueble" *ngFor="let inmuebl of inmuebles">
  				<my-inmueble [inmuebleActual]="inmuebl" ></my-inmueble>
  			</div>
  			<my-inmuebles *ngIf="aunFaltan && enElFondo && sePuedeCargarLaSiguiente" [numeroDePagina]="numeroDePaginaSiguiente"></my-inmuebles>
  	</div>
  	`,
  providers: [InmuebleService]
})
export class GridComponent implements OnInit { 
	
	inmuebles : any[];
	enElFondo : boolean = false;
	aunFaltan : boolean = true;
	@Input() numeroDePagina : number;
	numeroDePaginaSiguiente : number;
	sePuedeCargarLaSiguiente : boolean = false;

	constructor(private inmuebleService : InmuebleService){


	}


	ngOnInit(): void {
		if (this.aunFaltan){
	    	this.inmuebleService.loaddata(this.numeroDePagina).subscribe(data => {
      		// do something with the data

	      		this.inmuebles = construirInmuebles(data);

		      	if (data[data.length-1].aunFaltanPaginas == false){
		      			this.aunFaltan = false;
		      	}
					this.numeroDePaginaSiguiente = this.numeroDePagina;
					this.numeroDePaginaSiguiente += 1;
					this.sePuedeCargarLaSiguiente = true;
		    }

    	)
	    }
	    }
	

	@HostListener('window:scroll',[])
	onScroll(evento : any): void {
	if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
			this.enElFondo = true;

	    }
	    
	}


}