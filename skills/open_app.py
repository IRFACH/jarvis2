import subprocess
from skills.base import Skill
from core.permissions import has_permission

APP_MAP = {
    "whatsapp": "com.whatsapp",
    "youtube": "com.google.android.youtube",
    "chrome": "com.android.chrome"
}

class OpenApp(Skill):
    def execute(self, data):
        app = data.get("intent", "").lower()

        for name, package in APP_MAP.items():
            if name in app:
                if not has_permission("open_app"):
                    return

                subprocess.run([
                    "termux-open-app",
                    package
                ])
