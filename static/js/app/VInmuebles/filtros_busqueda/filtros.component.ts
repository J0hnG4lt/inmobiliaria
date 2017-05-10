import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { FiltrosService } from './filtros.service.js';

// TODO: agregar validadores de form necesarios abajo



function construirPaises(data:any){
    let paises : string[] = [];
    for(var objeto of data){
        paises.push(objeto.fields.nombrePais);
        
    }
    return paises;
}

function construirEstados(data:any){
    let estados : string[] = [];
    for(var objeto of data){
        estados.push(objeto);
    }
    return estados;
}

function construirMunicipios(data:any){
    let municipios : string[] = [];
    for(var objeto of data){
        municipios.push(objeto);
    }
    return municipios;
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
    public estados: string[];
    public municipios: string[];
    //public paisSeleccionado: string;

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

    cargarEstados(pais : string){
            this.filtrosService.cargarEstados(pais).subscribe(data => {
                this.estados = construirEstados(data);
            })
            //this.paisSeleccionado = pais;
    }

    cargarMunicipios(pais : string, estado : string){
            this.filtrosService.cargarMunicipios(pais,estado).subscribe(data => {
                this.municipios = construirMunicipios(data);
            })
    }

}