---
title: Compile and use PortAudio on OSX 10.7 (Lion)
author: uri
type: post
date: 2011-11-10T21:37:32+00:00
url: /2011/11/compile-and-use-portaudio-on-osx-10-7-lion/
categories:
  - programming
tags:
  - programming

---
**UPDATE**: Version [v19_20111121][1] doesn&#8217;t compile on my Lion, but version [v19_20110326][2] does. I&#8217;ve updated this document accordingly.

**UPDATE**: Apparently, this also works on Snow Leopard. Not only that, but it might be the only way to use it under Snow Leopard.

It is frustrating to download the latest stable version of [PortAudio][3], try to compile it on the new version of Mac OSX 10.7 (Lion), and get a bunch of errors.

However, for some reason, the [previous stable release][2] does work on 10.7.

Here the instructions (nothing fancy, just regular UNIX commands to compile and install):

  * Download the [source file][2]
  * Go to your directory and untar:  
    **`$> tar zxvf pa_stable_v19_20110326.tgz`**
  * Configure:  
    **`$> cd portaudio`  
    `$> ./configure`**
  * Compile:  
    **`$> make`**
  * Install:  
    **`$> sudo make install`**

Now you should be able to go to the examples directory and compile and run the examples.

You must change the commas in `#include "portaudio.h"` for brackets: `#include &#060;portaudio.h&#062;`, so that the linker will look for the portaudio library inside your library path. To compile, for example **paex_sine.c**, you should type (inside the exmaples directory):

`$> gcc -o paex_sine paex_sine.c -lportaudio`

Then, you can just type `./paex_sine` to listen to a 5 seconds sinewave.

If you are one of those who don&#8217;t like to install new libraries in your system path, you can always link with your libraries locally. In this case, you can leave the include with the commas. From the examples directory, you could compile some of these examples like this:

`$> gcc -o paex_sine paex_sine.c -I../include/ -L../lib/.libs/ -lportaudio`

In this case you will also need your DYLD\_LIBRARY\_PATH variable to point to your portaudio lib directory. Like this (it&#8217;s better to put the full path, I&#8217;m just putting the local path here as an example):

`$> export DYLD_LIBRARY_PATH=../libs/.libs/`

Now you can run it (from the examples directory): `./paex_sine`

You&#8217;re all set.  
Have fun coding with PortAudio!

 [1]: https://www.portaudio.com/archives/pa_stable_v19_20111121.tgz
 [2]: https://www.portaudio.com/archives/pa_stable_v19_20110326.tgz
 [3]: https://www.portaudio.com/