import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';


export interface Filtros {
    operacion: string; // required with minimum 5 chracters
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
    public submitted: boolean; // keep track on whether form is submitted
    public events: any[] = []; // use later to display form changes

    constructor(private _fb: FormBuilder) { } // form builder simplify form initialization

    ngOnInit() {
        // we will initialize our form model here

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
        this.submitted = true; // set form submit to true

        // check if model is valid
        // if valid, call API to save customer
        console.log(model, isValid);
    }
}