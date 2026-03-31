import subprocess
import tempfile
import os
from config import TIMEOUT


def run_code(code):
    filename = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
            f.write(code.encode())
            filename = f.name

        result = subprocess.run(
            ["python", filename],
            capture_output=True,
            text=True,
            timeout=TIMEOUT
        )

        return result.stdout, result.stderr

    except subprocess.TimeoutExpired:
        return "", "Execution timed out"

    except Exception as e:
        return "", str(e)

    finally:
        if filename and os.path.exists(filename):
            os.remove(filename)