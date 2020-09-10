---
title: Limitaciones de AJAX
author: uri
type: post
date: 2006-11-15T11:56:00+00:00
url: /2006/11/limitaciones-de-ajax/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/11/limitaciones-de-ajax.html
categories:
  - ajax
  - exportdfwiki
  - pfc

---
Todo lo que escribí ayer en el [post sobre AJAX][1] SÓLO funciona si trabajamos <span style="font-weight:bold;">localmente</span>.

AJAX no puede trabajar con servidores externos a menos que estemos trabajando de manera local. Ludo ha sido quien me ha advertido sobre ésto. Gracias!

Así que para exportar contenidos de una tiddly ésta tendrá que <span style="font-weight:bold;">descargarse</span> primero y luego exportar los datos al servidor local.

Mientrastanto, ya he acabo la parte de AJAX y de la Tiddly de nuestro ExportPlugin. Ahora queda la parte de PHP dentro del server de Moodle.

 [1]: http://enochrooted.blogspot.com/2006/11/posteando-con-ajax.html