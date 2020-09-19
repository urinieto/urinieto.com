---
title: El Acertijo de los Isleños de Ojos Azules
author: uri
type: post
date: 2009-11-30T03:24:24+00:00
url: /2009/11/el-acertijo-de-los-islenos-de-ojos-azules/
categories:
  - Uncategorized

---
Hace poco me contaron el mejor acertijo que haya escuchado nunca: [El Acertijo de los isleños de Ojos Azules][1]. Este acertijo usa la lógica pura de las matemáticas, el resultado es precioso y me produce un cierto gustillo cada vez que pienso en él. Ya que no he encontrado ninguna web en castellano que lo formule, lo voy a traducir (libremente) aquí.

> Una tribu peculiar vive en una isla alejada de cualquier otra civilización. La tribu consiste en 1000 personas, con distintos colores de ojos. Aún así, su religión les prohíbe saber cual es su propio color de ojos, o incluso hablar sobre ello entre ellos. Así pues, cada isleño puede (y debe) mirar el color de los ojos de todos los otros isleños, pero no hay manera de descubrir su propio color (no hay superficies reflectantes en toda la isla). Si un isleño descubre su propio color de ojos, entonces **su religión le obliga a hacer un ritual suicida al mediodía del día siguiente**, en la plaza principal del pueblecito de la tribu, para que **todos los demás lo puedan presenciar**. Todos los isleños tienen una manera de pensar extremadamente lógica, y cada uno de ellos sabe que los demás son tan lógicos y devotos como ellos (y todos saben que todos saben que cada uno es extremadamete lógico y devoto, etc).
> 
> Para los propósitos de este acertijo, &#8220;extremadamente lógico&#8221; significa que cualquier conclusión que pueda ser deducida con lógica extraída de cualquier información y/u observación disponible para un isleño, entonces ésta será sabida automáticamente por ese isleño.
> 
> De los 1000 isleños, resulta que hay **100 de ellos con los ojos azules y 900 con los ojos marrones**, aunque los isleños no son conscientes de estas estadísticas inicialmente (es obvio que cada uno de ellos solamente puede ver 999 de los 1000 isleños).
> 
> Un buen día, **un forastero con los ojos azules** visita la isla y se gana la plena confianza de la tribu.
> 
> Una tarde, se dirige a toda la tribu entera para agradecerles su hospitalidad.
> 
> No obstante, sin ser conocedor de sus curiosas costumbres religiosas, el forastero comete el grave error de mencionar su propio color de ojos, diciendo &#8220;qué inusual es ver otra persona con los ojos azules como yo en esta región del mundo!&#8221;
> 
> ¿Qué efecto -si hay alguno- tiene este &#8220;error&#8221; en los isleños?

Ahora os dejo pensar.  
Creo es un problema bastante difícil, y yo necesité varias pistas para poderlo resolver. Aún así, vale la pena el esfuerzo.

Os dejo una foto para que os entre la inspiración.

[{{< img src="/wp-content/uploads/2009/11/PuertoEscondido.jpg" alt="PuertoEscondido" title="PuertoEscondido" width="474" height="355" class="aligncenter size-full wp-image-637" >}}][2]

¿Pistas? Seguid leyendo.

Qué pasaría si hay 1 sólo hombre en la tribu, viene el forastero, y dice la misma frase: &#8220;qué inusual es ver otra persona con los ojos azules como yo en esta región del mundo!&#8221;. ¿Qué le pasaría a este hombre?

Otra pista, seguid leyendo.

¿Y qué pasaría si en lugar de 1 hombre, hubieran 2 y los dos tuvieran los ojos azules y viene el forastero y dice la misma frase?

Y ahora sí, voy a explicar la solución.

El argumento inicial de &#8220;no pasa nada&#8221;, es erróneo. La información que suelta el forastero generará un desequilibrio en la isla. 

Como he dicho en las pistas, si hay un sólo isleño (caso base), y el forastero le dice La Frase, entonces él tendrá que matarse al día siguiente al mediodía, pues es el único que puede tener los ojos azules. Si hay dos con los ojos azules, entonces, al saber los dos que el otro tiene los ojos igual que el forastero, se esperaran a que se mate el otro al día siguiente (i.e. los dos piensan &#8220;qué bien, a menos que yo tenga los ojos azules, yo no me voy a matar, pues es el otro isleño el que tiene los ojos azules igual que el forastero!&#8221;). Al ver que nadie se mata al día siguiente, y al ser personas tan lógicas, deducen que los dos deben de tener los ojos azules y se matarán al cabo de 2 días.

Si repetimos el proceso hasta 100 (por recursividad), veremos que al final se mataran todos juntos cuando hayan pasado 100 días. Todos los isleños con los ojos azules, pensarán el primer día: &#8220;qué bien, a menos que yo tenga los ojos azules, yo no me voy a matar, pues aquí hay 99 isleños con los ojos azules igual que el forastero&#8221;. Así se esperaran todos los 99 días y al ver que el día 99 no se ha matado nadie, el día 100 se suicidarán. Por otra parte los isleños de ojos marrones, pensarán: &#8220;qué bien, a menos que yo tenga los ojos azules, yo no me voy a matar, pues aquí hay 100 isleños con los ojos azules igual que el forastero&#8221;, así que se esperaran todos los 100 días y, al ver que el día 100, los 100 isleños con los ojos azules se matan, entonces los de los ojos marrones podrán seguir viviendo tranquilamente sin saber cual es el color de sus ojos.

Es básicamente un claro problema de recursividad (o inducción, pero mi condición de informático hace que me guste más usar la palabra recursividad), y creo que si me lo hubieran enseñado en la facultad me hubiera ayudado mucho a comprender cómo funciona este método de resolución de algoritmos.

Ahhh, me encantan estas mierdas&#8230;

Hurgando un poco he visto que es un acertijo de [Terence Tao][3] un jovencísimo doctor en matemáticas, Profesor de la universidad de Los Angeles.

 [1]: http://terrytao.wordpress.com/2008/02/05/the-blue-eyed-islanders-puzzle/
 [2]: /wp-content/uploads/2009/11/PuertoEscondido.jpg
 [3]: http://www.math.ucla.edu/~tao/