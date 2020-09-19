---
title: ImportDFWiki working!
author: uri
type: post
date: 2006-10-23T09:24:00+00:00
url: /2006/10/importdfwiki-working/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/10/funciona.html
categories:
  - importdfwiki
  - pfc
  - tiddlywiki

---
Parece que sí. Lo hemos conseguido. Hemos hecho un pluggin para tiddlywiki que se conecta con el webservice de la nwiki de moodle e importa las páginas deseadas. 

Y como me gustan tanto los pantallazos, aquí tenéis:

[{{< img style="display:block;text-align:center;cursor:hand;margin:0 auto 10px;" src="http://photos1.blogger.com/blogger2/4197/4184/320/tiddlyplugin.jpg" border="0" alt="" >}}][1]

Fué el sábado, cuando vino Alex a casa, cuando conseguimos entender a grandes rasgos el código del plugin ImportTiddlers de tiddlywiki y modificarlo para importar nuestras queridas wikis.

Mi problema con el ExportTiddlers parece ser un bug del mismo plugin. Y es que, si seleccionas todos los tiddlers con el botón &#8220;all&#8221; y luego los exportas se cuelga el plugin, y en cambio, si los seleccionas a mano (también todos, o sólo unos cuantos, o sólo uno) pues funciona perfectamente, tanto en Linux como en Windows como en Mac (aunque en Windows visiblemente más rápido). Cosas esotéricas, sí.

TODO:  
- Seguridad del webservice  
- Editar las macros del plugin para permitir poder tener el importdfwiki y el importtiddlers en una misma tiddlywiki  
- Mejorar interfaz en Javascript  
- Compatibilidad de la sintaxis tiddlywiki con nwiki

Bona feina!

 [1]: http://photos1.blogger.com/blogger2/4197/4184/1600/tiddlyplugin.jpg