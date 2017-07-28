Title: Running ZFS on TinkerBoard
Date: 2017-7-28 12:00
Tags: tinkerboard, zfs
Category: projects
Slug: zfs-on-tinkerboard
Authors: Lee Dobryden
Summary: Running ZFS TinkerBoard and Armbian

In my quest to replace my old Intel NUC with a TinkerBoard, one of the big
hurdles was trying to get ZFS to run on it. I thought in theory it *should* be
able to run ZFS, it seems to have enough computing power, but it is a 32-bit
processor which is [not recommended](https://github.com/zfsonlinux/zfs/wiki/FAQ#32-bit-vs-64-bit-systems),
and doesn't have ECC ram. However, having already shut down and packed up my old
computer, and needing my photo backups off of the ZFS disks, I was in a bind so
I gave it a shot. I mostly [followed the directions here](https://github.com/zfsonlinux/zfs/wiki/Custom-Packages),
but I had to do a little extra fiddling to get it to work.

1) Install the dependencies:
```bash
sudo apt-get install build-essential autoconf libtool gawk alien fakeroot
zlib1g-dev uuid-dev libattr1-dev libblkid-dev libselinux-dev libudev-dev
libdevmapper-dev parted lsscsi ksh gdebi
```


2) Download the Source:
The kernel module in the repo doesn't work, so I had to compile from source.
At the time I did this I used the latest release, 0.6.5.11 which I [downloaded here]
(https://github.com/zfsonlinux/zfs/releases/tag/zfs-0.6.5.11)
You'll need both the SPL and ZFS packages

3) Compile and install SPL:
First extract the SPL archive and change into the new dir.
Then:
```bash
./autogen.sh
./configure
```
To build a package to install on ARM I had to edit the Makefile that is created
by `./configure`.
Line 374 should read `RPMBUILD = rpmbuild --target=armhf`
Then build and install the packages:
```bash
make pkg-utils pkg-kmod
for file in *.deb; do sudo gdebi -q --non-interactive $file; done
```


4) Compile and install ZFS:
Extract the ZFS archive and change into the new dir.
Then:
```shell
./autogen.sh
./configure
```
Again build a package to install on ARM I had to edit the Makefile that is created
by `./configure`.
Line 454 should read `RPMBUILD = rpmbuild --target=armhf`
Then build and install the packages as before:
```bash
make pkg-utils pkg-kmod
for file in *.deb; do sudo gdebi -q --non-interactive $file; done
```

3) Edit `/boot/armbianEnv.txt`
I had to set the vmalloc param to help workaround the 32-bit issue mentioned earlier
I added the line `extraargs=vmalloc=1024M` to the file

4) Edit `/etc/modprobe.d/zfs.conf`
I also needed to specifically set the arc min and max for zfs. So I created the
zfs.conf file with the following lines:
```
options zfs zfs_arc_max=268435456
options zfs zfs_arc_min=268435456
```
This limits how much memory zfs will use and keeps the system from crashing. It
probably slows zfs down, but we're not running on the fastest board anyway.

5) Reboot
[Careful of that reboot bug]({filename}./4-armbian-tinkerboard.md)

Whew, that's it! You should be able to use standard ZFS mounting commands, etc. now.
I only tested retrieving files but was able to rsync many gigabytes
off of my zfs drives without issue. I wouldn't be surprised if compression and
de-duplication don't behave the best. My use case previously was mostly for mirroring capabilities
and error detection and correction. I might be better off with a standard software
raid setup now, but it's too late for that. Any updates I'll be sure to make new posts
and link to from here.
