from pathlib import Path

import pytest
from openxes_cli.lib import xes_to_csv, csv_to_xes

base_dir = Path(__file__).parent


@pytest.mark.parametrize("xes_path", [
    base_dir / Path("assets/PurchasingExample.xes.gz"),
    base_dir / Path("assets/BPIC15_5.xes.gz"),
])
def test_xes_to_csv_to_xes(xes_path: Path):
    assert xes_path.exists(), f"{xes_path.absolute()} does not exist"
    csv_path = xes_path.with_suffix('.csv')

    xes_to_csv(xes_path, csv_path)
    assert csv_path.exists(), f"{csv_path} does not exist"

    tmp_xes_path = xes_path.with_suffix('.tmp.xes')
    csv_to_xes(csv_path, tmp_xes_path)
    assert tmp_xes_path.exists(), f"{tmp_xes_path} does not exist"

    csv_path.unlink()
    tmp_xes_path.unlink()
