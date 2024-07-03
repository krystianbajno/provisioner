#!/usr/bin/python
import re
from collections import defaultdict
import yaml

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

def get_tool_metadata_from_config(installation_config, tool_url):
    for category, tools in installation_config.items():
        for tool in tools:
            if tool.get("name") in tool_url:
                return {"category": category, "install": tool.get("install")}
            
    return {"category": "UndefinedCategory", "install": None}

if __name__ == "__main__":
    with open("list-of-tools-to-download.md") as toolsConf:
        config = make_config(toolsConf.read())
        
    provisioningConfigurations = {
        "no-distribute": config.get("NoDistribute"),
        "compiled-to-distribute": config.get("CompiledToDistribute"),
        "exploits": config.get("Exploits")  
    }
    
    InstallationConfig = yaml.safe_load(config.get("InstallationConfig"))
    for provisionKey, provisionValue in provisioningConfigurations.items():
        for item in provisionValue.split("\n"):
            tool_metadata = get_tool_metadata_from_config(InstallationConfig, item)
            category = tool_metadata.get("category")
            install_instructions = tool_metadata.get("install")
            
            print(f"[+] {provisionKey} - {category}")
