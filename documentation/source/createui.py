from js import document
version = "0.1-alpha"
version_label = document.querySelector("span#aptfile-version")
version_label.textContent = f"Using Aptfile {version}"
