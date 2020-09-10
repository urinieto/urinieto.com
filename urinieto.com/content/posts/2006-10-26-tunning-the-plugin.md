---
title: Tunning the Plugin
author: uri
type: post
date: 2006-10-26T11:12:00+00:00
url: /2006/10/tunning-the-plugin/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/10/tunning-plugin.html
categories:
  - importdfwiki
  - pfc
  - tiddlywiki

---
Mañana publicamos una primera demo de nuestro ImportDFwikiPlugin para tiddlywiki. 

He arreglado un bug que sucedía cuando se trataba de importar un tiddler ya existente y he añadido el código necesario para empezar a trabajar con usuarios y pwd de moodle.

Para enviar el pwd de manera segura usaré un algoritmo MD5 en Javascript para cifrar y enviar junto con la llave aleatoria generada. En el server cifraré el pwd de la base de datos con la misma llave y lo compararé con lo recibido. Y ale, ya tengo una seguridad alucinante.

Pero esto aún no estará disponible mañana.

Mañana se podran importar wikis de un moodle **CON EL WEBSERVICE INSTALADO** y que éstas (las wikis) estén publicada en un curso con permiso a usuarios &#8220;guest&#8221;.

No, si al final me acabaré gustando mucho ésta cosa llamada tiddly wiki&#8230;