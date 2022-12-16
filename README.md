# Aptfile

An Aptfile is a file specifying Debian package requirements for a whole single project.
It works by looking at the Aptfile, downloading the packages, installing them, and then
installing dependenices. This process is otherwise known as "DID".

## Motivation

APT is dependency hell. Dependency hell is when one of the dependencies are outside release
cycle. This can break apps, especially when they get older and older while dependencies get
newer and newer while causing breaking changes. Aptfiles install every dependencies with
one command, while following release cycle.

Also, APT packages are harder to be used by GUI app stores, like GNOME Software and KDE
Discover. Aptfiles solve that, by containing information about the package in a single
file.

## Format

Aptfiles are written in [TOML](https://toml.io/en/) format. You can write an Aptfile like this:

```toml
# Aptfile for hello-world

[aptfile]
# Main Aptfile data.
target = 1.0

[humanfriendly.info]
# This is designed to be read by appstores. Without it, you should NOT list your app on Linux
# app stores, and you should NOT recommend your app to non-developers. It's called "humanfriendly"
# because plain "package names" are made for experienced users and even "robots".
name = "Hello World"
description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
version = "1.0"

[apt.dependencies]
# dependencies is freeform. Any package can go in as a value. You can define just the major number,
# the major and minor number, or even all 3 numbers (major, minor, and patch). It is recommended to
# use the major and minor number. This example demonstrates requiring Python 3.9 or newer to run the
# program, including Cython. Written in pip format or "latest".
python3 = 3.9
cython3 = "latest"
```

This is not a full list of Aptfile data values. See [the guidelines](https://tylerms887.github.io/aptfile)
for a (mostly) complete list.
