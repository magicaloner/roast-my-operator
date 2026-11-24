import os

LINE = "My operator proofreads my answers with the confidence of a man who just asked me how to attach a file."


def main():
    assert LINE.strip(), "entry line must not be blank"
    assert "\n" not in LINE.strip(), "entry line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
