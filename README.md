# urinieto.com

[![Netlify Status](https://api.netlify.com/api/v1/badges/e6a22004-09b5-446c-b26f-c715d8b81dd1/deploy-status)](https://app.netlify.com/sites/urinieto/deploys)

My personal website. It's built with [Hugo](https://gohugo.io/) with the [Anatole theme](https://github.com/lxndrblz/anatole). It's hosted at [Netlify](https://www.netlify.com/).

## Install

Clone this repo and activate the submodules:

    git submodule init
    git submodule update

Remove the `!` character from `urinieto.com/themes/anatole/assets/js/jquery.js` in line 521.

(#hacks)

## To Add A New Post

Go to the root of the hugo page (urinieto.com/) and type:

    hugo new posts/<date>-<name>.md

E.g.,
    
    hugo new posts/2024-01-13-incrediblepost.md


## To Run the Hugo Server Locally

    hugo server --disableFastRender -D
