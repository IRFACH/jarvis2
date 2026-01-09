import os
import importlib
from skills.base import Skill

def load_skills():
    skills = {}
    for file in os.listdir("skills"):
        if file.endswith(".py") and file not in ["base.py", "__init__.py"]:
            module_name = f"skills.{file[:-3]}"
            module = importlib.import_module(module_name)

            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, Skill) and obj != Skill:
                    skills[file[:-3]] = obj()
    return skills
