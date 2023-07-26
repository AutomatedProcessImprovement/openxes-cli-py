from pathlib import Path

from openxes_cli.lib import xes_to_csv

base_dir = Path(__file__).parent
jar_file = Path(__file__).parent.parent / "lib/openxes-cli.jar"


def xes_to_csv_manual_test():
    xes_path = base_dir / Path("assets/PurchasingExample.xes.gz")
    csv_path = xes_path.with_stem(xes_path.stem + "_converted").with_suffix(".csv")

    xes_to_csv(xes_path, csv_path, jar_file)


if __name__ == "__main__":
    xes_to_csv_manual_test()
