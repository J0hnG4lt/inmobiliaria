import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent }   from './app.component.js';
import { GridComponent } from './VInmuebles/grid_inmuebles/grid.component.js';
import { InmuebleComponent } from './VInmuebles/grid_inmuebles/inmueble_resumen/inmueble.component.js';
import { HttpModule } from '@angular/http';

@NgModule({
  imports:      [ BrowserModule,HttpModule ],
  declarations: [ AppComponent, GridComponent, InmuebleComponent],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }

