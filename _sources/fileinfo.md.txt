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
    <textarea id="input_text" name="input_text" style="width: 90%"></textarea>
</form>

```{tab} App Store
Appstore
```
```{tab} Dependencies
Dependencies
```
```{tab} Compatibility
Compatibility
```
