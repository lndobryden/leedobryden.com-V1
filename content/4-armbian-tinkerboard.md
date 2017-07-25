Title: Armbian on TinkerBoard
Date: 2017-7-25 12:00
Tags: tinkerboard
Category: projects
Slug: armbian-on-tinkerboard
Authors: Lee Dobryden
Summary: Booting up Armbian TinkerBoard

After some googling trying to solve some problems I was having with installing
some things on TinkerOS, I found that Armbian started supporting TinkerBoard.
It seemed like they were making a lot of advances very quickly, so I thought I'd
give it a try.

I downloaded the image here: [](https://www.armbian.com/tinkerboard/)
It's worth noting that they also noted the power supply was crucial,
as I discussed issues with in my previous post.

As usual I burned an SD Card using [Etcher](https://etcher.io). I used my usual
8GB SanDisk Class 10 card that I have had a lot of success with.

First boot was very nice, you login as `root` and password `1234`, and are
immediately prompted to change it, and create a new primary user. This is a great
attention to detail by the armbian team. The armbian teams notes a couple issues
with the TinkerBoard, mentioning there's some issues with the ethernet driver. I
haven't tested this at all to confirm, but the ethernet seems to work well enough.
One large issue is that rebooting doesn't work properly. However as of a couple days
ago there's a patch to address this in the 4.13 kernel that should hopefully be
mainlined soon.

Overall, I like Armbian, I'm going to stick with it moving forward. I was able
to get Home Assistant, TVHeadend, and even got ZFS compiled and
running. I'll write about both of these soon.
