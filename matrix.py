#!/usr/bin/env python3
"""Pinned rTorrent versions (upstream git tags). CI does not track floating branches."""
import yaml

matrix = [
    {
        "version": "0.15.7",
        "os": "debian-13",
        "codename": "trixie",
        "xmlrpc_c_version": None,
        "xml_library": "tinyxml2",
        "libtorrent_version": "0.15.7",
        "libudns_version": "0.6.0",
        "dumptorrent_version": "1.7.0",
        "mktorrent_version": "1.5.0",
    },
    {
        "version": "0.16.11",
        "os": "debian-13",
        "codename": "trixie",
        "xmlrpc_c_version": None,
        "xml_library": "tinyxml2",
        "libtorrent_version": "0.16.11",
        "libudns_version": "0.6.0",
        "dumptorrent_version": "1.7.0",
        "mktorrent_version": "1.5.0",
    }
]

print(yaml.safe_dump({"include": matrix}, sort_keys=False))
