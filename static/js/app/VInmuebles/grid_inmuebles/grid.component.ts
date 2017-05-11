import { Component, OnInit, HostListener, Input} from '@angular/core';
import { InmuebleService } from './grid.service.js';
import { Inmueble } from './inmueble_resumen/inmueble.component.js';
import { Filtros } from '../filtros_busqueda/filtros.component.js';

/*
Esta funcion convierte a un objecto inmueble los datos llegados
desde el back-end
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
		inmueble.estado = objeto.fields.estado;
		inmueble.municipio = objeto.fields.municipio;
		inmueble.tipoDeOperacion = objeto.fields.tipoDeOperacion;
		inmuebles.push(inmueble);
		i++;
	}

	return inmuebles;
}




/*
Este template corresponde a una pagina
*/

@Component({
  selector: 'grid-inmuebles',
  templateUrl:'grid_inmuebles',
  providers: [InmuebleService]
})
export class GridComponent implements OnInit { 
	
	inmuebles : any[] = [];
	enElFondo : boolean = false;
	aunFaltan : boolean = true;
	@Input() numeroDePagina : number;
	@Input() filtrosAplicados : Filtros;
	numeroDePaginaSiguiente : number;
	sePuedeCargarLaSiguiente : boolean = false;

	constructor(private inmuebleService : InmuebleService){


	}

	ngOnInit(): void {
		if (this.aunFaltan){
			// Cargar los inmuebles de esta pagina usando filtros
	    	this.inmuebleService.loaddata(this.numeroDePagina, this.filtrosAplicados).subscribe(data => {
      			// Construyo los inmuebles con la data y arreglo el numero de pagina
	      		this.inmuebles = construirInmuebles(data);

	      		// Determina si hacen falta mas paginas
	      		// Esto se hace para terminar la recursion
	      		//  en el template.
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
	
	// Cuando llego al fondo de la pagina debo cargar mas inmuebles
	@HostListener('window:scroll',[])
	onScroll(evento : any): void {
	let docHeight : number = Math.max(
        document.body.scrollHeight, document.documentElement.scrollHeight,
        document.body.offsetHeight, document.documentElement.offsetHeight,
        document.body.clientHeight, document.documentElement.clientHeight
    );
	if ((window.innerHeight + window.scrollY+15) >= docHeight) {
			this.enElFondo = true;

	    }
	    
	}


}