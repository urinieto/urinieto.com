---
title: Primera beta del Synchronize
author: uri
type: post
date: 2006-12-09T12:41:00+00:00
url: /2006/12/primera-beta-del-synchronize/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/12/primera-beta-del-synchronize.html
categories:
  - pfc
  - synchronize

---
Finalmente, ya tenemos una primera versión funcional del plugin de sincronismo. La cosa ya funciona casi casi casi. Queda implementar una función &#8220;casi&#8221; implementada para chequear los tiempos de modificación. Después de eso será el plugin funcionará al 100% (sin contar bugs, claro).

Lo siguiente que queda es: 

  * Queda implementar bien la interfaz del sincronismo.
  * Queda el problema de los grupos y parsers (ouuff)
  * Queda abrir los tiddlers de Import, Sync, i Export cada vez que se aprieta el botón de sincronizar. Si los tiddlers no están abiertos no funciona (esto es porque el javascript necesita los tags de html que definen dichos tiddlers).
  * Documentarlo todo.

Tela con lo de importar, el código que he reutilizado del import plugin original para poder sincronizar estaba totalmente ofuscado y en ocasiones he visto muertos en forma de código javascript.

Pero ya está. Es nuestro.