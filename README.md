# CInfo

Gather, filter and publish information on CI.

#### ...but it's not ready! :'(

## Installation

```
virtualenv ~/.cinfo_venv && source ~/.cinfo_venv/bin/activate
git clone git@github.com:rhos-infra/cinfo.git
cd cinfo
pipenv install .
```

## Configuration file

The path of the configuration file should be `~/.cinfo/cinfo.yaml`

```
environments:
  'OSP Phase 1':
    jobs: 'phase1-*'
    sources:
      - some_elk:
          driver: elk
          URL: 'http://..."
      - some_jenkins:
          driver: jenkins
          URL: 'http://..."
  'Tripleo CI':
    sources:
      - internal_zuul:
          URL: 'haha'
```

The hierarchy is `environment -> source -> driver` while the driver name must match the drivers CInfo supports. Everything else can be named freely.<br>
Users may limit environments to specific set of jobs by using the `jobs:` directive. The value provided to it, used as regex. This way, one environment can be split into multiple environments.

## Usage

Don't try to use it...told you, it's not ready :'(

* List CI environments: `cinfo query`
* List jobs in all CI environments: `cinfo query --jobs`
* List jobs in one specific CI environment: `cinfo query --env tripleo_ci` (can also be `--env 'tripleo ci`)
* List all the jobs that use the feature `overcloud-ssl`: `cinfo query --jobs --feature overcloud-ssl`
