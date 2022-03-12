Utilities
=========

This page has a list of helpful software utilities for various purposes.

Technical Analysis
------------------

`MediaInfo <https://mediaarea.net/en/MediaInfo>`_
    Convenient unified display of the most relevant technical and tag data for video and audio files.
    There's also a `Python wrapper <https://github.com/sbraz/pymediainfo>`_ for programmatic use.

`BDInfo <https://github.com/UniqProject/BDInfo>`_
    BDInfo tool to collect video and audio technical specifications from Blu-ray discs.

Muxing/Remuxing
---------------

`MKVToolNix <https://mkvtoolnix.download>`_
    Set of tools to create, alter and inspect Matroska files.

`MakeMKV <https://makemkv.com>`_
    Backup DVDs and Blu-rays as Matroska files. Can also backup Blu-ray discs to HDD.

Demuxing
--------

`eac3to <https://videohelp.com/software/eac3to>`_
    Primarily used to demux and/or convert Audio tracks from Blu-rays and DVDs to Matroska files.
    It can also be used to demux Video tracks, and is a common alternative to MakeMKV.

`Inviska MKV Extract <https://videohelp.com/software/Inviska-MKV-Extract>`_
    Batch demux any and all tracks from Matroska files with a simple GUI.
    Chapters are extracted to XML Matroska format.

`Chapter-Demuxer <https://github.com/jlw4049/Chapter-Demuxer>`_
    Extract Chapters from Matroska files to Simple Matroska format.

`pymplschapters <https://github.com/rlaphoenix/pymplschapters>`_
    Extract Chapters from Blu-ray MPLS playlists to XML Matroska format.

Subtitles
---------

`SubtitleEdit <https://github.com/SubtitleEdit/subtitleedit>`_
    Incredibly powerful Subtitle Viewer, Editor, and OCR software.
    Very useful to tweak or fix captions, sync captions, and so much more.

`DVDSubEdit <https://videohelp.com/software/DVDSubEdit>`_
    Old but gold DVD VobSub OCR tool. Generally more consistent and reliable OCR
    compared to SubtitleEdit.

`BDSup2Sub <https://videohelp.com/software/BDSup2Sub>`_
    Old but gold software for converting between Image-based Subtitle formats of
    Blu-ray and DVD. This does not OCR.

`ffsubsync <https://github.com/smacke/ffsubsync>`_
    Language-agnostic automatic synchronization of subtitles with video.
    In some scenarios, this can be extremely powerful.

Frame Serving
-------------

These utilities provide Frame Indexing, Decoding, and Serving to supported NLEs.
The only NLEs I know with support for all of these, is VapourSynth_ and AviSynth_.

Both are Script-based NLEs and do not use GUIs but rather Python scripts.
GUIs are available, but are more so for previewing the script output.
There are GUIs for applying changes, effects, and so on, but are very limited and
the only one I'm aware of is Japanese-only.

`DGMpgDec (DGIndex) <https://rationalqm.us/dgmpgdec/dgmpgdec.html>`_
    MPEG-1/2 Decoder and Frame Server.
    DGMPGDec is a multi-project containing DGIndex, DGDecode, and DGVfapi.

`L-SMASH <https://github.com/VFR-maniac/L-SMASH-Works>`_
    Video Decoder and Frame Server using Libavcodec, allowing support for a very wide
    range of codecs, all with accurate frame indexing.
    I highly recommend L-SMASH over FFMS/FFMS2 where possible, it's generally less buggy.
    Both FFMS2 and L-SMASH ultimately use Libavcodec, therefore L-SMASH is a great alternative to FFMS2.

`FFMS2 (FFmpegSource2) <https://github.com/FFMS/ffms2>`_
    Video Decoder and Frame Server using FFmpeg, allowing support for a very wide range
    of codecs.
    I've encountered bugs and problems usually relating to poor support for x/y/z version
    of FFmpeg, seeking is a mess sometimes, decoding is unreliable overall.
    I've had a lot more success with L-SMASH over FFMS2.

.. _VapourSynth: https://vapoursynth.com
.. _AviSynth: https://github.com/AviSynth/AviSynthPlus

Filenames and Documentation
---------------------------

`FileBot ($6, trial) <https://filebot.net>`_
    Automate filenames for Movies, TV, and Music files. Super handy to automatically set a
    filename based on the Content and it's Streams.

`nfog <https://github.com/rlaphoenix/nfog>`_
    Automate NFO and Description templates using a bit of Python. Supports Artwork files and
    can be run with a simple CLI call.

Chocolatey packages
-------------------

Here's a list of repositories with `Chocolatey <https://chocolatey.org/>`_ packages not
added to the official repository.

- `rlaphoenix/chocolatey-packages <https://github.com/rlaphoenix/chocolatey-packages>`_
