import { Component, OnInit, Inject } from '@angular/core';

import { FiltrosService } from './VInmuebles/filtros_busqueda/filtros.service.js';
import { GridComponent } from './VInmuebles/grid_inmuebles/grid.component.js';
import { FiltrosComponent, Filtros } from './VInmuebles/filtros_busqueda/filtros.component.js';

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

       if(this.filtrosAplicados.tipoDeInmueble != nuevosFiltros.tipoDeInmueble){
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