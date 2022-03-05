Rules
=====

Golden Rules
------------

1. The release is for a Movie, TV Season, or TV Episode.
2. All content of the release must have only ever received official releases in SD resolution. [#]_
3. All Video tracks of the release must have a maximum resolution of 720x576 (PAL 4:3 SAR).
4. All Sources used to create the release must be officially sourced material. [#]_
5. All tracks must be unaltered excluding:

   - Trimming nuisance material like Bumpers, Warnings, long blanks.
   - Retiming, e.g., PAL speedup back to NTSC, general fixes.
   - Subtitle Format conversion, e.g., Image Subtitle OCR, WebVTT to SRT.
   - Subtitle Typo and Grammar checks.

.. [#] Official Upscales are not considered official HD releases.
.. [#] Source is considered official if it's distributed or licensed by the original Company or Network.

Software Configuration
----------------------

1. All files in a release must be muxed to an MKV (Matroska Video) file by MKVToolNix/mkvmerge.
2. The version of MKVToolNix must be no older than 6 months from the release's upload date. [#]_
3. You must disable ``additional lossless compression for all track types`` in MKVToolNix preferences.
   The additional compression causes compatability problems with some decoders and demuxers.

.. thumbnail:: _static/images/mkvtoolnix-extra-compression.webp
   :width: 200px
   :title: Where to disable additional lossless compression

.. [#] Unless the latest version of MKVToolNix is older than 6 months.

Prohibited Sources
------------------

You may not use any of the following types of sources in your release.
This is over concern for reliability of VOB data and condition.

1. DVDR (DVD-/+R, i.e., a Homemade DVD, unofficial). [#]_
2. Backup by DVDShrink (e.g., a DVD9 transcoded and converted to DVD5).
3. Backup by DVDFab v1.x or MacTheRipper (known to corrupt VOB data, poor reliability). [#]_
4. Releases by other groups in partial or in full, as we do not know what changes they may have made.

What's wrong with DVDFab v1.x and MacTheRipper?

   These are known to produce corrupt VOB data due to programming mistakes therefore the
   backup produced by them is entirely unreliable. The corruption can be either minor or
   incredibly bad. This can often be attributed to small bits of "weird block corruption"
   in both Remuxes and Encodes, or straight up corrupt keyframes causing all adjacent P
   and B frames to be really messed up.

   This is confirmed to be the case for DVDFab v1.x, but other versions may have this
   issue as well. As for MacTheRipper, no specific version is known but while unlikely,
   it may be happening on all versions. MacTheRipper should not be confused with
   "Mac DVDRipper".

   You would be very surprised how often old cult-classic shows and movies are dumped
   with one of these software, especially for Kids DVDs around the 2000s. 
   
   Sadly there is no definitive way to check if one of these software was used or not.
   So please be wary of any extreme amount of warnings or errors by MakeMKV, and look
   for any signs of DVDFab or MacTheRipper use. If feasable, a fresh backup by AnyDVD
   HD would be ideal.

.. [#] Amazon's MOD (Made-on-Demand) discs are officially licensed, therefore they are allowed.
.. [#] MakeMKV will warn you if it detects metadata set by DVDFab v1.x or MacTheRipper.
