# rTorrent Builds

This repository provides build scripts for compiling the rTorrent BitTorrent client and creating Debian packages (.deb). Packages are produced when the GitHub Actions workflow is run manually; published artifacts appear under **Releases**.

## GitHub Actions

Workflow `.github/workflows/build.yaml` runs **only** on **`workflow_dispatch`**. Pushes to `main` do **not** trigger builds (including changes to `matrix.py`) — use **Actions** → run workflow → choose **`all`** or a specific version.

## Features

- Builds via GitHub Actions (manual trigger)
- Debian packages that install rTorrent in `/opt/Krate/vendor/rtorrent_${VERSION}`
- CI uses a **single reference image** (see `matrix.py`); **one published package per** rTorrent **version**, intended for recent **Debian and Ubuntu** on **amd64**
- Version matrix: pinned upstream **tags only** — **`0.15.7`** and **`0.16.11`** (see `matrix.py`)
- XMLRPC and TinyXML2 support
- Automated metadata generation
- Package signing and verification

## Supported Versions

The CI matrix builds **tagged releases only**; it does not multiply distributions—the same `.deb` is provided for Debian/Ubuntu use.

| Version (upstream tag) | Notes    |
| ---------------------- | -------- |
| 0.15.7                 | TinyXML2 |
| 0.16.11                | TinyXML2 |

For local experiments against moving upstream branches, you can still set **`LT_GIT_REF`** and **`RT_GIT_REF`** before `build.sh` (defaults follow the tagged checkout used in CI).

## Build Process

When you start the workflow, the job sequence includes:
1. Environment setup with all required dependencies
2. Download and compilation of rTorrent
3. Static linking of all components
4. Creation of Debian packages
5. Generation of JSON metadata
6. Package signing and verification
7. Create or update the GitHub Release (when the workflow completes successfully)

## Available Packages

Packages are available in the GitHub Releases of this repository. Each release includes:
- A `.deb` file installable with `dpkg -i`
- A `.json` file containing package metadata
- Documentation and changelog
- Package signatures

### Package Structure

The Debian package installs rTorrent in a dedicated directory structure:
- Base installation path: `/opt/Krate/vendor/rtorrent_${VERSION}`
- Binaries in `/opt/Krate/vendor/rtorrent_${VERSION}/usr/bin`
- Libraries in `/opt/Krate/vendor/rtorrent_${VERSION}/usr/lib`
- Documentation in `/opt/Krate/vendor/rtorrent_${VERSION}/usr/share/doc/rtorrent`

The package uses Debian alternatives to manage the binaries, making them available in the system PATH.

## Installation

### Manual Installation
1. Download the `.deb` for your target rTorrent version from the [GitHub Releases](../../releases)
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

### Automated Installation
The packages can be installed automatically using the JSON metadata and package management tools.

## Build Configuration

The build process is configured through:
- `build.yaml`: GitHub Actions workflow configuration
- `matrix.py`: Build matrix configuration for upstream versions (single reference OS in CI)

## Contributing

Contributions are welcome! Please open issues or pull requests for bug fixes, new features, or improvements.

## Support

For questions, issues, or support, please use the GitHub Issues section of this repository.

## License

This repository is licensed under the terms specified in the LICENSE file.

rTorrent is distributed under the terms of the [GNU General Public License v2](https://www.gnu.org/licenses/gpl-2.0.html) or later. 
