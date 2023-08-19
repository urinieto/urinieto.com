---
title: "Efficient Spoken Language Recognition via Multilabel Classification"
author: uri
type: post
date: 2023-08-19T08:22:02+09:00
url: language-detection-interspeech23
draft: false
thumbnail:
  src: "/wp-content/uploads/2023/ErrorRateParams.png"
  alt: Thumbnail image
categories:
  - papers
  - interspeech

---

TL;DR: we present efficient models for the task of Spoken Language Recognition plus an effective strategy to gracefully handle unsupported languages via multilabel classification.
Read our new Interspeech 2023 paper [here](https://arxiv.org/abs/2306.01945).

Here's a little video to motivate our work:

{{< video "/wp-content/uploads/2023/Interspeech2023.mp4" >}}

To potentially address this issue, we could:

- Have efficient models to quickly assess the language that the user is speaking so that the right language is selected for the speech-to-text model.
- Have a better way to handle unsupported languages.

And that's exactly what we do in our paper!

We present two sets of models, based on TC-ResNets and ECAPA-TDNNs: TC-ResNet10, TC-ResNet14, and LECAPAT (Light ECAPA-Tdnn). These models are _orders of magnitude smaller_ than baselines! Check out this plot, and note the logarithmic scale on the y axis:

{{< img src="/wp-content/uploads/2023/SLR-models.png" alt="" width="550" >}}

When assessed with the VoxLingua107 dataset, these models can be comparable in performance to models that have orders of magnitude more parameters that only address the task of Spoken Language Recognition.
In the following Figure, we plot the error rates against the model parameters (so that we ideally want models in the bottom left corner). Our proposed LECAPAT performs almost equally than ECAPA-TDNN, with two orders of magnitude less parameters!

{{< img src="/wp-content/uploads/2023/ErrorRateParams.png" alt="" width="550" >}}

Moreover, the proposed models are _fast_! Here's a plot of their real-time factor, the higher the better:

{{< img src="/wp-content/uploads/2023/RealTimeFactor.png" alt="" width="550" >}}

Finally, we present a multilabel approach during training that, without adding any sort of complexity to the model, it allows to handle unsupported classes better, so that the problem motivated in the video will no longer occur!
Here the confusion matrix of a standard model (using multiclass) on the left, and our proposed multilabel strategy on the right:

{{< img src="/wp-content/uploads/2023/ConfusionMatrices.png" alt="" width="550" >}}

The final row and columns represent the “other” class. We can see how there are so many false positives on the left matrix (e.g., Norwegian is classified almost 30% of times as “other”, and Portugeuese is always classified as “other”. On the other hand, with our proposed multilabel strategy (right), Portuguese is always correctly classified, and Norwegian is only classified as “other” 10% of times.)

And that's it! This is, to the best of our knowledge, the first paper to address _efficiency_ in the task of Speaker Language Recognition. 
We hope this work motivates the usage of such tiny models so that our little assistants will no longer get confused when we speak to them in other languages rather than English, without having to manually configure them! Making the world a better place, one step at a time, titans!
