from typing import NamedTuple
from argparse import ArgumentParser
from os import walk, path, makedirs
from logging import getLogger, basicConfig
from shutil import copy2 as copy

from .clock import HighPrecisionClock
from .file_hasher import Sha256FileHasher
from .deduplicator import DeduplicatorImpl


class Arguments(NamedTuple):
    input_dir: str
    output_dir: str
    log_level: str

    @staticmethod
    def parse():
        ap = ArgumentParser()
        ap.add_argument("indir", help="Name of the input directory", type=str)
        ap.add_argument("outdir", help="Name of the output directory", type=str)
        ap.add_argument("--log-level", default="INFO", choices={"DEBUG", "INFO", "CRITICAL", "ERROR"})
        opts = ap.parse_args()
        print(opts)
        return Arguments(
            input_dir=opts.indir,
            output_dir=opts.outdir,
            log_level=opts.log_level,
        )


def main(opts: Arguments):

    basicConfig(level=opts.log_level)

    log = getLogger("main")
    hasher = Sha256FileHasher(HighPrecisionClock(), getLogger("file-hasher"))
    finder = DeduplicatorImpl(hasher, HighPrecisionClock(), getLogger("finder"))
    files = iterate_files(opts.input_dir)

    for file in finder.collect_files(files):
        rel = path.relpath(file, opts.input_dir)
        target = path.join(opts.output_dir, rel)
        makedirs(path.dirname(target), exist_ok=True)
        copy(file, target)

    print("success")


def iterate_files(root_path):
    ret = []
    for root, _, files in walk(root_path):
        for file in files:
            ret.append(path.join(root, file))
    return ret


if __name__ == "__main__":
    opts = Arguments.parse()
    main(opts)

