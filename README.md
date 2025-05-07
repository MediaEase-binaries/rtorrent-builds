# rTorrent Builds

This repository provides automated build scripts for compiling the rTorrent BitTorrent client and creating Debian packages (.deb) for multiple Linux distributions. All builds are automated via GitHub Actions and are available in the GitHub Releases section.

## Features

- Automated builds via GitHub Actions
- Debian packages that install rTorrent in `/opt/MediaEase/.binaries/installed/rtorrent-${STABILITY}_${VERSION}`
- Support for multiple Linux distributions:
  - Debian 11 (Bullseye)
  - Debian 12 (Bookworm)
  - Ubuntu 22.04 LTS
  - Ubuntu 24.04 LTS
- Multiple version support with different stability levels:
  - Oldstable (0.9.8)
  - Stable (0.10.0, 0.15.0, 0.15.1, 0.15.2)
  - Next (0.15.3)
- XMLRPC and TinyXML2 support
- Automated metadata generation
- Package signing and verification

## Supported Versions & Distributions

| Version    | Stability  | Debian 11 | Debian 12 | Ubuntu 22.04 | Ubuntu 24.04 |
|------------|------------|-----------|-----------|--------------|--------------|
| 0.15.3     | next       |     ✘     |     ✔     |      ✘       |      ✔       |
| 0.15.2     | stable     |     ✘     |     ✔     |      ✘       |      ✔       |
| 0.15.1     | stable     |     ✘     |     ✔     |      ✘       |      ✔       |
| 0.15.0     | stable     |     ✘     |     ✔     |      ✘       |      ✔       |
| 0.10.0     | stable     |     ✔     |     ✔     |      ✔       |      ✔       |
| 0.9.8      | oldstable  |     ✔     |     ✘     |      ✔       |      ✘       |

## Build Process

The build process is fully automated and includes:
1. Environment setup with all required dependencies
2. Download and compilation of rTorrent
3. Static linking of all components
4. Creation of Debian packages
5. Generation of JSON metadata
6. Package signing and verification
7. Automated release creation

## Available Packages

Packages are available in the GitHub Releases of this repository. Each release includes:
- A `.deb` file installable with `dpkg -i`
- A `.json` file containing package metadata
- Documentation and changelog
- Package signatures

### Package Structure

The Debian package installs rTorrent in a dedicated directory structure:
- Base installation path: `/opt/MediaEase/.binaries/installed/rtorrent-${STABILITY}_${VERSION}`
- Binaries in `/opt/MediaEase/.binaries/installed/rtorrent-${STABILITY}_${VERSION}/usr/bin`
- Libraries in `/opt/MediaEase/.binaries/installed/rtorrent-${STABILITY}_${VERSION}/usr/lib`
- Documentation in `/opt/MediaEase/.binaries/installed/rtorrent-${STABILITY}_${VERSION}/usr/share/doc/rtorrent`

The package uses Debian alternatives to manage the binaries, making them available in the system PATH.

## Installation

### Manual Installation
1. Download the appropriate .deb package for your distribution from the [GitHub Releases](../../releases)
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

### Automated Installation
The packages can be installed automatically using the JSON metadata and package management tools.

## Build Configuration

The build process is configured through:
- `build.yaml`: GitHub Actions workflow configuration
- `matrix.py`: Build matrix configuration for different versions and distributions

## Contributing

Contributions are welcome! Please open issues or pull requests for bug fixes, new features, or improvements.

## Support

For questions, issues, or support, please use the GitHub Issues section of this repository.

## License

This repository is licensed under the terms specified in the LICENSE file.

rTorrent is distributed under the terms of the [GNU General Public License v2](https://www.gnu.org/licenses/gpl-2.0.html) or later. 
