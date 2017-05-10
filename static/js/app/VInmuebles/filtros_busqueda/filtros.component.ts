import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { FiltrosService } from './filtros.service.js';

// TODO: agregar validadores de form necesarios abajo
// TODO: agregar la lista de opciones para los estados y municipios


function construirPaises(data:any){
    let paises : string[] = [];
    for(var objeto of data){
        paises.push(objeto.fields.nombrePais);
        
    }
    return paises;
}

export class Filtros {

	// Filtros usados
    operacion: string; 
    tipoDeInmueble: string;
    antiguedadMax: string;
    numeroBanyos: number;
    numeroHabitaciones: number;
    numeroEstacionamientos: number;
    metrosCuadradosMin: number;
    metrosCuadradosMax: number;
    precioMax: number;
    precioMin: number;
    pais: string;
    estado: string;
    municipio: string;
}

@Component({
	selector: 'filtros',
	templateUrl: 'filtros',
	styles: []
})
export class FiltrosComponent implements OnInit {
    public myForm: FormGroup; // our model driven form
    public paises: string[]; // TODO: crear tipo

    constructor(private _fb: FormBuilder,
    			private filtrosService : FiltrosService) { 

            this.filtrosService.cargarPaises().subscribe(data => {
                  this.paises = construirPaises(data);
            })

    }

    ngOnInit() {
        
        // Se crean los inputs del filtro y se conectan con sus inputs en el template por su nombre
	    this.myForm = new FormGroup({
	        operacion: new FormControl('', []),
	        tipoDeInmueble: new FormControl('', []),
	        antiguedadMax: new FormControl('', []),
	        numeroBanyos: new FormControl('', []),
	        numeroHabitaciones: new FormControl('', []),
	        numeroEstacionamientos: new FormControl('', []),
	        precioMax: new FormControl('', []),
            precioMin: new FormControl('', []),
            metrosCuadradosMin: new FormControl('', []),
            metrosCuadradosMax: new FormControl('', []),
            pais: new FormControl('', []),
            estado: new FormControl('', []),
            municipio: new FormControl('', [])
	    });

    }

    save(model: Filtros, isValid: boolean) {
        // TODO: determinar si el form es valido antes de compartir
        this.filtrosService.compartirDatos(model);
    }
}