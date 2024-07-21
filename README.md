# Provisioner.py
This script downloads and installs tools based on configurations provided in list-of-tools-to-download.md.

# Installation
```python
pip install -r requirements.txt
```

# Usage 
### Install tools into a directory and provision the shell
```bash
python3 provisioner.py <install-dir>
```
### Install tools into a directory without provisioning the shell
```bash
python3 provisioner.py <install-dir> --no-shell
```
### Provision the shell only
```bash
python3 provisioner.py . --shell-only
```

# Configuration
You can categorize the tools into: `NoDistribute`, `CompiledToDistribute`, `Web`, `C2`, `Exploits`, and `Encrypted`.

Example:
```
# NoDistribute
https://github.com/Syslifters/sysreptor
```

### Tools Configuration
You can further configure tools in the `InstallationConfig` section. Tools can be placed into subdirectories within a category directory and configured for installation by modifying the `install` parameter.
```
ActiveDirectoryTools:
  - name: bloodyAD
    install: ""
```
The tool will execute the specified `install` command. If no install command is provided, the tool will simply be downloaded and placed into the appropriate subcategory.

If a tool is not configured, it will be downloaded and placed in the UndefinedCategory directory.

# Shell features
- The prompt displays the date, time, and the IP address of the operator's machine.
- Use the `logger` alias to enable or disable command logging.

### Prompt example:
```
┌──(root💀kali)-[~/pentest-provisioner]
└─192.168.64.3 2024-07-21/03:00:54 #
```

### Enable Command Logging
```bash
logger on
```

### Disable Command Logging
```bash
logger off 
```