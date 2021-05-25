import sys
import os
import subprocess
import glob
from pymediainfo import MediaInfo


CHANNEL_LAYOUT_MAP = {"LFE": 0.1}


def get_tracks(mediainfo, types):
    return [t for t in mediainfo.tracks if t.track_type in types]


def main():
    if len(sys.argv) <= 1:
        exit("gimme path bro python bla.py path")

    folder = sys.argv[1]
    print(f"Ok, setting up what I can automatically, make sure you follow #checklist still for every .mkv file in \"{folder}\", including all folders within")
    if (not os.path.exists(folder)):
        exit("which doesn't exist, what you talkin' bout willis??")

    global_tags = os.path.join(folder, "global_tags.xml")

    if not os.path.exists(global_tags) or not os.path.isfile(global_tags):
        exit(f"No global_tags.xml, this is needed, get them from https://pastebin.com/raw/Lq22AfkB, edit the values, and save to \"{global_tags}\"")

    for f in glob.glob(os.path.join(folder, "**/*.mkv"), recursive=True):
        
        filename = os.path.splitext(os.path.basename(f))[0]

        mediainfo = MediaInfo.parse(f)
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
            "-s", f"title={filename}"
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
        args.extend([f])

        mkvpropedit = subprocess.run(args, capture_output=True)
        if (mkvpropedit.returncode != 0):
            exit(f"Failed to mkvpropedit: {f}\nWhy? Not sure, here's the log:\n\n{mkvpropedit.stdout.decode()}")
        print(f"✓ : {filename}")

    print("✓✓✓ done all files")


if __name__ == "__main__":
    main()
