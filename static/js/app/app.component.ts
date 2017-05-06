import { Component, OnInit, Inject } from '@angular/core';

import { FiltrosService } from './VInmuebles/filtros_busqueda/filtros.service.js';
import { GridComponent } from './VInmuebles/grid_inmuebles/grid.component.js';
import { FiltrosComponent, Filtros } from './VInmuebles/filtros_busqueda/filtros.component.js';

//TODO: cuando el contador de filtros aplicados llegue a 100 hay que refrescar la página


function compararFiltros(filtro1: Filtros, filtro2: Filtros): boolean{

  alert(filtro1);
  alert(filtro2);

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

  return true;
}

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
  numeroDeFiltros : Array<number> = [];
  constructor(@Inject(FiltrosService) private filtrosService: FiltrosService){
    for (let i=0; i<100;i++){
      this.numeroDeFiltros.push(i);
    }
  }

 ngOnInit(): void{
   this.filtrosAplicados = this.filtrosService.obtenerDatos();
 } 

 ngDoCheck(): void{
   let nuevosFiltros = this.filtrosService.obtenerDatos();
   if (nuevosFiltros && this.filtrosAplicados){

       if( ! compararFiltros(this.filtrosAplicados, nuevosFiltros) ){
         this.filtrosAplicados = nuevosFiltros;
         this.numeroDeFiltro += 1;
       }

   }
   else if (nuevosFiltros){
       this.filtrosAplicados = nuevosFiltros;
       this.numeroDeFiltro += 1;
   }

 }

}