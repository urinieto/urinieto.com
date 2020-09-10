---
title: Problemas importando
author: uri
type: post
date: 2006-11-11T15:47:00+00:00
url: /2006/11/problemas-importando/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/11/problemas-importando.html
categories:
  - exportdfwiki
  - importdfwiki
  - pfc

---
Los tags en html no le gustan a nuestro querido plugin. Se los come. En un principio pensamos que era problema del parser de Didac, pero no es así. El parser saca los tags perfectamente, pero, una vez en el plugin &#8220;desaparecen&#8221;. Porque tienen que ser tratados.

Alex ha estado mirando info y ha encontrado el núcleo del problema (con su solución). Copio y pego:

> El pluglin funciona de puta madre, lo que pasa eske peta porke lo ke nos parsea el dídac lo metemos en un string que luego la tiddly reconoce como html (de ahí los saca la funcion readItemsFromHTML), y en html los carácteres especiales como &#8220;<&#8221; petan, se han de codificar previamente de otra forma.
> 
> Ya verás, si en vez de tener en la página el tag![]() pones va a petar igual, por eso petan todos los tags de la forma .
> 
> En cambio, si importas una página que haya sido editada con el &#8220;html editor&#8221; y no con el &#8220;dfwiki editor&#8221;, como en la base de datos de moodle está guardado como html puro y duro, los caracteres especiales ya estan substituidos (x ejemplo el &#8220;&#8221; como &#8220;&gt&#8221;) y la importación furula bien. Tengo una foto que lo demuestra

Así que volvemos a pasar el problema a Didac y seguimos con el export. De momento éste ha sido modificidao de tal manera que hace petar toda la tiddly. Pero nada, esto se arregla en breve!

Espero.