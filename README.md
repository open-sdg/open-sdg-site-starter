# Open SDG - Site - Armenia

This is the site repository for the Armenian implementation of Open SDG.

## Adding new indicators

A helper script is available to add new indicators. To use it, execute the script
with Python from the root of the repository. Here is an example:

`py scripts/batch/add_indicator 1.2.z "Title of indicator"`

This will create a new "1.2.z" indicator called "Title of indicator".

> This script requires the `pyyaml` package. Here is the command to install
> this package:
>
> `py -m pip install pyyaml`

Note that you will still need to add/commit/push these files with Git.

Finally, the next step is to perform the same steps in the other repository (if
you have not already).

## Google Analytics

The UA code for Google Analytics can be set, for the production site, in the
`_config_prod.yml` file.

## Production deployments

To start a production deployment, merge the `develop` branch into `master`. You
can do this in Github.com by creating a new pull-request. The steps are:

1. Click "New pull request"
2. Set "base: master" and "compare: develop"
3. Click "Create pull request"
