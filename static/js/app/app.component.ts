import { Component } from '@angular/core';


@Component({
  selector: 'my-app',
  template: '<my-inmuebles class="selector"></my-inmuebles>',
  styles:[`

  my-inmuebles {
  	width: 100%;
  	height: 100%;
  }

  `]
})
export class AppComponent { 
  
}