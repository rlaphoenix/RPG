import sys
import subprocess
import glob
from pathlib import Path
from pymediainfo import MediaInfo


CHANNEL_LAYOUT_MAP = {"LFE": 0.1}


def get_tracks(mediainfo, types):
    return [t for t in mediainfo.tracks if t.track_type in types]


def main():
    if len(sys.argv) <= 1:
        exit("Usage: prep.py [DIRECTORY]")
    if len(sys.argv) > 2:
        exit("Error: You provided too much arguments %s, expecting only one." % sys.argv[1:])

    folder = Path(sys.argv[1])

    if not folder.exists():
        exit("Error: The directory you provided (%s) does not exist." % folder)

    print("Ok, setting up what I can automatically.")
    print("You still need to follow the handbook. This script cannot cover every single thing.")
    print("There's various stuff a script simply cannot do automatically.")

    global_tags = folder / "global_tags.xml"

    if not global_tags.exists():
        exit(
            "No global_tags.xml, this is needed, get an example from https://pastebin.com/raw/Lq22AfkB, "
            f"edit the values, and save it to: {global_tags}"
        )

    for file in glob.glob(folder / "**/*.mkv", recursive=True):
        mediainfo = MediaInfo.parse(file)
        video_tracks = get_tracks(mediainfo, ["Video"])
        if not video_tracks:
            exit("no video tracks? the fuck?")
        audio_tracks = get_tracks(mediainfo, ["Audio"])
        if not video_tracks:
            exit("no audio tracks? the fuck?")
        sub_tracks = get_tracks(mediainfo, ["Text"])

        args = [
            "mkvpropedit",
            # tags
            "-t", f"global:{global_tags}",
            # general
            "-e", "info",
            "-s", f"title={file.stem}"
        ]
        for track in video_tracks:
            args.extend([
                "-e", f"track:{track.track_id}",
                "-s", "flag-enabled=1",
                "-s", f"flag-default={'1' if int(track.stream_identifier) == 0 else '0'}",
                "-s", "flag-forced=0",
                "-s", "name=",
                "-s", f"language={audio_tracks[0].language}",
            ])
        for track in audio_tracks:
            channels = sum(CHANNEL_LAYOUT_MAP.get(x, 1) for x in track.channel_layout.split(" "))
            title = f"{track.format} {float(channels)}"
            if not audio_tracks[0].language == track.language:
                title += ", different lang, is this wanted?"
            if int(track.stream_identifier) > 0:
                title += ", not first audio, is this commentary?"
            args.extend([
                "-e", f"track:{track.track_id}",
                "-s", "flag-enabled=1",
                "-s", f"flag-default={'1' if int(track.stream_identifier) == 0 else '0'}",
                "-s", "flag-forced=0",
                "-s", f"name={title}",
            ])
        for track in sub_tracks:
            if track.language:
                title = track.other_language[0]
                if not sub_tracks[0].language == track.language:
                    title += ", different lang, is this wanted?"
                if len([x for x in sub_tracks if x.language == track.language and x.codec_id == track.codec_id]) > 1:
                    title += " (Dialect? Forced?)"
            else:
                title = "Undefined???"
            title += f" ({'CC' if track.codec_id == 'S_TEXT/UTF8' else 'type'}?)"
            args.extend([
                "-e", f"track:{track.track_id}",
                "-s", "flag-enabled=1",
                "-s", "flag-default=0",
                "-s", "flag-forced=0",
                "-s", f"name={title}"
            ])
        args.extend([file])

        mkvpropedit = subprocess.run(args, capture_output=True)
        if (mkvpropedit.returncode != 0):
            exit(f"Failed to mkvpropedit: {file}\nWhy? Not sure, here's the log:\n\n{mkvpropedit.stdout.decode()}")
        print(f"✓ : {file.name}")

    print("✓✓✓ done all files")


if __name__ == "__main__":
    main()
