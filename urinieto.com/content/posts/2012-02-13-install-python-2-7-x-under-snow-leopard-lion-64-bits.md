---
title: Install Python 2.7.x under Snow Leopard / Lion (64 bits)
author: uri
type: post
date: 2012-02-13T16:57:03+00:00
url: /2012/02/install-python-2-7-x-under-snow-leopard-lion-64-bits/
thumbnail:
  src: "/wp-content/uploads/2012/02/Python-500x311.png"
  alt: Thumbnail image
categories:
  - programming
  - python

---
OS X comes with a Python installation that I find a bit confusing and misleading. What I present in this post is a guide to remove the default Python from your 64 bits OS X (i.e. Snow Leopard or Lion), install its latest version, and set up a nice environment to work with (e.g. iPython + MacVim). The only requirement for this process is to have the latest version of **XCode**, that you can get from the **App Store**.

**Uninstall Python**

I couldn&#8217;t find any nice and clean uninstaller for Python in OS X. So we will have to remove all files by hand. Here is the code:

`sudo rm -rf /Library/Frameworks/Python.framework<br />
sudo rm -rf /Applications/Python*<br />
sudo rm -rf /Library/Python*<br />
cd /usr/local/bin<br />
sudo rm -rf 2to3 idle idle2.7 pydoc pydoc2.7 python* smtpd.py smtpd2.7.py<br />
cd /usr/bin<br />
sudo rm -rf 2to3 idle idle2.7 pydoc pydoc2.7 python* smtpd.py smtpd2.7.py<br />
` 

(if you have another versions of Python installed (e.g. 2.6, 2.5), just change 2.7 for your version number when removing the files. However, that is not really that important, just so that you don&#8217;t have that much garbage in your computer).

**Install Python 2.7.x**

Now let&#8217;s install the latest release of 2.7.x for OS X. You can see the latest releases [here][1]. When writing this post, the latest version is [2.7.2][2].

Once you have run the installer, edit your **~/.bash_profile** file. To edit your file, use your favorite text edito (vim in my case):

`vim ~/.bash_profile`

You should now have the following lines (add them if you don&#8217;t, but the installer is supposed to add them for you):

`<br />
# Setting PATH for Python 2.7<br />
# The orginal version is saved in .bash_profile.pysave<br />
PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:${PATH}"<br />
export PATH<br />
` 

Now let&#8217;s add the compiler flags for 64-bits and the Python Path for the modules. **This is important, otherwise your easy_install will probably fail**. Add the following lines to your _~/.bash_profile_:

`export PYTHONPATH=/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages<br />
export CFLAGS="-I/Developer/SDKs/MacOSX10.7.sdk/usr/lib/"<br />
export ARCHFLAGS="-arch x86_64"`

(note: change MacOSX10.7 to MacOSX10.6 if you&#8217;re using Snow Leopard in the second line)

Notice that all your modules will be installed here:  
**/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages**. It&#8217;s kind of important to remember this path, so you may want to add it to your sidebar in Finder or create some soft link.

Close your file and restart your bash so that the new environment variables are available. Check that you can now run python from the new terminal.

**Install most common modules**

I usually use easy_install to install new modules. You can get it from [here][3] (the module is called setuptools).

Download it, decompress it, and type the following from it&#8217;s folder:

`python setup.py build<br />
python setup.py install`

Now you can use _easy_install_ to install your favorite modules. E.g.:

`easy_install numpy<br />
easy_install scipy<br />
easy_install matplotlib<br />
easy_install ipython`

If you&#8217;re running Lion, I highly recommend the [SciPy SuperPack][4], which will do all the work for you.

**Setting up your programming environment**

This last section is completely biased due to my eternal love to **VIM**. I know some heartless people who use Emacs, or even Eclipse (I was one of them, and it was a terrible thing!) to code in Python.

If you&#8217;re a VIM lover you should already know about [MacVim][5], but if you don&#8217;t you should definitively get it.

In any case, you should choose your favorite text editor (in case you want to use VIM -everybody wants to use VIM, but unfortunately some people don&#8217;t know that-, here it is a nice [python module][6]), and then I highly recommend using iPython instead of the classic Python console. This is especially useful for debugging and plotting. iPython is life changing, really.

To run iPython with matplotlib already running in the background just type:

`ipython --pylab`

Finally, here is a nice screenshot of how my programming environment looks like (iPython + PyLab + MacVim):

[{{< img src="/wp-content/uploads/2012/02/Python-500x311.png" alt="" title="Python" width="500" height="311" class="aligncenter size-medium wp-image-1469" >}}][7]

Beautiful isn&#8217;t it? : )

And finally, for something -not that- completely different: Happy programming!

 [1]: https://python.org/download/releases/
 [2]: https://python.org/ftp/python/2.7.2/python-2.7.2-macosx10.6.dmg
 [3]: https://pypi.python.org/pypi/setuptools
 [4]: https://fonnesbeck.github.com/ScipySuperpack/
 [5]: https://code.google.com/p/macvim/
 [6]: https://www.vim.org/scripts/script.php?script_id=790
 [7]: /wp-content/uploads/2012/02/Python.png