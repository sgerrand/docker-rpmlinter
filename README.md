# RPM Linter

This is a Docker image for linting RPM packages.

## Usage

The linter is typically run from your RPM spec source directory:

    docker run -v "$PWD:/specs" sgerrand/rpmlinter

This would lint all the spec files in the current directory. You can run the
builder anywhere - you just need to mount your specs directory to `/specs`, but
this mount point can be changed using the `SPECSDIR` environment variable.

## Environment

There is currently two environment variables which can be changed at run time:

* `SPECSDIR`: Defaults to `/specs`. This specifies the mount point for your
  specs directory. If overridden, this mount point must exist for the linter
  script to work.
* `SPECFILE`: Defaults to an empty string. This specifies the location of a
  single spec file. The file can exist within the `SPECSDIR` directory or a
  separate location on the file system.
