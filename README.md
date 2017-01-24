# dehydrated-hooks

Hook scripts for using [dehydrated](https://github.com/lukas2511/dehydrated)
to generate and upload TXT records which can be used to respond to DNS
challenges for LetsEncrypt certificate issuance.

## Dependencies

 * Python 3.x. The hook scripts will not work in Python 2.x. This is a feature,
 not a bug.
 * `dnspython`: Package `python3-dnspython` in Ubuntu.

## Usage

To use these scripts, run `dehydrated` as normal with the following additional
command line arguments:

 * `--hook /path/to/hook.py`
 * `--challenge dns-01`

Choose the appropriate hook script for your DNS provider.
