---
title: HTML y Media wiki terminado, sincronismo avanzando
author: uri
type: post
date: 2006-11-28T14:48:00+00:00
url: /2006/11/html-y-media-wiki-terminado-sincronismo-avanzando/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/11/html-y-media-wiki-terminado-sincronismo.html
categories:
  - exportdfwiki
  - importdfwiki
  - pfc
  - synchronize

---
Nuestros plugins de importar y exportar ya pueden hacerlo usando el formato HTML o el parser de Media Wiki si se desea.

Han habido [problemas][1] con el tema, y ha sido Alex el que se ha peleado con todo ello, pero al final se ha conseguido.

Mientras tanto yo me he enfrentado con <span style="font-weight:bold;">El Sincronismo</span> (Nota Mental: No abusar de tanta negrita y Mayúsculas).

He sufrido intentando hacer compatibles los dos plugins de importación y exportación con el nuevo plugin de sincronismo. Pero finalmente he conseguido hacerlo usando los propios campos del DOM que usan el import y el export.

De momento, cuando sincronizas un tiddler, comprueba que éste se encuentre en el servidor de Moodle. Es un gran paso, puesto que he usado las funciones de export sin apenas modificarlo.

¿Y qué queda por hacer?

Mucho: 

  * Si no encuentra la wiki en el Server de Moodle, mostrar un mensaje al usuario. (Creo que es una buena idea que, para sincronizar algo que aún no se encuentra en el Moodle, primero lo exporte con el plugin adecuado y luego ya sincronizará. Así que sería buena idea mostrar un mensaje informándole de ello).
  * Cómo guardar la información del usuario y su passwd. (Como para sincronizar un tiddler solamente tenemos que apretar un botón, en algún lugar tendrá que quedar guardado el user y el pwd del Moodle Server. Algo como se hace en tiddlyspot sería bonito).
  * Una vez hallada la wiki en el Moodle Server, llamar a una nueva función en ajax y del webservice que nos diga cual ha sido la última vez que se ha modificado.
  * Si esta fecha es anterior, realizar un export.
  * Si esta fecha es posterior, realizar un import.
  * Modificar la pequeña interfície del plugin para que no sólo nos muestre qué tiddlers se han sincronizado sinó que nos diga la última vez.
  * Muchas otras cosas que seguro me estoy olvidando.
</ul> 

En fín, mañana reunión, nos repartiremos el trabajo con Alex.  
Yo ahora voy a preparar la sesión de AJAX de éste viernes.

 [1]: http://vdemarvvv.blogspot.com/2006/11/novedades-importexport.html