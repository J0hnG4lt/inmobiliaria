# Inmobiliaria

Este proyecto usa de manera conjunta el framework de desarrollo web Django y 
Angularjs en su versión dos.

Instalación de Desarrollo
-------------------------

Luego de clonar el repositorio es necesario ejecutar la siguiente orden
en el directorio raíz:
```bash
sudo pip install -r requirements.txt
```

Posteriormente, es necesario ejecutar lo siguiente:
```bash
cd static/js
sudp npm install
```

Dependiendo de la versión de typescript instalada se encontrarán
incovenientes distintos. Para determinar la versión de *tsc* que
fue instalada, es necesario ejecutar `tsc -v`.

Si se tiene la versión 2.2.2, se debería poder ejecutar `tsc` sin
problemas en el directorio `static/js`.

Si se tiene la versión 1.8.0, se debe ejecutar lo siguiente:
```bash
sudo npm install -g typings
typings install --global dt~es6-shim
```

Luego de esto es necesario abrir el archivo de configuración
de compilación *tsconfig.json* y eliminar el elemento `"lib": [ "es2015", "dom" ],`.

Finalmente, se debe ejecutar `tsc`. El output de esta orden debería ser así:

```bash
app/app.module.ts(3,32): error TS2307: Cannot find module './app.component.js'.
main.ts(2,27): error TS2307: Cannot find module './app/app.module.js'.
```

Luego de esto, sólo hay que recargar la página.
