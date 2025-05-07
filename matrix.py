#!/usr/bin/env python3
import json

matrix = []

# 0.9.8 for Debian 11 and Ubuntu 22.04 only
for os in ["debian-11", "ubuntu-22.04"]:
    matrix.append({
        "version": "0.9.8",
        "stability": "oldstable",
        "os": os,
        "xmlrpc_c_version": "1.59.04",
        "xml_library": "xmlrpc-c",
        "libtorrent_version": "0.13.8",
        "libudns_version": "0.4.0",
        "dumptorrent_version": "1.3.0",
        "mktorrent_version": "1.1"
    })

# 0.10.0 for all 4 distros
for os in ["debian-11", "debian-12", "ubuntu-22.04", "ubuntu-24.04"]:
    matrix.append({
        "version": "0.10.0",
        "stability": "stable",
        "os": os,
        "xmlrpc_c_version": "1.64.01",
        "xml_library": "xmlrpc-c",
        "libtorrent_version": "0.14.0",
        "libudns_version": "0.5.0",
        "dumptorrent_version": "1.5.0",
        "mktorrent_version": "1.3.0"
    })

# 0.15.0, 0.15.1, 0.15.2, 0.15.3 for Debian 12 and Ubuntu 24.04 only
for version in ["0.15.0", "0.15.1", "0.15.2", "0.15.3"]:
    for os in ["debian-12", "ubuntu-24.04"]:
        if version in ["0.15.0", "0.15.1", "0.15.2"]:
            xmlrpc_c_version = "1.64.01" if version in ["0.15.0", "0.15.1"] else None
            xml_library = "xmlrpc-c" if version in ["0.15.0", "0.15.1"] else "tinyxml2"
            stability = "stable"
        else:
            xmlrpc_c_version = None
            xml_library = "tinyxml2" 
            stability = "next"
        matrix.append({
            "version": version,
            "stability": stability,
            "os": os,
            "xmlrpc_c_version": xmlrpc_c_version,
            "xml_library": xml_library,
            "libtorrent_version": version,
            "libudns_version": "0.6.0",
            "dumptorrent_version": "1.7.0",
            "mktorrent_version": "1.5.0"
        })

print(json.dumps({"include": matrix}, indent=2))
