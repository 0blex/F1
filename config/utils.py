# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:50:28 2022

@author: alex.black
"""

from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parent.parent