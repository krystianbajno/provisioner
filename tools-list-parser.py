#!/usr/bin/python
import re
from collections import defaultdict
import yaml

NO_DIST_HDR = "NoDistribute"
CMP_DST_HDR = "CompiledToDistribute"
EXP_HDR = "Exploits"
UNDEFINED_CATEGORY = "UndefinedCategory"

# Reset
Color_Off='\033[0m'       # Text Reset

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

def make_config(md_text):
    title_pattern = re.compile(r'^#\s*(.*)')
    parsed_data = defaultdict(str)
    current_title = None
    current_content = ""

    lines = md_text.split('\n')
 
    for line in lines:
        title_match = title_pattern.match(line)
        if title_match:
            if current_title:
                parsed_data[current_title] += current_content
            current_title = title_match.group(1).strip()
            current_content = ""
        else:
            current_content += line + "\n"
    
    if current_title:
        parsed_data[current_title] = current_content
    
    return parsed_data

def metadata_factory(name, category, install_instructions, url):
    return {"name": name, "category": category, "install": install_instructions, "url": url}

def get_tool_metadata_from_config(installation_config, url):
    for category, tools in installation_config.items():
        for tool in tools:
            name = tool.get("name")
            install = tool.get("install")
            
            if name in url:
                return metadata_factory(name, category, None if not install else install, url)
            
    return metadata_factory(url.split("/")[-1], UNDEFINED_CATEGORY, None, url)

def provision_item(item):
    pass

if __name__ == "__main__":
    with open("list-of-tools-to-download.md") as toolsConf:
        config = make_config(toolsConf.read())
        
    provisioningConfigurations = {
        "no-distribute": config.get(NO_DIST_HDR),
        "compiled-to-distribute": config.get(CMP_DST_HDR),
        "exploits": config.get(EXP_HDR)  
    }
    
    InstallationConfig = yaml.safe_load(config.get("InstallationConfig"))
    
    for provisionKey, provisionValue in provisioningConfigurations.items():
        for item in provisionValue.split("\n"):
            if not item: continue
            
            tool_metadata = get_tool_metadata_from_config(InstallationConfig, item)
            category = tool_metadata.get("category")
            install_instructions = tool_metadata.get("install")
            url = tool_metadata.get("url")
            name = tool_metadata.get("name")
            
            print(f"{Green}[+] {name}{Color_Off}: {provisionKey} / {category} {Cyan}$ {install_instructions}{Color_Off} - {Blue}{url}{Color_Off}")
            provision_item(item)

