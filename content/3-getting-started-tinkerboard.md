Title: Getting Started with TinkerBoard
Date: 2017-5-10 12:00
Tags: tinkerboard
Category: projects
Slug: getting-started-with-tinkerboard
Authors: Lee Dobryden
Summary: Unboxing and booting up TinkerBoard

I ordered a [Tinkerboard](https://www.asus.com/us/Single-Board-Computer/Tinker-Board/)
to try and replace some of the functions my Intel NUC
is currently fulfilling. This board was a little more interesting to me than the
raspi 3 because of it's dedicated gigabit NIC, meaning more bandwidth over the USB
bus for disk IO. More on that later... Anyway, I had a few troubles getting it setup,
so here's a few tips to get going.

![]({photo}3-tinkerboard/TinkerBox.jpg)

Finding the download for the OS was not too tricky, but definitely not intuitive.
You can [download TinkerOS here](https://www.asus.com/uk/Single-Board-Computer/Tinker-Board/HelpDesk_Download/)

The version I used at the time writing was TinkerOS_Debian V1.8 (Beta version)

I burned the SD Card with [Etcher](https://etcher.io).

I used an 8GB SanDisk Ultra SD card, which I've had good luck with on raspberry pis.

I had some trouble getting going, I tried different SD cards, different usb cables,
but ultimately it turned out that the power supply was *very* touchy.
Luckily I had a dedicated 5V 2A power supply
as no usb charging dongle or usb hub worked for me. I had issues with continual
reboots, which usually means the board is underpowered. I have seen this in the
past with raspberry pis and beagleboards, so eventually I worked out what the
issue was. To the TinkerBoard's credit, I accidentally plugged in a 9V power supply to it for
a second and it simply didn't turn on. After realizing what I'd done, I found
the supply I meant to use in the first place and it fired right up like nothing
had happened.

![]({photo}3-tinkerboard/TinkerUnboxed.jpg)

With a proper power supply the board booted up, resized the SD card, and rebooted
into an LXDE desktop session within 20 seconds.
I was able to enter a wifi password and connect easily.
I fired up chromium and it complained of the time not being set correctly, so I
opened the menu, went to preferences, time and date (default password is linaro, btw),
 and setup my timezone. After that I was in action. Playback on youtube videos
 was pretty smooth and I didn't notice notice any video tearing or stuttering.
 I only played around on the desktop for a few minutes though, so it wasn't
 the most thorough review.

 ![]({photo}3-tinkerboard/TinkerBooted.jpg)

 I look forward to playing with it more. My plan is to try to eventually replace
 my current media center/dvr/backup server/home-assistant with it.
 So we'll see if it's up for the task.
