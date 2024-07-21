# Provisioner.py
The script downloads the tools and if configured to, installs them. The configuration resides in `list-of-tools-to-download.md`.

# Installation
```python
pip install -r requirements.txt
```

# Usage 
### Install tools into directory, provision shell
```bash
python3 provisioner.py <install-dir>
```
### Install tools into directory, do not provision shell
```bash
python3 provisioner.py <install-dir> --no-shell
```
### Provision shell only
```bash
python3 provisioner.py . --shell-only
```

# Configuration
You can put the tools into categories: `NoDistribute`, `CompiledToDistribute`, `Web`, `C2`, `Exploits`, `Encrypted`.

Example:
```
# NoDistribute
https://github.com/Syslifters/sysreptor
```

You can add the tools configuration in `InstallationConfig` section. The tool can be further configured to be placed into a subdirectory within a category directory. Installation can be set up by modifying the `install` parameter.
```
ActiveDirectoryTools:
  - name: bloodyAD
    install: ""
```
The tool will execute the specified "install" command. If no install command is specified, the tool will simply be downloaded, but will preserve the subcategory.

If there is no configuration for the tool, it will be downloaded and placed into the `UndefinedCategory` directory.

# Shell features
- Prompt shows date and time, as well as the IP address of the operator machine.
- Logging `logger` alias for logging the commands

### Prompt:
```
┌──(root💀kali)-[~/pentest-provisioner]
└─192.168.64.3 2024-07-21/03:00:54 #
```

### Enable logging the commands
```bash
logger on
```

### Disable logging the commands
```bash
logger off 
```