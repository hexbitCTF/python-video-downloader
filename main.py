import argparse
import yt_dlp
import os


def download_video(url, resolution, output_path):
    # Make sure the download directory exists
    os.makedirs(output_path, exist_ok=True)

    # Output options: truncate title length, restrict to safe characters
    ydl_opts = {
        "outtmpl": os.path.join(output_path, "%(title).100s.%(ext)s"),
        "restrictfilenames": True,
    }

    # Resolution handling
    if resolution == "max":
        # Best available video+audio in MP4
        ydl_opts["format"] = "best[ext=mp4]/best"
    else:
        res = resolution.lower().replace("p", "")
        ydl_opts["format"] = (
            f"bestvideo[height<={res}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
        )

    # Try download
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except OSError:
        # Fallback: save with video ID instead of title
        fallback_opts = ydl_opts.copy()
        fallback_opts["outtmpl"] = os.path.join(output_path, "%(id)s.%(ext)s")
        with yt_dlp.YoutubeDL(fallback_opts) as ydl:
            ydl.download([url])


def main():
    parser = argparse.ArgumentParser(description="Universal Video Downloader")
    parser.add_argument("-u", "--url", required=True, help="Video URL")
    parser.add_argument(
        "-r", "--resolution", default="max", help="Resolution (e.g., 720p, 1080p, max)"
    )
    parser.add_argument(
        "-o", "--output", default="downloads", help="Download folder path"
    )

    args = parser.parse_args()

    print(
        f"Downloading {args.url} at {args.resolution} into {os.path.abspath(args.output)}..."
    )
    download_video(args.url, args.resolution, args.output)


if __name__ == "__main__":
    main()
