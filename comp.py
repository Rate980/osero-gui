from base64 import encode
import jinja2 as j2
from pathlib import Path
import glob


prefix = Path(__file__).resolve().parent
SRC_DIR = prefix.joinpath("src")
DIST_DIR = prefix.joinpath("dist")

env = j2.Environment(loader=j2.FileSystemLoader(str(SRC_DIR.joinpath("j2")), encoding='utf8'))


def main():
    j2_files = [x.replace('\\', '/').removeprefix('./') for x in glob.glob(
        './**/*.j2',
        root_dir=SRC_DIR.joinpath("j2"),
        recursive=True
    )]

    for j2_file in j2_files:
        # print(j2_file.name)
        tmpl = env.get_template(j2_file)

        out = DIST_DIR.joinpath(j2_file.removesuffix('.j2'))
        out.write_text(tmpl.render())


if __name__ == "__main__":
    main()
