#!/usr/bin/python3
"""__init__ the method directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
