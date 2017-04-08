import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent }   from './app.component.js';
import { InmuebleComponent } from './inmueble.component.js'

@NgModule({
  imports:      [ BrowserModule ],
  declarations: [ AppComponent, InmuebleComponent],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }

