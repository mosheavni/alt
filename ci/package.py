#!/usr/bin/env python3
import subprocess
from os import path, makedirs
from shutil import copy, move
from argparse import ArgumentParser

def sh(*args):
    return subprocess.run(
        args,
        check=True,
        capture_output=True,
        text=True,
    )


def parse():
    parser = ArgumentParser()
    parser.add_argument('--alt-bin', required=True)
    parser.add_argument('--dest-dir', required=True)
    parser.add_argument('--rust-target', required=True)
    return parser.parse_args()


def main(
    alt_bin=None,
    dest_dir=None,
    rust_target=None,
):
    makedirs(dest_dir, exist_ok=True)
    dest_alt_bin = path.join(dest_dir, 'alt')
    copy(alt_bin, dest_alt_bin)

    version = sh(dest_alt_bin, '--version').stdout
    version = version.strip().split(' ')[1]

    gz_dir = path.join(dest_dir, 'gz-bin')
    makedirs(gz_dir, exist_ok=True)
    sh('gzip', '-fk9', dest_alt_bin)
    move(
        '{0}.gz'.format(dest_alt_bin),
        path.join(gz_dir, 'alt_v{0}_{1}.gz'.format(version, rust_target))
    )


if __name__ == "__main__":
    args = parse()
    main(**vars(args))