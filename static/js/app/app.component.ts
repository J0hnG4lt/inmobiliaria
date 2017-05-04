import { Component } from '@angular/core';


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

  `]
})
export class AppComponent { 
  
}