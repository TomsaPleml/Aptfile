from js import document
version = "0.1-alpha"
version_label = document.querySelector("span#aptfile-version")
toml_code = document.querySelector("span#toml")
version_label.textContent = f"Using Aptfile {version}"
toml_code.textContent = f"Aptfile {version} generator test."
