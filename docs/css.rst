CSS
===

The Content Scramble System (CSS) is a digital rights management (DRM) and encryption system
employed on many commercially produced DVD-Video discs.

However, it's heavily flawed. It was originally defeated back in 1999 by `DeCSS <https://en.wikipedia.org/wiki/DeCSS>`_.
The 40-bit key size can be subjected to a brute-force attack as the effective key size is only
about 16 bits. That's a mere two bytes. It can be brute-forced in about a minute on even an old
Pentium II and effectively instantly on modern hardware.

.. thumbnail:: _static/images/decss.webp
   :width: 350px
   :title: Fragment of the DeCSS code

Where CSS is Applied
--------------------

CSS is applied on ISO 9660 Sectors containing VOB data in it's entirety, not on each file. Header
and IFO sectors are unprotected. A sector can contain one or more files' data, and one file's data
may reside on multiple sectors.

If you backup a protected disc to a VIDEO_TS folder without first decrypting CSS, it will be a lot
harder to re-align each VOB file, get each VTS's key for the corresponding VOBs, and decrypt, but
not impossible.

Decrypting CSS
--------------

Since CSS is applied on each 2048-byte sector, decryption occurs while reading from the disc, as
the disc would be read one sector at a time, in order from first VTS to last VTS. As the disc is
read, header information for each VTS is also read before the VOB data, allowing the CSS key to be
obtained for that VTS's. It then decrypts the following VOB data sectors with that key. Once a new
VTS sector is reached a new key for that VTS is obtained and the process repeats until all sectors
have been decrypted.

Saving Decrypted Sectors
----------------------------

Once a sector is read and decrypted, it's generally saved to the disk by appending each sectors data
(2048 bytes) to a .ISO file.

Alternatively, it is possible to read the sector data as it's being read and parse as an ISO 9660
file-system to read the filenames and data. This allows you to save as normal separate files into
a folder and is what happens when you backup directly to a VIDEO_TS folder.

You may also get a VIDEO_TS folder with VOB/IFO files by extracting from the .ISO afterwards with
a supported program like `7-zip <https://7-zip.org>`_. However, this method is slower and would use
more disk space at least temporarily while you extract from the ISO.

CSS Keys and Region Codes
-------------------------

While I don't fully understand it, there is Key negotiation between the Player Hardware and the
DVD-Video disc that may fail if the region code of the Player and the Disc doesn't match.
Modern Backup Software has ways around this via brute-force and region emulation.

However, the workarounds don't always work or result in the correct key. For example, I was
backing of Region 1 (USA) The Fresh Prince of Bel-Air DVD using my Player which was set to
Region 2. It failed to negotiate keys and used some kind of workaround on one of the VTS.
The resulting key for that VTS specifically was incorrect. The resulting stream caused corrupted
key frames at random parts of the video, and weird mushed pixels around edges of some frames.

While changing the Player region to match the disc did work, you can only do that a limited
number of times before the player refuses to change region. So, I had to get a second Player
as I often backup discs from two regions.

Can you just give me a way to do all this automatically...
----------------------------------------------------------

Sure can. Give a look at `AnyDVD HD <https://redfox.bz/en/anydvdhd.html>`_ it's a fantastic piece
of software that decrypts DVD-Video at a driver-level, essentially spoofing it as a disc with no
CSS.

This allows you to use your DVD-Video disc on any software, including legal backup solutions like
ImgBurn which is a much newer and still supported version of DVD Decrypter, which had to drop CSS
decryption functionality after legal pressure.

You can also have AnyDVD HD back up the disc for you with a very minimal UI, no bloat, no adware.
Simply back it up!

More Information
----------------

CSS has a pretty large history with an interesting legal battle.
Check out the `Content Scramble System <https://en.wikipedia.org/wiki/Content_Scramble_System>`_
Wikipedia page for more information.
