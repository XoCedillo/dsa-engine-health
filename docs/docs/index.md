# engine_health documentation!

## Description

ML project to predict the health of engines

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://engine_data/data/`.
* `make sync_data_down` will use `aws s3 sync` to recursively sync files from `s3://engine_data/data/` to `data/`.


