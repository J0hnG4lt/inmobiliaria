import { Injectable } from '@angular/core';
import { Inmueble } from './inmueble_resumen/inmueble.component.js';
import { INMUEBLES } from './mock_inmuebles.js';

@Injectable()
export class InmuebleService {

	getInmuebles() : Promise<Inmueble[]> {
  		return Promise.resolve(INMUEBLES);
	}
	
}