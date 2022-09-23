---
title: Upload Videos to YouTube with iPhone custom App
author: uri
type: post
date: 2010-10-15T20:20:25+00:00
url: /2010/10/upload-videos-to-youtube-with-iphone-custom-app/
categories:
  - google
  - iphone

---
**EDIT**: This is an old post, and apparently things have changed quite a bit. Unfortunately I haven&#8217;t had the time to update this and I&#8217;m not sure what the process to upload videos to YouTube is anymore.

With the 4.0 iOS and its new [AVCaptureSession][1] we now have access to video data, so that developers can edit this info and create cool apps such as [SketchWiz][2], [Predator Vision][3] or [iRetroscope][4].

However it&#8217;s not clear how these videos can be shared through the net. So in this post I&#8217;ll explain how we can upload videos to YouTube with a custom app and provide some **[sample code][5]** to test it.

We will need the **Google Data API Client for Objective-C**, and install it into our application. Here are the steps to do so:

&#8211; Download the GData Client for Objective-C from [here][6]  
&#8211; Open the GData project with XCode  
&#8211; Drag and drop the group _GData Source_ from the GData project into your project (reference it or copy it into your project directory, up to you)  
&#8211; Optional: In your project delete all groups inside _GData Source_ but **YouTube** and **Commons**. This will make the compilation process much faster. You will have to comment the imports in your GData.h  
&#8211; Add the **Security.framework** into your frameworks  
&#8211; In the properties of your target, add the **-ObjC** to your _Other Linker Flags_ setting  
&#8211; In the properties of your target, add the **/usr/include/libxml2** path to your _Header Search Path_ setting  
&#8211; Make sure your _C Language Dialect_ is **c99** in your target properties

You should now be able to compile the API within your own app.

Next step is to go [here][7] to get a **Developer Key from Google**. Your Developer Key and Client ID are required in order to use the GData API.

Once you have them, take a look at the [simple YouTube upload test sample code][5] based on the Mac OSX Example inside the GData Client Objective-C code and add them there in the YouTubeTestViewController.m.

**[Sample Code][5]**

For more information and other type of installations for the API, please read the [API documentation][8].

I hope it helps. Any feedback is welcome as always.

 [1]: https://developer.apple.com/library/ios/#documentation/AVFoundation/Reference/AVCaptureSession_Class/Reference/Reference.html#//apple_ref/occ/cl/AVCaptureSession
 [2]: https://itunes.apple.com/us/app/sketchwiz/id392835926?mt=8
 [3]: https://itunes.apple.com/us/app/predator-vision/id384111522?mt=8
 [4]: https://itunes.apple.com/us/app/iretroscope/id385118861?mt=8
 [5]: /iPhone/YouTubeTest.zip
 [6]: https://code.google.com/p/gdata-objectivec-client/downloads/list
 [7]: https://code.google.com/apis/youtube/dashboard/gwt/index.html#newProduct
 [8]: https://code.google.com/p/gdata-objectivec-client/wiki/BuildingTheLibrary#Linking_to_the_iPhone_Static_Library