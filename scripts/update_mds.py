import argparse
import glob
import os
import re
from tqdm import tqdm


def replace_smileys(data):
    return re.sub(r'<img.*alt="(.*)".*class="wp-smiley".*/>', ' \g<1> ', data)


def replace_urinieto(data):
    data = re.sub(r'https://urinieto.com', '', data)
    data = re.sub(r'http://urinieto.com', '', data)
    return data


def replace_images(data):
    return re.sub(r'<img\s(.*?)\s/>', '{{< img \g<1> >}}', data)


def replace_iframes(data):
    # These are likely youtube videos
    return re.sub(r'<iframe.*src=".*/(.*?)["\?]',
                  '{{< youtube \g<1> >}}', data)


def add_thumbnail(data, alt="Thumbnail image"):
    def add_thumbnail_string(src, alt):
        thumb_str = f"thumbnail:\n  src: \"{src}\"\n  alt: {alt}\n"
        return data.replace("categories:", f"{thumb_str}categories:")

    # Try with youtube
    res = re.search(r'<iframe.*src=".*/(.*?)["\?]', data)
    if res and len(res.groups()) >= 1:
        src = f"https://img.youtube.com/vi/{res.groups()[0]}/0.jpg"
        return add_thumbnail_string(src, alt)

    # Try with img
    res = re.search(r'<img.*src="(.*?)"', data)
    if res and len(res.groups()) >= 1:
        return add_thumbnail_string(res.groups()[0], alt)

    # Else, do nothing
    return data


def update_file(in_file, out_file):
    print(in_file)
    # Read file
    with open(in_file, "r") as fn:
        data = fn.read()

    # Update file
    data = replace_smileys(data)
    data = add_thumbnail(data)  # Do this before replacing images but after replacing smileys
    data = replace_urinieto(data)
    data = replace_iframes(data)
    data = replace_images(data)

    # Write file
    with open(out_file, "w") as fn:
        fn.write(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parses MarkDown files for the Hugo site.')
    parser.add_argument('-i',
                        '--in_dir',
                        dest='in_dir',
                        type=str,
                        default='../posts_old/',
                        help='Input directory with Markdown files')
    parser.add_argument('-o'
                        '--out_dir',
                        dest='out_dir',
                        type=str,
                        default='../urinieto.com/content/posts/',
                        help='Output directory')

    args = parser.parse_args()
    in_dir = args.in_dir
    out_dir = args.out_dir
    os.makedirs(out_dir, exist_ok=True)

    md_files = glob.glob(in_dir + "*.md")

    for md_file in tqdm(sorted(md_files)):
        out_file = os.path.join(out_dir, os.path.basename(md_file))
        update_file(md_file, out_file)

