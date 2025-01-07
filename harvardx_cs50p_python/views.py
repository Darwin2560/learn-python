import csv

import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r", encoding="utf-8") as views, open(
        "analysis.csv", "w", encoding="utf-8", newline=""
    ) as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(
            analysis, fieldnames=reader.fieldnames + ["brightness"]
        )  # noqa
        writer.writeheader()

        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpg")
            writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2),
                }
            )


def calculate_brightness(filename):
    with Image.open(filename) as img:
        brightness = np.mean(np.array(img.convert("L"))) / 255
    return brightness


main()
