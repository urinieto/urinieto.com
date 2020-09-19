---
title: Especificación del Wikibook
author: uri
type: post
date: 2006-10-16T10:07:00+00:00
url: /2006/10/especificacion-del-wikibook/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/10/especificacin-del-wikibook.html
categories:
  - pfc
  - wikibook

---
He hecho una primera aproximación al diseño de nuestro Wikibook. Aquí adjunto el boceto:

[{{< img style="display:block;text-align:center;cursor:hand;margin:0 auto 10px;" src="http://photos1.blogger.com/blogger2/4197/4184/320/wikibook-specification.jpg" border="0" alt="" >}}][1]  
He dudado en implementar la base de datos tal y como me han enseñado en la facultad o hacerlo tal y como pone en la documentación de Moodle. La primera opción era crear 3 tablas:

-Wikibooks(<span style="font-weight:bold;">id</span>)  
-WikibookChapters(<span style="font-weight:bold;">id, <span style="font-style:italic;">wikibookid</span></span>)  
-WikibookPages(<span style="font-weight:bold;">id, <span style="font-style:italic;">wikibookid, wikibookchapterid</span></span>)

Los campos en negrita son las claves primarias.  
Los campos en cursiva son las claves foráneas.

Ésta implementación está muy bien, pero según Moodle y su filosofía de obviar las claves foráneas (limitación impuesta por versiones anteriores de mySQL), no se puede implementar así.

Así pues, haré caso a Moodle y la implementación final que he decidio es básicamente la misma pero usando un id único para cada tabla, y que éste sea la única clave primaria. Quedando así:

-Wikibooks(<span style="font-weight:bold;">id</span>)  
-WikibookChapters(<span style="font-weight:bold;">id</span>, wikibookid)  
-WikibookPages(<span style="font-weight:bold;">id</span>, wikibookid, wikibookchapterid)

Los campos en negrita son las claves primarias.  
No hay claves foráneas explícitas. Las joins se harán en php y no en sql.

Repito que es una primera aproximación, ahora me dispongo a hacer las primeras pruebas con ella.

 [1]: http://photos1.blogger.com/blogger2/4197/4184/1600/wikibook-specification.jpg