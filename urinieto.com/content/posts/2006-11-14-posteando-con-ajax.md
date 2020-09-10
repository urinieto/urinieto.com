---
title: POSTeando con AJAX
author: uri
type: post
date: 2006-11-14T11:42:00+00:00
url: /2006/11/posteando-con-ajax/
blogger_blog:
  - enochrooted.blogspot.com
blogger_permalink:
  - /2006/11/posteando-con-ajax.html
categories:
  - ajax
  - exportdfwiki
  - pfc

---
He implementado las funciones del objeto XMLHttpRequest en nuestro Export plugin des de &#8220;casi&#8221; cero porque:

(1) Tenemos que pasar la información a exportar por <span style="font-weight:bold;">POST</span> ya que por GET no cabría (los tiddlers pueden ser enormes).  
(2) La información irá a una URL <span style="font-weight:bold;">externa</span>.  
(<span style="font-weight:bold;">EDIT 15-11-06</span>: ATENCIÓN, trabajar con una URL externa en AJAX sólo es posible si trabajamos con una página que esté guardada <span style="font-weight:bold;">localmente</span>. Si metemos la página en un server tendremos problemas de seguridad!).  
(3) El Exportplugin original no tiene funciones AJAX implementadas.  
(4) Así aprovechamos para aprender un poquito más de esta cosa tan &#8220;virguera&#8221; que es el AJAX ;)  

Voy a explicar un poco cómo me lo he montado y los problemas que he tenido.

Empecemos con las implementaciones que hicimos para wikibook, con el ya típico:

> function GetXmlHttpObject()  
> {  
> var objXMLHttp=null;  
> if (window.XMLHttpRequest)  
> {  
> objXMLHttp=new XMLHttpRequest();  
> }  
> else if (window.ActiveXObject)  
> {  
> objXMLHttp=new ActiveXObject(&#8220;Microsoft.XMLHTTP&#8221;);  
> }  
> return objXMLHttp;  
> }

Ahora ya podremos crear el objecto XMLHttpRequest sin problemas generados por nuestro querido amigo El Micro$oft.

Pero lo queremos pasar por POST. Y además hacia una URL <span style="font-weight:bold;">externa</span>. Allá vamos.

Creamos nuestro objeto XMLHttpRequest y le asociamos la función que queremos que haga. En nuestro caso, la función la llamamos stateExportToMoodle:

> xmlHttp=GetXmlHttpObject();  
> xmlHttp.onreadystatechange=stateExportToMoodle;

Vayamos a tratar lo del tema de la URL externa. Deberemos tener en cuenta a los usuarios preocupados por su seguridad, privacidad y, en general, libertad (usuarios de navegadores tipo netscape), ya que a éstos navegadores se les tiene que decir, explícitamente, que el objeto XMLHttpRequest accederá de manera excepcional a una URL externa. Para el resto de usuarios, los del IE, no hace falta.

> if (typeof(netscape)!=&#8221;undefined&#8221;) {  
> try { netscape.security.PrivilegeManager.enablePrivilege(&#8220;UniversalBrowserRead&#8221;);}  
> catch (e) { alert(e.description?e.description:e.toString()); }  
> }

Si el usuario no tiene permisos para dejar que el objecto XMLHttpRequest acceda a página externas saltará un bonito y toca huevos alert.

Ahora el tema del POST. Abriremos la conexión con nuestra url con el método POST:

> xmlHttp.open(&#8220;POST&#8221;,url);

Y ahora viene la parte importante: debemos definir el Content type de nuestra cabecera del XMLHttpRequest, ya que sinó, la url que lo reciba no sabrá cómo tratarlo y no sabrá que contendrá datos en POST. Así que necesitamos lo siguiente:  


> xmlHttp.setRequestHeader(&#8216;Content-Type&#8217;, &#8216;application/x-www-form-urlencoded&#8217;);</p>
Ahora tan sólo queda enviar el objeto. Supongamos que queremos enviar el objeto con dos parámetros post: sel y wikiname. La cosa sería así:  


> xmlHttp.send(&#8220;sel=valorsel&wikiname=valorwikiname&#8221;);</p>
Y ya está. Lo que hagáis con la función stateExportToMoodle ya será cosa vuestra. Yo, de momento, sólo la he usado para comprobar que, efectivamente, todo funciona perfectamente.

Los principales problemas que he tenido han sido:  
- No tenía permisos para llamar a una URL externa. No sabía que debía solicitarlos.  
- Añadir el campo de la cabecera del XMLHttpRequest para que la página de destino supiera reconocer los datos del POST.

Espero que os haya sido útil.  
AJAX power!