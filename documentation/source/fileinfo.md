---
py-config:
  splashscreen:
    autoclose: true
  packages:
  - toml
---

# Aptfile info
This utility lets you show information about an Aptfile in a human-readable format.
It is compatible with the latest version of the Aptfile specification.

```{py-script}
:file: aptfile_describer.py
```

<form method="post">
    <label for="input_text" style="display: block">Write or paste an Aptfile:</label>
    <textarea id="input_text" name="input_text" style="width: 90%">
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
# An array of dependent packages.
depends = ["python3", "python3-pip"]
# Recommended packages.
recommends = ["python3-tk"]</textarea>
</form>
