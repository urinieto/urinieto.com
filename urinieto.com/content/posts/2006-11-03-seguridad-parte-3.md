---
title: Seguridad, parte 3
author: uri
type: post
date: 2006-11-03T16:10:00+00:00
url: /2006/11/seguridad-parte-3/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/11/seguridad-parte-3.html
thumbnail:
  src: "https://photos1.blogger.com/blogger2/4197/4184/320/importsecurity.jpg"
  alt: Thumbnail image
categories:
  - Uncategorized

---
No hay dos sin tres.

Lo he conseguido. Funciona. Ya puedes logearte desde tu plugin para tiddlywiki a tu server de moodle. Flipa. 

[{{< img style="display:block;text-align:center;cursor:hand;margin:0 auto 10px;" src="https://photos1.blogger.com/blogger2/4197/4184/320/importsecurity.jpg" border="0" alt="" >}}][1]  
El código de sesiones y logins de moodle es enorme y bastante complejo y &#8220;spaghetti&#8221;, pero he conseguido encontrar la manera de entenderlo y usar las partes que me importaban a mi plugin.

He creado un nuevo archivo para la wiki (por si había pocos), el wssecurity.php, donde he puesto todas las funciones de seguridad del web service.

En resumen: envío el pwd en md5 y lo comparo con el de la base de datos, que ya está en md5. He usado funciones internas de moodle y funciones modificadas para mi webservice para crear la sesion e identificar si el usuario tiene permisos o no para un determinado curso.

Ahora queda pulirlo, pero el núcleo está acabado. Bona!

 [1]: https://photos1.blogger.com/blogger2/4197/4184/1600/importsecurity.jpg