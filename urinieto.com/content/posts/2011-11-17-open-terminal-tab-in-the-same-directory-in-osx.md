---
title: Open Terminal Tab in the same Directory in OSX
author: uri
type: post
date: 2011-11-17T16:10:35+00:00
url: /2011/11/open-terminal-tab-in-the-same-directory-in-osx/
categories:
  - osx
  - programming

---
I tend to work with multiple tabs in my terminals, keep opening, closing them, and so it is very useful to me to open a new terminal in my current folder instead of going to the home.

I&#8217;ve found this nice [script][1] that will do the work for you:

``<strong>#!/bin/bash<br />
osascript -e 'tell application "Terminal"' \<br />
-e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down' \<br />
-e "do script with command \"cd `pwd`;clear\" in selected tab of the front window" \<br />
-e 'end tell' &#038;> /dev/null</strong>``

If you c&p this in a new file called &#8220;nt&#8221; in your /usr/local/bin, and you change it&#8217;s permissions to be executable ( **chmod +x /usr/local/bin/nt** ), all you have to do to open a new tab in your current directory will be:

**`$> nt`**

Nice!

 [1]: http://procbits.com/2011/07/18/open-a-new-tab-in-terminal-app-in-the-same-directory-on-mac-os-x/