if __name__ == "__main__":
    import sys

    print("cli not implemented", file=sys.stderr)
    exit(1)


def run(
    glob_list: list[str] = ["*.qmd"],
    folder: str = None,
    lbl_num="\#",
    lbl_name="Título",
    lbl_link="Link",
) -> list[str]:
    import os
    import glob
    import json
    import frontmatter
    from scripts.util import relpath

    if folder is None:
        folder = os.environ["QUARTO_DOCUMENT_PATH"]

    globs = [glob.glob(f"{folder}/{ext}") for ext in glob_list]
    files = sorted([f for gs in globs for f in gs if "index" not in f])

    if not len(files) > 0:
        return []

    out = [f"| {lbl_num} | {lbl_name} | {lbl_link} |", "| --: | --- | --- |"]
    for i, file in enumerate(files, start=1):
        rpath = relpath(file, folder, to_path=True)
        ppath = relpath(file, os.environ["QUARTO_PROJECT_ROOT"], to_path=True)

        meta = {}
        if ppath.suffix == ".ipynb":
            with open(ppath) as fd:
                ipynb = json.load(fd)
                source = "".join(ipynb["cells"][0]["source"])
                meta, _ = frontmatter.parse(source)
        else:
            with open(ppath) as fd:
                meta, _ = frontmatter.parse(fd.read())

        title = meta.get("title", rpath.stem)
        out.append(f"| {i} | {title} | [Ir para {rpath.name}]({rpath}) |")

    return out
