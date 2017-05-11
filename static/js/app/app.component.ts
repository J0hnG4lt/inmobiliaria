import { Component, OnInit, Inject, HostListener } from '@angular/core';

import { FiltrosService } from './VInmuebles/filtros_busqueda/filtros.service.js';
import { GridComponent } from './VInmuebles/grid_inmuebles/grid.component.js';
import { FiltrosComponent, Filtros } from './VInmuebles/filtros_busqueda/filtros.component.js';

//TODO: cuando el contador de filtros aplicados llegue a 100 hay que refrescar la página


function compararFiltros(filtro1: Filtros, filtro2: Filtros): boolean{


  if (filtro1.antiguedadMax != filtro2.antiguedadMax){
    return false;
  }
  else if (filtro1.numeroBanyos != filtro2.numeroBanyos){
    return false;
  }
  else if (filtro1.numeroEstacionamientos != filtro2.numeroEstacionamientos){
    return false;
  }
  else if (filtro1.numeroHabitaciones != filtro2.numeroHabitaciones){
    return false;
  }
  else if (filtro1.operacion != filtro2.operacion){
    return false;
  }
  else if (filtro1.precioMax != filtro2.precioMax){
    return false;
  }
  else if (filtro1.tipoDeInmueble != filtro2.tipoDeInmueble){
    return false;
  }
  else if (filtro1.precioMin != filtro2.precioMin){
    return false;
  }
  else if (filtro1.estado != filtro2.estado){
    return false;
  }
  else if (filtro1.municipio != filtro2.municipio){
    return false;
  }
  else if (filtro1.pais != filtro2.pais){
    return false;
  }
  else if (filtro1.metrosCuadrados != filtro2.metrosCuadrados){
    return false;
  }

  return true;
}

/*
Cada vez que se actualizan los filtros, hay que vover a generar los componentes de
las páginas de inmuebles desde cero, pues hay data que depende del server 
que no se puede actualizar usando los métodos usuales de angular 2. Por
esta razón nos valemos del switch statement y el ngFor abajo.
*/

@Component({
  selector: 'my-app',
  template: `
  	<div id="arriba">

  		<filtros>
  		</filtros>

	  	<div id="cuerpo" class="w3-margin-top" [ngSwitch]="numeroDeFiltro">
        
        <ng-container *ngFor="let numero of numeroDeFiltros">
  		  	
          <grid-inmuebles *ngSwitchCase="numero" [filtrosAplicados]="filtrosAplicados" 
                           [numeroDePagina]="0" class="selector">
  		  	</grid-inmuebles>
        
        </ng-container>

		</div>
	</div>
  	`,
  styles:[`

  my-inmuebles {
  	width: 100%;
  	height: 100%;
  }

  `],
  providers: [ FiltrosService ]
})
export class AppComponent implements OnInit { 

  filtrosAplicados : Filtros;
  numeroDeFiltro : number = 1;

  // Para usar en el ngFor arriba
  numeroDeFiltros : Array<number> = [];
  constructor(@Inject(FiltrosService) private filtrosService: FiltrosService){
    for (let i=0; i<100;i++){
      this.numeroDeFiltros.push(i);
    }
  }

 ngOnInit(): void{
   this.filtrosAplicados = this.filtrosService.obtenerDatos();
 } 

 
 // Escucha a un custom event registrado en filtros.service.ts
 @HostListener('window:filtroSubmitted', ['$event'])
 checkear(): void{

   let nuevosFiltros = this.filtrosService.obtenerDatos();

   // Si no es primera vez que se cambia
   if (nuevosFiltros && this.filtrosAplicados){

       if( ! compararFiltros(this.filtrosAplicados, nuevosFiltros) ){
         this.filtrosAplicados = nuevosFiltros;
         this.numeroDeFiltro += 1;
       }

   }
   // Si es primera vez que se cambia el filtro
   else if (nuevosFiltros){
       this.filtrosAplicados = nuevosFiltros;
       this.numeroDeFiltro += 1;
   }

 }

}