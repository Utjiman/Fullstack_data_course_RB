from pathlib import Path
from enum import Enum

ROOT_PATH = Path(__file__).parents[1]
ENV_PATH = ROOT_PATH / ".env"
BACKEND_PATH = ROOT_PATH / "backend"
FRONTEND_PATH = ROOT_PATH / "frontend"

class StationIds(Enum):
    MALMO = 740000003
    GOTEBORG = 740000002
    UMEA = 740000190


