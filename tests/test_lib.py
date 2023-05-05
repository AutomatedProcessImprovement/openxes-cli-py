from pathlib import Path

import pandas as pd
import pytest
from openxes_cli.lib import xes_to_csv, csv_to_xes

base_dir = Path(__file__).parent
jar_file = Path(__file__).parent.parent / "lib/openxes-cli.jar"


@pytest.mark.parametrize(
    "xes_path",
    [
        base_dir / Path("assets/PurchasingExample.xes.gz"),
        base_dir / Path("assets/BPIC15_5.xes.gz"),
    ],
)
def test_xes_to_csv_to_xes(xes_path: Path):
    assert xes_path.exists(), f"{xes_path.absolute()} does not exist"
    csv_path = xes_path.with_suffix(".csv")

    xes_to_csv(xes_path, csv_path, jar_file)
    assert csv_path.exists(), f"{csv_path} does not exist"

    tmp_xes_path = xes_path.with_suffix(".tmp.xes")
    csv_to_xes(csv_path, tmp_xes_path, jar_file)
    assert tmp_xes_path.exists(), f"{tmp_xes_path} does not exist"

    csv_path.unlink()
    tmp_xes_path.unlink()


@pytest.mark.parametrize(
    "csv_path",
    [
        base_dir / Path("assets/Production.csv"),
    ],
)
def test_csv_to_xes_to_csv(csv_path: Path):
    assert csv_path.exists(), f"{csv_path.absolute()} does not exist"

    generated_xes_path = csv_path.with_suffix(".generated.xes")
    generated_csv_path = csv_path.with_suffix(".generated.csv")

    csv_to_xes(csv_path, generated_xes_path, jar_file)
    assert generated_xes_path.exists(), f"{generated_xes_path} does not exist"

    xes_to_csv(generated_xes_path, generated_csv_path, jar_file)
    assert generated_csv_path.exists(), f"{generated_csv_path} does not exist"

    df_expected = pd.read_csv(csv_path).sort_values(
        [
            "case:concept:name",
            "concept:name",
            "org:resource",
            "start_timestamp",
            "time:timestamp",
        ],
        ignore_index=True,
    )
    df_converted = pd.read_csv(generated_csv_path).sort_values(
        [
            "case:concept:name",
            "concept:name",
            "org:resource",
            "start_timestamp",
            "time:timestamp",
        ],
        ignore_index=True,
    )

    pd.testing.assert_frame_equal(df_expected, df_converted)

    generated_xes_path.unlink()
    generated_csv_path.unlink()
