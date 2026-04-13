#!/usr/bin/env sh
set -eu

REPO_URL="${SUPLEX_REPO_URL:-https://github.com/ValentinGuigon/SUPLEX-agentic-workflow}"
REF="${SUPLEX_REF:-main}"
SOURCE_ROOT="${SUPLEX_SOURCE_ROOT:-}"
TARGET_DIR="$(pwd)"
TEMP_ROOT=""
ATTEMPTED_INTERPRETERS="python3, python"

cleanup() {
  if [ -n "${TEMP_ROOT}" ] && [ -d "${TEMP_ROOT}" ]; then
    rm -rf "${TEMP_ROOT}"
  fi
}

trap cleanup EXIT INT TERM

is_usable_python3() {
  if ! command -v "$1" >/dev/null 2>&1; then
    return 1
  fi

  "$1" -c 'import sys; raise SystemExit(0 if sys.version_info[0] == 3 else 1)' >/dev/null 2>&1
}

if [ -z "${SOURCE_ROOT}" ]; then
  TEMP_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/suplex-bootstrap.XXXXXX")"
  ARCHIVE_URL="$(printf '%s' "${REPO_URL}" | sed 's/\.git$//')/archive/refs/heads/${REF}.zip"
  ARCHIVE_PATH="${TEMP_ROOT}/suplex-template.zip"
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "${ARCHIVE_URL}" -o "${ARCHIVE_PATH}"
  elif command -v wget >/dev/null 2>&1; then
    wget -qO "${ARCHIVE_PATH}" "${ARCHIVE_URL}"
  else
    echo "SUPLEX bootstrap failed: curl or wget is required." >&2
    exit 1
  fi
  unzip -q "${ARCHIVE_PATH}" -d "${TEMP_ROOT}"
  SOURCE_ROOT="$(find "${TEMP_ROOT}" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
fi

if is_usable_python3 python3; then
  PYTHON_BIN="python3"
elif is_usable_python3 python; then
  PYTHON_BIN="python"
else
  echo "SUPLEX bootstrap failed: Python 3 is required. Attempted interpreters: ${ATTEMPTED_INTERPRETERS}. Install Python 3 and ensure either 'python3' or 'python' runs Python 3, then rerun the bootstrap." >&2
  exit 1
fi

"${PYTHON_BIN}" "${SOURCE_ROOT}/bootstrap/init_suplex.py" --target-dir "${TARGET_DIR}" --source-root "${SOURCE_ROOT}" --repo-url "${REPO_URL}" --ref "${REF}"
