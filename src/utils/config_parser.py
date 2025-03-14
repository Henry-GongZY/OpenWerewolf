import json
from typing import Dict, Any

def load_config(config_path: str) -> Dict[str, Any]:
    """
    加载配置文件。

    Args:
        config_path: 配置文件的路径。

    Returns:
        配置文件的内容，以字典形式返回。
    """
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print(f"Error: Config file not found at {config_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {config_path}")
        return {}
