Rules
=====

Last updated: 2023-09-09 02:03 UTC

Golden Rules
------------

1. The release must be for a Movie, TV Season, or TV Episode.
2. The release must be in SD resolution (no more than 576 pixels in vertical resolution).
3. The title the release is for must not have an Official HD version available. [#]_
4. All Source(s) used to create the release must be officially sourced material. [#]_
5. All Source material must be kept unaltered, with the following exceptions:

   - Trimming nuisance material like Bumpers, Warnings, and long blanks (with reason).
   - Retiming fixes where appropriate (retiming PAL->NTSC or NTSC->PAL is explicitly not allowed).
   - Required fixes for playback in the modern age (only if absolutely necessary).
   - Subtitle format conversion and OCR.
   - Subtitle typo and grammar fixes.

.. [#] Official Upscales are not considered official HD releases.
.. [#] Source(s) are considered Official if they are distributed or licensed by the original Company/Network, or a Distributor.

Software Configuration
----------------------

1. All files in a release must be muxed to an MKV (Matroska Video) file by MKVToolNix/mkvmerge.
2. The version of MKVToolNix must be no older than 6 months from the release's upload date. [#]_
3. You must disable ``additional lossless compression for all track types`` in MKVToolNix preferences.
   The additional compression causes compatibility problems with some decoders and demuxers.

.. thumbnail:: _static/images/mkvtoolnix-extra-compression.webp
   :width: 200px
   :title: Where to disable additional lossless compression

.. [#] Unless the latest version of MKVToolNix is older than 6 months.

Prohibited Sources
------------------

To comply with Golden Rule 4, you may not use any of the following types of sources in your release.
This is over concern for the reliability of VOB data and the possibility of altered, removed, or missing data.

1. DVDR (DVD-/+R, i.e., a Homemade DVD, unofficial). [#]_
2. Backup by DVDShrink (e.g., a DVD9 transcoded and converted to DVD5).
3. Backup by DVDFab v1.x or MacTheRipper (known to corrupt VOB data, poor reliability). [#]_
4. Releases by other groups in partial or in full, as we do not know what changes they may have made. [#]_

What's wrong with DVDFab v1.x and MacTheRipper?

   These are known to produce corrupt VOB data due to programming mistakes therefore the
   backup produced by them is entirely unreliable. The corruption can be either minor or
   incredibly bad. This can often be attributed to small bits of "weird block corruption"
   or `Datamoshing <https://en.wikipedia.org/?title=Datamoshing&redirect=no>`_ properties
   in both Remuxes and Encodes or straight-up corrupt keyframes causing all adjacent P
   and B frames to be really messed up or missing.

   This is confirmed to be the case for DVDFab v1.x, but other versions may have this
   issue as well. As for MacTheRipper, no specific version is known but while unlikely,
   it may be happening on all versions. MacTheRipper should not be confused with
   "Mac DVDRipper".

   You would be very surprised how often old cult-classic shows and movies are dumped
   with old and unreliable software, especially for Kids' DVDs. Sadly there is no
   definitive way to check if one of these software was used or not. So please be wary
   of any warnings or errors by MakeMKV, and look for any signs of DVDFab or MacTheRipper
   use.

   It's worth the ease of mind of dumping your own copy, and I recommend you do the job
   with AnyDVD HD. There are a lot of public libraries around the world that have a vast
   collection of DVDs, including quite rare or niche ones. I employ you to give them a
   shot. A small walk down to the library is a lot easier than working on a REPACK and
   scrounging around to look for an alternative non-dodgy source.

.. [#] Amazon's MOD (Made-on-Demand) discs are officially licensed, therefore they are allowed.
.. [#] MakeMKV will warn you if it detects metadata set by DVDFab v1.x or MacTheRipper.
.. [#] To clarify, ISO, VIDEO_TS, or other backup-like releases by other groups are allowed to be used.
       However, `REMUX`s, Encodes, or anything that is not strictly RAW, are not to be used.
