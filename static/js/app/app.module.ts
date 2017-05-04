import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent }   from './app.component.js';
import { GridComponent } from './VInmuebles/grid_inmuebles/grid.component.js';
import { InmuebleComponent } from './VInmuebles/grid_inmuebles/inmueble_resumen/inmueble.component.js';
import { FiltrosComponent } from './VInmuebles/filtros_busqueda/filtros.component.js';
import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


@NgModule({
  imports:      [ BrowserModule,
  				  HttpModule,
  				  FormsModule,
  				  ReactiveFormsModule ],
  declarations: [ AppComponent, 
  				  GridComponent, 
  				  InmuebleComponent,
  				  FiltrosComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }

