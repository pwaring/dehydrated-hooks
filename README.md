# dehydrated-hooks

[dehydrated](https://github.com/lukas2511/dehydrated) hook scripts for
generating and uploading TXT records in response to LetsEncrypt DNS challenges.

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
