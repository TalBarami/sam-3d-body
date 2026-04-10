"""Minimal setup so that tools/ and notebook/ are importable after pip install -e .

The main sam_3d_body package already provides the core model code.  The tools/
and notebook/ directories are utility packages used by example scripts and
ASDHub wrappers — they need to be importable without sys.path manipulation.

Install (editable mode, run once):
    cd ~/PycharmProjects/sam-3d-body
    pip install -e .
"""
from setuptools import setup, find_packages

setup(
    name="sam-3d-body",
    version="0.1.0",
    packages=find_packages(),  # discovers sam_3d_body/, tools/, notebook/
)
