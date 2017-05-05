import { Component } from '@angular/core';

import { FiltrosService } from './VInmuebles/filtros_busqueda/filtros.service.js';
import { GridComponent } from './VInmuebles/grid_inmuebles/grid.component.js';
import { FiltrosComponent } from './VInmuebles/filtros_busqueda/filtros.component.js';

@Component({
  selector: 'my-app',
  template: `
  	<div id="arriba">

  		<filtros>
  		</filtros>

	  	<div id="cuerpo" class="w3-margin-top">

		  	<grid-inmuebles [numeroDePagina]="0" class="selector">
		  	</grid-inmuebles>
		  	
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
export class AppComponent { 
  
}