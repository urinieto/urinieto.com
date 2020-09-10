---
title: Vim (or MacVim) as a C/C++ IDE
author: uri
type: post
date: 2014-09-01T15:01:53+00:00
url: /2014/09/vim-or-macvim-as-a-c-ide/
categories:
  - programming

---
This post is meant to be a little guide to setting up Vim (or MacVim) as your next favorite C/C++ IDE. Vim is probably the most powerful text editor that humans have ever created, so you should consider using it even if its learning curve is a [bit steep][1].

### MacVim

  


First, let&#8217;s install MacVim. MacVim adds a graphical interface to Vim that can help newcomers (only for OSX users, others should consider GVim). Skip the next steps if you want to use the regular Vim instead.

  * Get the latest snapshot of MacVim from [here][2] (make sure you have the correct OSX version).
  * Decompress it (double click) and drag MacVim.app to your Applications folder.
  * Open the Terminal (commonly located in /Applications/Utilities/Terminal.app, but I suggest you put it in your Dock) and go to the MacVim Snapshot folder you just downloaded. In my case, I had to type the following:  
    `cd ~/Downloads/MacVim-snapshot-73/`
  * Copy the `mvim` binary to your PATH so that you can open MacVim from any directory in your computer. Like this (you will have to enter your machine password):  
    `sudo cp mvim /usr/bin`
  * Now you should be able to start a new document with MacVim by typing:  
    `mvim hello.c`  
    (Type `:w` to quit).

### .vimrc

  


Now that you have Vim (and/or MacVim) installed in your system, the next thing you should do is to set it up to adapt it to your needs. The rest of the instructions work for Vim and MacVim, so I will use Vim to refer to both (simply replace `vim` for `mvim` if you want to use MacVim). Vim is highly configurable, but here I will describe what I believe is the most useful setup for new users and C/C++ developers.

The Vim (or MacVim) configuration file is located in `~/.vimrc`. Therefore, type `vim ~/.vimrc` to start editing your configuration. You might see a blank file if you have never edited Vim&#8217;s configuration before. You can copy and paste the following. There&#8217;s a comment for the most important commands, so that you can understand what these lines do if you are interested.

<pre class="brush: vimscript; title: ; notranslate" title="">" Enables highlight syntax
syntax enable
set nofoldenable

" Sweet colorscheme
" colorscheme codeschool
set background=dark

" Set utf8 as standard encoding and en_US as the standard language
set encoding=utf-8

"" Display line numbers on the left
set number

"" Use mouse (only for resizing!)
set mouse=a

" Set the focus to the correct screen (ok, no more mouse thingies)
set mousefocus

" No more annoying sounds
set visualbell

" Do not scroll sideways unless we reach the end of the screen
set sidescrolloff=0

" highlight the status bar when in insert mode
if version &gt;= 700
    if has("gui_running")
        au InsertEnter * hi StatusLine guifg=black guibg=green
        au InsertLeave * hi StatusLine guibg=black guifg=grey
    else
        au InsertEnter * hi StatusLine ctermfg=235 ctermbg=2
        au InsertLeave * hi StatusLine ctermbg=240 ctermfg=12
    endif
endif

" Infere the case-sensitivity
set infercase

" Need to set this flag on in order to have many cool features on
set nocompatible

" Indent properly based on the current file
filetype indent plugin on
filetype plugin on

" Pathogen load
"filetype off " Makes syntax non-working on office box
call pathogen#infect()
call pathogen#helptags()

" Switch between files in buffer
nnoremap &lt;C-Tab&gt; :bn&lt;CR&gt;
nnoremap &lt;C-S-Tab&gt; :bp&lt;CR&gt;

" Change default fontsize to fit MacBook Pro 13'
set guifont=Monaco:h11

" Don't select first Omni-completion option
set completeopt=longest,menuone
"set completeopt=menuone,longest,preview

set tabstop=4     " a tab is four spaces
set backspace=indent,eol,start
                  " allow backspacing over everything in insert mode
set autoindent    " always set autoindenting on
set copyindent    " copy the previous indentation on autoindenting
set shiftwidth=4  " number of spaces to use for autoindenting
set shiftround    " use multiple of shiftwidth when indenting with '&lt;' and '&gt;'
set incsearch     " show search matches as you type
set expandtab
set shiftwidth=4
set softtabstop=4

" Always set the current file directory as the local current directory
autocmd BufEnter * silent! lcd %:p:h

" Enable folding
nnoremap &lt;silent&gt; &lt;Space&gt; @=(foldlevel('.')?'za':"\&lt;Space&gt;")&lt;CR&gt;
vnoremap &lt;Space&gt; zf

set history=1000         " remember more commands and search history
set undolevels=1000      " use many levels of undo

" Tabs in command line mode behave like bash
set wildmode=longest,list,full
set wildmenu

" Highlight the entire word when searching for it
set hlsearch

"====[ Make tabs, trailing whitespace, and non-breaking spaces visible ]======
exec "set listchars=tab:\uBB\uBB,trail:\uB7,nbsp:~"
set list

" Move line by line even when the line is wrapped
map j gj
map k gk

" Persistent undo
set undofile                " Save undo's after file closes
set undodir=$HOME/.vim/undo " where to save undo histories
set undolevels=1000         " How many undos
set undoreload=10000        " number of lines to save for undo

" YouCompleteMe
let g:ycm_global_ycm_extra_conf = "~/.vim/bundle/YouCompleteMe/.ycm_extra_conf.py"
nnoremap &lt;leader&gt;g :YcmCompleter GoToDefinitionElseDeclaration&lt;CR&gt;
</pre>

### Plugins

  


Now it&#8217;s time to install some plugins. We will start with [Pathogen][3], a script to make the installation of other scripts extremely easy. To install Pathogen, just type:

`mkdir -p ~/.vim/autoload ~/.vim/bundle<br />
curl https://raw.githubusercontent.com/tpope/vim-pathogen/master/autoload/pathogen.vim > ~/.vim/autoload/pathogen.vim<br />
` 

Using Pathogen, we will install [Syntastic][4], a wonderful plugin to identify errors in your code (linting) in the most popular programming languages. To install it, just type:

`cd ~/.vim/bundle &#038;&#038; \<br />
git clone https://github.com/scrooloose/syntastic.git`

Now restart Vim and type `:Helptags`. Linting should be working now for C/C++.

The next plugin to install is [MiniBufExplorer][5], which will make our life easier when dealing with multiple files in Vim. To install it, simply type:

`cd ~/.vim/bundle &#038;&#038; \<br />
git clone https://github.com/fholgado/minibufexpl.vim.git`

We also want to have some auto complete options when developing our C/C++ programs. The best plugin I&#8217;ve found is called [YouCompleteMe][6], which is compatible with basically all the most popular programming languages to date. Type the following to install it:

`cd ~/.vim/bundle &#038;&#038; \<br />
git clone https://github.com/Valloric/YouCompleteMe.git<br />
cd YouCompleteMe<br />
git submodule update --init --recursive<br />
./install.sh --clang-completer`

Note: You might need to install Homebrew to install YouCompleteMe. To install it, type:

`<br />
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"<br />
` 

You will need to do some additional setup in order to get the plugin working. As you may see in the second to last line of the `.vimrc` above, we set up the default configuration file in `~/.vim/bundle/YouCompleteMe/.ycm_extra_conf.py`. You can simply copy [my .ymc\_extra\_conf.py][7] in this folder. To do so, simply type:

`curl /drop/.ycm_extra_conf.py > ~/.vim/bundle/YouCompleteMe/.ycm_extra_conf.py`

Finally, the last plugin to install is the [C Plugin][8], which will help us when navigating through C/C++ files, debugging, etc. This plugin does not support Pathogen installation, so we will have to do it manually. Go to the official plugin page: <http://www.vim.org/scripts/script.php?script_id=213> and download the latest `cvim.zip`. Copy the zip file to your `~/.vim/` folder and type:

`unzip cvim.zip`

Before we are done, you should configure the template file with your name and affiliation. To do so, edit the template file and edit the user macros, like this:

`vim ~/.vim/c-support/templates/Templates`

My User Macros look like this:

`<br />
§ ==========================================================<br />
§  User Macros<br />
§ ==========================================================</p>
<p>SetMacro( 'AUTHOR',      'Oriol Nieto' )<br />
SetMacro( 'AUTHORREF',   '' )<br />
SetMacro( 'COMPANY',     'New York University' )<br />
SetMacro( 'COPYRIGHT',   '' )<br />
SetMacro( 'EMAIL',       'oriol@nyu.edu' )<br />
SetMacro( 'LICENSE',     '' )<br />
SetMacro( 'ORGANIZATION','New York University' )`

If you&#8217;ve done everything correctly, you will be able to create a new .c file (e.g. `vim hello.c` and a nice template will be included in the top of the file. Moreover, you should be able to open multiple files (e.g. `:e otherfile.c`) and they will appear in the MiniBufferExplorer. And finally, if you make some errors while coding, Syntastic will tell you. As an example, see the following screenshot:

<div id="attachment_1883" style="width: 510px" class="wp-caption aligncenter">
  <a href="/wp-content/uploads/2014/09/Screen-Shot-2014-09-01-at-10.58.09-AM.png"><img src="/wp-content/uploads/2014/09/Screen-Shot-2014-09-01-at-10.58.09-AM-500x806.png" alt="MacVim with the following plugins: Syntastic, YouCompleteMe, C.vim, and MiniBufExplorer" width="400" height="706" class="size-medium wp-image-1883" /></a>
  
  <p class="wp-caption-text">
    MacVim with the following plugins: Syntastic, YouCompleteMe, C.vim, and MiniBufExplorer
  </p>
</div>

Please, let me know if you have any questions. I hope you enjoy your new IDE!

 [1]: http://mrozekma.com/editor-learning-curve.png
 [2]: https://github.com/b4winckler/macvim/releases
 [3]: http://www.vim.org/scripts/script.php?script_id=2332
 [4]: https://github.com/scrooloose/syntastic
 [5]: https://github.com/fholgado/minibufexpl.vim
 [6]: https://github.com/Valloric/YouCompleteMe
 [7]: /drop/.ycm_extra_conf.py
 [8]: http://www.vim.org/scripts/script.php?script_id=213