if __name__ == "__main__":
    import sys

    print("cli not implemented", file=sys.stderr)
    exit(1)


def run(
    folder: str,
    exts: list[str] = ["*.qmd"],
    lbl_num="\#",
    lbl_name="Nome do arquivo",
    lbl_link="Link",
) -> list[str]:
    import glob
    from scripts.util import relpath

    globs = [glob.glob(f"{folder}/{ext}") for ext in exts]
    files = sorted([f for gs in globs for f in gs if "index" not in f])

    if not len(files) > 0:
        return []

    out = [f"| {lbl_num} | {lbl_name} | {lbl_link} |", "| --- | --- | --- |"]
    for i, file in enumerate(files, start=1):
        path = relpath(file, folder, to_path=True)
        out.append(f"| {i} | {path.stem} | [Ver {path}]({path}) |")

    return out
