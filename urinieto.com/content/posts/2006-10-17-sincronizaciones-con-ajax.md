---
title: Sincronizaciones con AJAX
author: uri
type: post
date: 2006-10-17T18:21:00+00:00
url: /2006/10/sincronizaciones-con-ajax/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/10/sincronizaciones-con-ajax.html
categories:
  - ajax
  - pfc
  - wikibook

---
He solucionado un pequeño problema que teníamos cuando llamábamos a dos funciones que trabajan con un objeto XMLHttpRequest cada una.

La cosa es que teníamos un par de funciones que se llaman cuando se hace un click en un botón. De la siguiente manera:

código del botón:

<span style="font-weight:bold;"></span>

código javascript:

<span style="font-weight:bold;">function saveAndShowChapters() {<br /> save_wikibook_chapter(instancia, valor, curso);<br /> show_chapters(insancia, curso);<br />}</span>

Con ésto consigo que, apretando dicho botón, se guarde el capítulo que quiera en la base de datos e inmediatamente despues se actualice la lista de capítulos por pantalla.

Parece precioso y perfecto ¿no?

Pues parece que no. Al objecto XMLHttpRequest no le gustaba tanto mareo junto. (Os recuerdo que éstas dos funciones envian y reciben información del servidor con el XMLHttpRequest, y que se llaman una despues de la otra).

La solución de poner un wait() entre las llamadas no entiendo porqué no parecía funcionar.

Así que he optado por poner la segunda llamada en el apartado donde se decide que la función del XMLHttpRequest ha finalizado. De la siguiente manera:

<span style="font-weight:bold;"><br />function stateSaveWikibookChapterChanged() { <br /> if (xmlHttp.readyState==4 || xmlHttp.readyState==&#8221;complete&#8221;) { <br /> document.getElementById(&#8220;saveChapter&#8221;).innerHTML=xmlHttp.responseText;<br /> show_chapters(instancia, curso);<br /> } <br />}</span>

Entonces, en la función saveAndShowChapters() sólo tenemos que llamar a una función:

<span style="font-weight:bold;">function saveAndShowChapters() {<br /> save_wikibook_chapter(instancia, valor, curso);<br /> //show_chapters(insancia, curso);<br />}</span>

Y funciona de maravilla.

Pero, ¿y si alguna vez quiero salvar un capíulo sin mostrarlo? Pues puedo pasarle un parámetro a la funcion save\_wikibook\_chapter y listos. Cap problema.

AJAX power!