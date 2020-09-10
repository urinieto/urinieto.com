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


def replace_iframes(data):
    # These are likely youtube videos
    return re.sub(r'<iframe.*src="(.*/(.*))"\sf.*</iframe>', '[![](http://img.youtube.com/vi/\g<2>/0.jpg)](https://youtube.com/watch?v=\g<2>) ', data)


def update_file(in_file, out_file):
    # Read file
    with open(in_file, "r") as fn:
        data = fn.read()

    # Update file
    data = replace_smileys(data)
    data = replace_urinieto(data)
    data = replace_iframes(data)

    # Write file
    with open(out_file, "w") as fn:
        fn.write(data)


if __name__ == "__main__":
    in_dir = "../posts_old/"
    out_dir = "../urinieto.com/content/posts/"
    os.makedirs(out_dir, exist_ok=True)

    md_files = glob.glob(in_dir + "*.md")

    for md_file in tqdm(md_files):
        out_file = os.path.join(out_dir, os.path.basename(md_file))
        update_file(md_file, out_file)

