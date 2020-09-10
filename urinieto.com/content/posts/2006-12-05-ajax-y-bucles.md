---
title: AJAX y bucles
author: uri
type: post
date: 2006-12-05T12:39:00+00:00
url: /2006/12/ajax-y-bucles/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/12/ajax-y-bucles.html
categories:
  - ajax
  - pfc

---
Llamar a una función que cree un objeto XMLHttpRequest dentro de un bucle es totalmente impensable. Ejemplifico:

> funcion impensable(){  
> var i;  
> for(i=0; i<10; i++){  
> crearXMLHttpRequest();  
> }  
> }

Ok, si sólo queremos crear un XMLHttpRequest sin utilizarlo, pues ningún problema. Pero obviamente, no crearemos un objeto para no usarlo (exceptuando casos puntuales de exceso de alcohol y/o otras substancias).

El problema está en que, de ésta manera, la velocidad de recorrido de éste bucle es mucho más rápida que la velocidad de envío, recibo y tratado del XMLHttpRequest que se envía.

Así lo que tenemos aquí es que enviamos 10 XMLHttpRequests y sólo nos da tiempo de tratar el último <span style="font-weight:bold;">puesto que hemos usado la misma función las 10 veces</span>.

La solución es hacer una función distinta para cada llamada. Pero esto puede hacerse intratable en el caso que no queramos tratar 10 funciones si no un número variable de ellas.

Así pues, lo que he hecho, es añadir un parámetro a la función y llamar a la función creadora con un parámetro. Y cuando tratemos el recibo del XMLHttpRequest, llamaremos otra vez a la función pero con ése valor (i) incrementado.

Algo así:

> funcion impensable(i){  
> var i;  
> for(i=0; i<10; i++){  
> crearXMLHttpRequest(i);  
> }  
> }

Y en la función que trate el XMLHttpRequest:

> funcion tratarXMLHttpRequest(){  
> if (xmlHttp.readyState == 4){  
> var i = xmlHttp.responseXML.donde-esté-la-i;  
> impensable(i+1);  
> }  
> }

Creo que esto me ahorrará largos dolores de cabeza.