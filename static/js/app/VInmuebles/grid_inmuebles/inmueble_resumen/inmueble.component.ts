import { Component, OnInit, Input } from '@angular/core';



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
  urlImagenPrincipal : string;
  urlImagenesSecundarias : string[];
}


@Component({
  selector: 'my-inmueble',
  template: `
           <div class="card">
           <div class="imagen">
            <img src="{{ inmuebleActual.urlImagenPrincipal }}" alt="Avatar" style="width:100%">
            </div>
            <div class="container">
              <h4><b> BS. {{ inmuebleActual.precio }} </b></h4> 
              <p>{{ inmuebleActual.descripcion }}</p> 
            </div>
          </div>
  	`,
  styles:[`
      .card {

          /* Add shadows to create the "card" effect */
          box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
          transition: 0.3s;
          border-radius: 5px; /* 5px rounded corners */

      }

      /* On mouse-over, add a deeper shadow */
      .card:hover {
          box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
      }

      /* Add some padding inside the card container */
      .container {
          padding: 2px 16px;
          height:50%;
          width:100%;
          display: block;
          position: relative;
          overflow: hidden;
      }
      .imagen {
          height:50%;
          width:100%;
      }

      /* Add rounded corners to the top left and the top right corner of the image */
      img {
          border-radius: 5px 5px 0 0;
          position: inline;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
      }

  `]
})
export class InmuebleComponent implements OnInit { 
	
  @Input() inmuebleActual : Inmueble;

	constructor(){
	}

	ngOnInit(): void {
	}

}