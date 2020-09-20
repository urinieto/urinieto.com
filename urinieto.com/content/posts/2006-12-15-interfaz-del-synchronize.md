---
title: Interfaz del Synchronize
author: uri
type: post
date: 2006-12-15T12:17:00+00:00
url: /2006/12/interfaz-del-synchronize/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/12/interfaz-del-synchronize.html
thumbnail:
  src: "http://bp3.blogger.com/_WEHvyZj_jiU/RYKU5m9tgZI/AAAAAAAAAAY/nPsg3Ksfn3k/s320/syncPanel.jpg"
  alt: Thumbnail image
categories:
  - pfc
  - synchronize

---
Me he estado peleando con la interfaz del Synchronize, muy parecida a la del PluginsManager. He tratado de buscar una manera para crear un campo que nos diga cuando ha sido la última vez que se ha sincronizado. Y he encontrado una, pero no es correcta, puesto que, al no guardar la información en el tiddler de manera física, al recargar la página se pierde. 

Después de varios días, he llegado a la conclusión que para poderlo hacer, es necesario modificar la estructura interna de un tiddler añadiéndole el campo &#8220;sync&#8221;, pero esto conllevaría a modificar el diseño interno de la Tiddlywiki y esto es algo que no creo oportuno hacer.

Así que la interfaz quedará reducida y sólo aparecerán los tiddlers que se han sincronizado. Además, podremos seleccionarlos y quitarlos de la sincronización si así lo deseamos. O incluso borrarlos.

Así queda la interfaz final: 

[{{< img style="display:block;text-align:center;cursor:hand;margin:0 auto 10px;" src="http://bp3.blogger.com/_WEHvyZj_jiU/RYKU5m9tgZI/AAAAAAAAAAY/nPsg3Ksfn3k/s320/syncPanel.jpg" border="0" >}}][1]  
Por cierto, ya he enviado el webservice a Ludo. Cuando lo haya colgado en Crom subiré los tres plugins a la web de [TiddlySpot][2].

Seguimos documentando.

 [1]: http://bp3.blogger.com/_WEHvyZj_jiU/RYKU5m9tgZI/AAAAAAAAAAY/nPsg3Ksfn3k/s1600-h/syncPanel.jpg
 [2]: http://moodle.tiddlyspot.com