AnyDVD HD
=========

AnyDVD HD is incredibly simple and fast Backup Solution for Blu-rays and DVDs. It's fantastic
support, consistent updates, and absolutely no ad-ware push it far past the competition.

:Website: https://redfox.bz/en/anydvdhd.html
:Price: €59 for 1 year,
        €75 for 2 years,
        €89 for 3 years,
        or €109 for a lifetime license
:Payment Methods: VISA, MasterCard, Bitcoin, Bitcoin Cash, and Litecoin
:Discounts: 10% off if you pay with any cryptocurrency

The rest of this page will guide you through AnyDVD HD settings for the best experience. All of
these settings changes are completely optional though recommended.

The majority of the settings we will change are to keep the untouched nature of the backups, and to
keep all backups compliant with rules in most communities. It also aims to disable annoying parts
of the software, like unnecessary popups or nags.

The following sections refer to the final settings you should use for the same-named menus in
AnyDVD HD Settings.

Program Settings
----------------

The following changes prevent annoying popups, enables further protection removal, and ensures that
your system won't go into Sleep Mode or Power Saving mode while in use. I also recommend disabling
Disc Autoplay popups in Windows Settings.

- ☑ Enable AnyDVD
- ☑ Autostart
- ☐ Aggressive I/O Mode
- ☐ Hide Icon
- ☑ Automatically check for new AnyDVD version
- ☐ Show information window for new media
- ☐ Show Balloon Tip while AnyDVD is scanning discs
- ☐ Show information window while AnyDVD is scanning discs
- ☑ Disable power saving
- ☐ Show warning, if no drive is detected.
- ☐ Show warning, when ripping a DVD to image
- ☑ Show warning, when creating a protected image
- ☑ Show "Aggressive I/O Mode" warning
- ☑ Prevent player software from detecting Cinavia
- ☑ Remove Cinavia watermark from CloneBD audio stream during copy

Drives
------

Here you can enable or disable Speed Control to reduce the noise from your drive in the case that
it's too loud. However, This will of course reduce the read speed as well. Generally it's up to
you if you want to use it or not, and it shouldn't affect accuracy or reliability of backups.

Selection
~~~~~~~~~

You can also choose which drives to enable or disable for AnyDVD HD under the Selection sub-menu.

Video DVD
---------

The following changes help create optimal DVD backups that are untouched as much as possible while
gaining benefits like disabling Prohibited User Operations.

Navigation
~~~~~~~~~~

Everything here is disabled as annoying or short clips are kept for an untouched backup. Most
communities will not accept a DVD backup if any clip were to be removed, as it would not be
untouched.

- ☐ Remove annoing clips from menus
- ☐ Remove annoying intro and outro clips from menus
- ☐ Remove annoying titles shorter than...
- ☐ Show Dialog to set Video DVD settings for each individual Drive

Default Region
~~~~~~~~~~~~~~

This should be set to what you expect to be backing up the most often.

Feature Removal
~~~~~~~~~~~~~~~

The following changes generally remove region checks (software and hardware based), extra
protection systems, Prohibited User Operations, and Autorun files.

- ☑ Software Region Code
- ☑ Hardware Region Code: Simulate RPC2 drive with matching region
- ☑ Region Code Scripts
- ☑ Analog Protection Systems
- ☑ Prohibited User Operations
- ☑ PC-Friendly (Autorun on Video DVD)
- ☑ Copy Protection based on unreadable Sectors
- ☐ CSS Mastering Errors

AI Scanner
~~~~~~~~~~

I generally leave this as the Default option, in my case "Automatic" as it isn't clear what it
actually does, and "Always Enabled" is specifically marked as "Not Recommended".

Subtitles
~~~~~~~~~

- ☐ Subtitle Transparency

Subtitle transparency should not be done in the DVD backup as reversing the process is difficult
and can cause problems with OCR software. Changing the Subtitle Transparency can also be
considered modifying the DVD backup, so it would no longer be untouched.

CSS Keys
~~~~~~~~

I recommend enabling the CSS Key Archive for both Read and Write. With the CSS Key Archive enabled,
you can look back to see if it had to guess a CSS Key by checking the value of "Substitute".

If it says "Substitute: Yes", then it was ultimately guessed and not actually cracked. That is
unsafe to be used. If this happens you should immediately discard that key from the CSS Key
Archive (Right Click -> Delete) and insert the disc into a matching region player.

Using AnyDVD HD
---------------

Backing up to ISO
~~~~~~~~~~~~~~~~~

.. thumbnail:: _static/images/anydvd-ripper-iso.webp
   :width: 300px
   :title: Example usage showing recommended settings for `.ISO` backups.

1. Right Click the AnyDVD HD Tray Icon in your Taskbar Tray area.
2. Click `Rip to Image...`.
3. Choose the disc reader with the disc you wish to Backup.
4. Specify where you wish to save the backup ISO file.
5. Choose your settings (these will be remembered next time). I recommend using the settings shown below.
6. Click `Copy Disc`.

Recommended Settings for ALL discs:

- ☐ Keep Protection (Blu-ray / HD DVD)
- ☑ Create additonal .dvd file
- ☐ Create Image File as a sparse file (saves harddisk space)

The ``Create additonal .dvd file`` option also creates a ``.dvdid.xml`` file for the ISO. The
``.dvd`` file itself is not strictly necessary as it describes physical attributes of the disc,
not the disc contents. But as to get the DVD ID file, we must tick it.

Backing up to a VIDEO_TS folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Right Click the AnyDVD HD Tray Icon in your Taskbar Tray area.
2. Click `Rip Video Disc to Harddisk...`.
3. Choose the disc reader with the disc you wish to Backup.
4. Specify where you wish to save the backup folder to.
5. Click `Copy Disc`.

Note: This method loses all ISO 9660 Information, that includes:

- Burned and Creation Date
- Application and Volume Identifier (i.e., the software used, and the Disc Label)
- Copyright Identifier (i.e., creator of the Disc ISO, usually the distributor)
- Publisher and Preparer Identifier (similar use to copyright identifier)

In the case of Pirate discs, it's common for common home burner software like
ImgBurn or Nero to appear in the ISO information.
