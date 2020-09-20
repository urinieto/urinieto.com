---
title: Audio Resampling in Python
author: uri
type: post
date: 2011-05-10T22:00:33+00:00
url: /2011/05/audio-resampling-in-python/
thumbnail:
  src: "/wp-content/uploads/2011/05/python-icon-150x150.png"
  alt: Thumbnail image
categories:
  - music
  - software

---
Here I present a little Python script I wrote to resample 48kHz audio files to 44.1kHz (16 bits).

[{{< img src="/wp-content/uploads/2011/05/python-icon-150x150.png" alt="" title="python-icon" width="150" height="150" class="aligncenter size-thumbnail wp-image-1163" >}}][1]

The script uses a [Kaiser Window][2] instead of a [Rectangular Window][3] to better filter out the [aliasing][4]. Here it is the Kaiser Windowed Impulse Response used in this script:

[{{< img src="/wp-content/uploads/2011/05/KaiserIR-500x377.png" alt="" title="KaiserIR" width="500" height="377" class="aligncenter size-medium wp-image-1170" >}}][5]

As you can see, the lower ribs are smoothed out compared to just a impulse response (rectangularly windowed), so that the aliasing will be much more silenced using this Keiser Window. More information in the [great article by Julius O. Smith on resampling][6].

To apply the filter, I used an algorithm based on the &#8220;efficient polyphase filter bank with resampling&#8221; found on page 129 (Figure 4.3-8d) of the book [&#8220;Multirate Systems and Filter Banks&#8221; by Vaidyanathan][7].

The code is fully documented. If you have any comments or questions, or find any bug, please let me know.

Oh, and just to let you know: Python is the next and much better version of Matlab.  
Alright.

 [1]: /wp-content/uploads/2011/05/resample.zip
 [2]: http://en.wikipedia.org/wiki/Kaiser_window
 [3]: http://en.wikipedia.org/wiki/Rectangular_window
 [4]: http://en.wikipedia.org/wiki/Aliasing
 [5]: /wp-content/uploads/2011/05/KaiserIR.png
 [6]: https://ccrma.stanford.edu/~jos/resample/Theory_Practice.html
 [7]: http://www.amazon.com/Multirate-Systems-Filter-Banks-Vaidyanathan/dp/0136057187