import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { FiltrosService } from './filtros.service.js';

// TODO: agregar validadores de form necesarios abajo

export class Filtros {

	// Filtros usados
    operacion: string; 
    tipoDeInmueble: string;
    antiguedadMax: string;
    numeroBanyos: number;
    numeroHabitaciones: number;
    numeroEstacionamientos: number;
    precioMax: number;
}

@Component({
	selector: 'filtros',
	templateUrl: 'filtros',
	styles: []
})
export class FiltrosComponent implements OnInit {
    public myForm: FormGroup; // our model driven form

    constructor(private _fb: FormBuilder,
    			private filtrosService : FiltrosService) { } // form builder simplify form initialization

    ngOnInit() {
        
        // Se crean los inputs del filtro y se conectan con sus inputs en el template por su nombre
	    this.myForm = new FormGroup({
	        operacion: new FormControl('', []),
	        tipoDeInmueble: new FormControl('', []),
	        antiguedadMax: new FormControl('', []),
	        numeroBanyos: new FormControl('', []),
	        numeroHabitaciones: new FormControl('', []),
	        numeroEstacionamientos: new FormControl('', []),
	        precioMax: new FormControl('', [])
	    });

    }

    save(model: Filtros, isValid: boolean) {
        // TODO: determinar si el form es valido antes de compartir
        this.filtrosService.compartirDatos(model);
    }
}