---
title: What is an Aptfile?
---

Aptfile is an exit from dependency hell. Aptfile can also solve issues on other APT-based
OSes, e.g. Ubuntu, Kali, Mint, and others.

Also, GUI appstores don't understand APT, so Aptfiles can also contain app information including
the description of it.

## How it works

Aptfile works in a different order from normal APT. APT downloads first, installs dependencies
first and then installs the real software. Aptfiles do it by downloading packages, installing them,
and then installing dependencies. Aptfile is a simple replacement for the traditional `Depends` option
in `deb` files.

## Example

Aptfiles are written in **TOML** so a basic Aptfile could look like this:

```toml
[aptfile]
target = 1.0

[humanfriendly.info]
name = "Hello World"
description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
version = "1.0"

[apt.dependencies]
python3 = 3.9
cython3 = "latest"
```

Not all of the Aptfile language is shown in this example. Read these guidelines for a complete
list.
