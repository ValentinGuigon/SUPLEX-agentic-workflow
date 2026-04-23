#!/usr/bin/env sh
set -eu

REPO_URL="${SUPLEX_REPO_URL:-https://github.com/ValentinGuigon/SUPLEX-agentic-workflow}"
REF="${SUPLEX_REF:-main}"
SOURCE_ROOT="${SUPLEX_SOURCE_ROOT:-}"
WORKFLOW_MODE="${SUPLEX_WORKFLOW_MODE:-standard}"
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

download_to_file() {
  uri="$1"
  destination="$2"
  parent_dir="$(dirname "${destination}")"
  mkdir -p "${parent_dir}"
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "${uri}" -o "${destination}"
  elif command -v wget >/dev/null 2>&1; then
    wget -qO "${destination}" "${uri}"
  else
    echo "SUPLEX bootstrap failed: curl or wget is required." >&2
    return 1
  fi
}

derive_raw_base_url() {
  repo_url="$1"
  ref="$2"
  case "${repo_url}" in
    https://github.com/*)
      trimmed="$(printf '%s' "${repo_url}" | sed 's#/$##; s#\.git$##')"
      repo_path="$(printf '%s' "${trimmed}" | sed 's#^https://github\.com/##')"
      printf 'https://raw.githubusercontent.com/%s/%s\n' "${repo_path}" "${ref}"
      ;;
    git@github.com:*)
      repo_path="$(printf '%s' "${repo_url}" | sed 's#^git@github\.com:##; s#\.git$##')"
      printf 'https://raw.githubusercontent.com/%s/%s\n' "${repo_path}" "${ref}"
      ;;
    *)
      return 1
      ;;
  esac
}

stage_remote_source_lightweight() {
  source_root="${TEMP_ROOT}/staged-source"
  raw_base_url="$(derive_raw_base_url "${REPO_URL}" "${REF}")" || return 1
  manifest_path="${TEMP_ROOT}/payload-manifest.txt"

  mkdir -p "${source_root}"
  download_to_file "${raw_base_url}/bootstrap/payload_manifest.txt" "${manifest_path}" || return 1
  download_to_file "${raw_base_url}/bootstrap/init_suplex.py" "${source_root}/bootstrap/init_suplex.py" || return 1

  while IFS= read -r relative_path || [ -n "${relative_path}" ]; do
    case "${relative_path}" in
      ""|\#*)
        continue
        ;;
    esac
    download_to_file "${raw_base_url}/${relative_path}" "${source_root}/${relative_path}" || return 1
  done < "${manifest_path}"

  SOURCE_ROOT="${source_root}"
}

stage_remote_source_archive() {
  archive_url="$(printf '%s' "${REPO_URL}" | sed 's#/$##; s#\.git$##')/archive/refs/heads/${REF}.zip"
  archive_path="${TEMP_ROOT}/suplex-template.zip"
  download_to_file "${archive_url}" "${archive_path}" || return 1
  unzip -q "${archive_path}" -d "${TEMP_ROOT}"
  SOURCE_ROOT="$(find "${TEMP_ROOT}" -mindepth 1 -maxdepth 1 -type d -name 'SUPLEX-agentic-workflow-*' | head -n 1)"
}

if [ -z "${SOURCE_ROOT}" ]; then
  TEMP_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/suplex-bootstrap.XXXXXX")"
  if ! stage_remote_source_lightweight; then
    echo "SUPLEX lightweight staging failed; falling back to full archive download." >&2
    stage_remote_source_archive
  fi
fi

if is_usable_python3 python3; then
  PYTHON_BIN="python3"
elif is_usable_python3 python; then
  PYTHON_BIN="python"
else
  echo "SUPLEX bootstrap failed: Python 3 is required. Attempted interpreters: ${ATTEMPTED_INTERPRETERS}. Install Python 3 and ensure either 'python3' or 'python' runs Python 3, then rerun the bootstrap." >&2
  exit 1
fi

"${PYTHON_BIN}" "${SOURCE_ROOT}/bootstrap/init_suplex.py" --target-dir "${TARGET_DIR}" --source-root "${SOURCE_ROOT}" --repo-url "${REPO_URL}" --ref "${REF}" --workflow-mode "${WORKFLOW_MODE}"
