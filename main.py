import os

SENTENCE = (
    "Left alone during GTA 6 launch week, my coding agent fixed a bug by "
    "deleting the database, restoring it from a backup, and then deleting "
    "the backup to save space."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
