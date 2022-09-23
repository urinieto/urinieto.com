---
title: How to get all indexPaths from a UITableView?
author: uri
type: post
date: 2009-05-27T14:57:32+00:00
url: /2009/05/how-to-get-allindexpaths-from-a-uitableview/
categories:
  - iphone

---
I find this a very basic question, but somewhat difficult to find in the Apple documentation. The answer is not found in the [NSIndexPath Class Reference][1], but in the [NSIndexPath UIKit Additions][2]. That&#8217;s why I think some people would not know about the following method which allows us to get a specified indexPath from a UITableView.

The method is:

    + (NSIndexPath *)indexPathForRow:(NSUInteger)row inSection:(NSUInteger)section

And it returns an indexPath object initialized with the indexes of a specific row and section in a table view.

With this method we will be able to retrieve all the indexPaths from a table view performing a loop like this:

    NSInteger nSections = [tableView numberOfSections];
    for (int j=0; j<nSections; j++) {
      NSInteger nRows = [tableView numberOfRowsInSection:j];
      for (int i=0; i<nRows; i++) {
        NSIndexPath *indexPath = [NSIndexPath indexPathForRow:i inSection:j];
        //Do something with your indexPath. Maybe you want to get your cell,
        // like this:
        //UITableViewCell *cell = [tableView cellForRowAtIndexPath:indexPath];
      }
    }
    

I hope this helps. If you find an easier way, please tell me.

 [1]: https://developer.apple.com/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSIndexPath_Class/Reference/Reference.html
 [2]: https://developer.apple.com/iPhone/library/documentation/UIKit/Reference/NSIndexPath_UIKitAdditions/Reference/Reference.html