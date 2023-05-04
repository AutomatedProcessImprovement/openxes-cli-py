import logging
import os

from pathlib import Path

logging.basicConfig(level=logging.INFO)

jar_file = Path(__file__).parent.parent / "lib/openxes-cli.jar"


def xes_to_csv(xes_path: Path, csv_path: Path, jar_file: Path = jar_file):
    """
    Converts XES to CSV using openxes-cli.jar. Java 8 is required.

    :param xes_path: Event log in XES format either with the .xes or .xes.gz extension.
    :param csv_path: Output path for the CSV file.
    :param jar_file: Path to the openxes-cli.jar file. Default: lib/openxes-cli.jar.
    :return: Exit code of the Java process.
    """
    return run_jar(jar_file, "-f", str(xes_path), "-t", "csv", "-o", str(csv_path))


def csv_to_xes(csv_path: Path, xes_path: Path, jar_file: Path = jar_file):
    """
    Converts CSV to XES using openxes-cli.jar. Java 8 is required.

    :param csv_path: Event log in CSV format.
    :param xes_path: Output path for the XES file.
    :return: Exit code of the Java process.
    """
    return run_jar(jar_file, "-f", str(csv_path), "-t", "xes", "-o", str(xes_path))


def run_jar(jar_file: Path, *args) -> int:
    cmd = f"java -jar {str(jar_file)} {' '.join(args)}"
    logging.info("Running", cmd)
    return os.system(cmd)
