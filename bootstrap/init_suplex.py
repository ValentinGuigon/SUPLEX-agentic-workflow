#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from textwrap import dedent
from urllib.request import urlopen
import zipfile


TEMPLATE_SUBDIR = "template"
TEMPLATE_REQUIRED_FILES = ["SUPLEX.md"]
TEMPLATE_REQUIRED_DIRS = [".suplex"]
METADATA_NAMES = {
    ".git",
    ".gitignore",
    ".gitattributes",
    ".github",
    ".suplex",
    "SUPLEX.md",
    "AGENTS.md",
    "CLAUDE.md",
    "README.md",
    "LICENSE",
    "LICENSE.md",
}
CODE_DIR_MARKERS = {"src", "app", "lib", "tests", "test", "scripts", "services", "packages"}
DATA_DIR_MARKERS = {"data", "datasets", "models", "notebooks"}
PUBLIC_DIR_MARKERS = {"site", "public", "docs_site", "mkdocs"}
BUILD_FILE_MARKERS = {
    "pyproject.toml",
    "requirements.txt",
    "package.json",
    "Cargo.toml",
    "Makefile",
    "CMakeLists.txt",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply the SUPLEX control layer to the current repository."
    )
    parser.add_argument(
        "--target-dir",
        default=".",
        help="Repository to initialize. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--source-root",
        help="Local suplex-template repository root. Skips remote archive fetch when provided.",
    )
    parser.add_argument(
        "--repo-url",
        default="https://github.com/ValentinGuigon/SUPLEX-agentic-workflow",
        help="Repository URL used to fetch a temporary archive when --source-root is not provided.",
    )
    parser.add_argument(
        "--ref",
        default="main",
        help="Git ref to fetch from the remote template repository.",
    )
    parser.add_argument(
        "--archive-url",
        help="Explicit archive URL to fetch instead of deriving one from --repo-url and --ref.",
    )
    parser.add_argument(
        "--workflow-mode",
        choices=("standard", "sans-sucre"),
        default="standard",
        help="SUPLEX runtime infrastructure mode to install in the target repository.",
    )
    return parser.parse_args()


def fail(message: str, exit_code: int = 1) -> int:
    print(message, file=sys.stderr)
    return exit_code


def extract_title_and_purpose(readme_text: str, fallback_name: str) -> tuple[str, str]:
    title = fallback_name
    for line in readme_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            break
    else:
        for line in readme_text.splitlines():
            stripped = line.strip()
            if stripped:
                title = stripped.strip("#*` ").strip() or fallback_name
                break

    paragraphs = []
    current: list[str] = []
    for raw_line in readme_text.splitlines():
        line = raw_line.strip()
        if not line:
            if current:
                paragraphs.append(" ".join(current).strip())
                current = []
            continue
        if line.startswith("#"):
            continue
        if re.match(r"^[-*]\s+", line):
            continue
        current.append(line)
    if current:
        paragraphs.append(" ".join(current).strip())

    purpose = paragraphs[0] if paragraphs else f"{title} is the target repository for SUPLEX initialization."
    return title, purpose


def analyze_target(target_dir: Path) -> dict[str, object]:
    entries = [entry for entry in target_dir.iterdir() if entry.name not in {".git"}]
    non_metadata = [entry for entry in entries if entry.name not in METADATA_NAMES]
    code_dirs = [entry.name for entry in entries if entry.is_dir() and entry.name in CODE_DIR_MARKERS]
    data_dirs = [entry.name for entry in entries if entry.is_dir() and entry.name in DATA_DIR_MARKERS]
    public_dirs = [entry.name for entry in entries if entry.is_dir() and entry.name in PUBLIC_DIR_MARKERS]
    compiled_validation = any((target_dir / marker).exists() for marker in BUILD_FILE_MARKERS)
    project_mode = "overlay" if non_metadata else "greenfield"

    return {
        "project_mode": project_mode,
        "public_surface": "present" if public_dirs else "absent",
        "compiled_validation": compiled_validation,
        "existing_code_structure_detected": bool(code_dirs or data_dirs),
        "existing_publication_structure_detected": bool(public_dirs),
        "existing_agent_governance_detected": any(
            (target_dir / filename).exists() for filename in ("AGENTS.md", "CLAUDE.md")
        ),
        "non_metadata_entries": [entry.name for entry in non_metadata],
        "code_dirs": code_dirs,
        "data_dirs": data_dirs,
        "public_dirs": public_dirs,
    }


def derive_archive_url(repo_url: str, ref: str) -> str:
    normalized = repo_url[:-4] if repo_url.endswith(".git") else repo_url
    return f"{normalized}/archive/refs/heads/{ref}.zip"


def stage_source(source_root: str | None, repo_url: str, ref: str, archive_url: str | None) -> tuple[Path, str | None]:
    if source_root:
        return Path(source_root).resolve(), None

    temp_dir = tempfile.mkdtemp(prefix="suplex-bootstrap-")
    archive_path = Path(temp_dir) / "suplex-template.zip"
    resolved_archive_url = archive_url or derive_archive_url(repo_url, ref)
    with urlopen(resolved_archive_url) as response:
        archive_path.write_bytes(response.read())

    with zipfile.ZipFile(archive_path) as archive:
        archive.extractall(temp_dir)

    extracted_roots = [path for path in Path(temp_dir).iterdir() if path.is_dir()]
    if len(extracted_roots) != 1:
        raise RuntimeError("Unable to determine staged source root from downloaded archive.")
    return extracted_roots[0], temp_dir


def resolve_template_root(source_root: Path) -> Path:
    template_root = source_root / TEMPLATE_SUBDIR
    if not template_root.is_dir():
        raise RuntimeError(f"Bootstrap source is missing template payload directory: {template_root}")
    return template_root


def copy_kernel(template_root: Path, target_dir: Path) -> None:
    suplex_root = template_root / ".suplex"
    target_suplex_root = target_dir / ".suplex"

    shutil.copy2(template_root / "SUPLEX.md", target_dir / "SUPLEX.md")
    if target_suplex_root.exists():
        shutil.rmtree(target_suplex_root)
    shutil.copytree(suplex_root, target_suplex_root)


def standard_current_handoff_placeholder() -> str:
    return dedent(
        """
        # No Active Handoff

        There is currently no active bounded pass.

        Supervision should:
        1. read this file first
        2. confirm that no unfinished bounded pass exists
        3. consult `./.suplex/docs/13_bounded_task_backlog.md` as the default next-task sequencing reference unless a blocker, discrepancy, or fresh validation result justifies a deviation
        4. issue exactly one new dated handoff before execution work begins
        """
    )


def sans_sucre_current_handoff_placeholder() -> str:
    return dedent(
        """
        # No Active Handoff

        There is currently no active bounded pass.

        In `sans-sucre` mode, supervision should:
        1. read this file first
        2. confirm that no unfinished bounded pass exists
        3. consult `./.suplex/docs/13_bounded_task_backlog.md` as the default next-task sequencing reference unless a blocker, discrepancy, or fresh validation result justifies a deviation
        4. issue exactly one new active handoff in this file before execution work begins
        5. use `./.suplex/handoffs/active/current_execution_report.md` as the matching live execution-report artifact for the pass
        """
    )


def sans_sucre_current_execution_report_placeholder() -> str:
    return dedent(
        """
        # No Active Execution Report

        There is currently no active execution report.

        In `sans-sucre` mode, execution should write the live report for the current bounded pass here.
        Clear or replace this file when the active pass is closed so stale report content does not carry into the next pass.
        """
    )


def configure_workflow_layout(target_dir: Path, workflow_mode: str) -> None:
    active_dir = target_dir / ".suplex" / "handoffs" / "active"
    history_dir = target_dir / ".suplex" / "handoffs" / "history"
    report_template = target_dir / ".suplex" / "handoffs" / "templates" / "01_execution_report_template.md"
    active_report = active_dir / "current_execution_report.md"

    if workflow_mode == "sans-sucre":
        if history_dir.exists():
            shutil.rmtree(history_dir)
        if report_template.exists():
            report_template.unlink()
        write_text(active_dir / "current_handoff.md", sans_sucre_current_handoff_placeholder())
        write_text(active_report, sans_sucre_current_execution_report_placeholder())
        return

    if active_report.exists():
        active_report.unlink()
    write_text(active_dir / "current_handoff.md", standard_current_handoff_placeholder())


def quote_yaml(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def normalize_prompt(text: str) -> str:
    return "\n".join(line.strip() for line in dedent(text).strip().splitlines())


def build_scope_doc(project_name: str, purpose: str, analysis: dict[str, object], workflow_mode: str) -> str:
    mode = analysis["project_mode"]
    if mode == "greenfield":
        scope_line = "- establish canonical control-memory docs for this target repo [E]"
        context_line = (
            "Target repo initialized in `greenfield` mode with the full SUPLEX agentic control layer. [E]"
        )
        out_of_scope = "- modeling, data, notebook, pipeline, publication, or deployment scaffolding [E]"
    else:
        scope_line = "- add canonical control-memory docs without restructuring the existing project [E]"
        context_line = (
            "Target repo initialized in `overlay` mode with the full SUPLEX agentic control layer and preexisting project structure preserved. [E]"
        )
        out_of_scope = "- renaming, moving, or deleting existing project directories [E]"

    return normalize_prompt(
        f"""
        # 00 Project Scope

        ## Project

        {purpose} [E]

        ## SUPLEX layer scope

        - establish repo-local governance for bounded agentic work [E]
        {scope_line}
        - install the same full SUPLEX agentic control layer regardless of detected repo shape [E]
        - prepare the repo for supervision bootstrap before bounded execution [E]
        - avoid computation or publication scaffolding during initialization [E]
        - defer architecture-planning and workflow-structure decisions to supervision after repo review and user check-in [E]

        ## Explicitly out of scope

        - computation-layer initialization [E]
        {out_of_scope}
        - project-domain execution during initialization [E]

        ## Current execution tool or agent context

        {context_line}

        ## Installed workflow mode

        - `{workflow_mode}` workflow infrastructure was installed during initialization. [E]

        ## Current task family

        Initialization completed; repo is ready for supervision bootstrap and first bounded-task definition. [E]
        """
    )


def build_provenance_doc(project_name: str) -> str:
    return dedent(
        f"""
        # 01 Source of Truth and Provenance

        Use this file to track what currently counts as source material, what is inferred, and what remains unresolved for `{project_name}`.

        ## Evidence tag definitions

        - `[E]` directly evidenced from repo artifacts or canonical docs
        - `[I]` strong inference from those artifacts
        - `[U]` unresolved / uncertain

        ## Tier 1 canonical sources

        - The target repo's `README.md` is the mandatory seed specification input for initialization. [E]
        - After initialization, repo-local canonical SUPLEX control memory lives in `./.suplex/docs/`. [E]
        - If the target repo's `README.md` is missing, initialization must halt and request either the file itself or enough project description to draft it first. [E]

        ## Tier 2 derived control artifacts

        - `SUPLEX.md` is the root entrypoint that points agents to the canonical SUPLEX control layer under `./.suplex/`. [E]
        - `./.suplex/AGENTS.md` and `./.suplex/CLAUDE.md` define stable SUPLEX governance for bounded agentic execution. [E]
        - `./.suplex/docs/00_project_scope.md`, `./.suplex/docs/08_status_checkpoint.md`, `./.suplex/docs/09_supervision_brief.md`, `./.suplex/docs/validation_ledger.md`, and `./.suplex/docs/discrepancy_log.md` are control-memory artifacts derived during initialization. [E]
        - `./.suplex/handoffs/` artifacts define bounded execution packets and remain subordinate to stable governance. [E]

        ## Tier 3 controlled support artifacts if any

        - `.suplex/init_state.yaml` is internal system state maintained by the control layer. [E]

        ## Source hierarchy rules

        - The target repo's `README.md` remains the first source for initialization and later reconstruction. [E]
        - Repo-local canonical docs in `./.suplex/docs/` take precedence over stale assumptions once they are rewritten during initialization. [E]
        - Handoffs constrain execution scope but do not override stable governance. [E]

        ## Unresolved provenance questions

        1. [U] Which project-specific documents beyond `README.md` should be promoted to canonical sources during supervision bootstrap?
        2. [U] Whether this repo will later require compiled validation conventions beyond the default validation ledger.
        """
    )


def build_checkpoint_doc(project_name: str, today: str, analysis: dict[str, object], workflow_mode: str) -> str:
    mode = analysis["project_mode"]
    if mode == "greenfield":
        action_line = "- [E] Added `SUPLEX.md` plus the canonical SUPLEX control layer under `./.suplex/`."
        not_done_line = "- [E] No computation, modeling, data, notebook, pipeline, publication, or deployment scaffolding was added."
        validation_line = "- [E] The repo is ready for the first supervisory decision."
    else:
        preserved = analysis["code_dirs"] + analysis["data_dirs"] + analysis["public_dirs"]
        preserved_text = ", ".join(f"`{name}/`" for name in preserved) if preserved else "preexisting project directories"
        action_line = f"- [E] Added the SUPLEX control layer alongside {preserved_text}."
        not_done_line = "- [E] No preexisting project directories were renamed, moved, deleted, or repurposed."
        validation_line = "- [E] The repo remains structurally unchanged outside the added control layer."

    return dedent(
        f"""
        # 08 Status Checkpoint

        ## Target-Repo Initialization Checkpoint - {today}

        ### Phase State

        - [E] This target repo completed bounded SUPLEX initialization in `{mode}` mode.
        - [E] The installed workflow infrastructure mode is `{workflow_mode}`.
        - [E] The same full SUPLEX agentic control layer was added without introducing computation or publication scaffolding.
        - [E] The first active layer after init is supervision, not execution.

        ### What Was Done

        - [E] Confirmed the target repo had its own `README.md` before initialization.
        {action_line}
        - [E] Rewrote `./.suplex/docs/00_project_scope.md`, `./.suplex/docs/01_source_of_truth_and_provenance.md`, `./.suplex/docs/08_status_checkpoint.md`, and `./.suplex/docs/09_supervision_brief.md` so they describe {project_name} rather than `suplex-template`.
        - [E] Wrote `.suplex/init_state.yaml` for the initialized target repo.
        - [E] Deferred architecture-planning and next-step selection to the supervision layer.

        ### What Was NOT Done

        {not_done_line}
        - [E] No project-domain execution task was started.

        ### Why It Was NOT Done

        - [E] Initialization is limited to preparing the control layer and truthful supervisory state.
        - [E] Project architecture and workflow-depth decisions must be made by supervision after reading `README.md` and checking with the user.

        ### Validation Decision

        - [E] The repo-state docs now reflect the target repo and are usable for supervision bootstrap.
        {validation_line}

        ### Exact Next Bounded Task

        - [E] `bootstrap_supervision_reconstruct_repo_state_and_propose_single_next_bounded_task`

        ### Context-Clear Assessment

        - [E] The initialization task family is closed.
        - [E] Relevant repo-state docs were rewritten during init.
        - [E] The next task family is different in kind because it moves from initialization to supervision.

        **Context can be cleared after this bounded pass.** [E]
        """
    )


def build_supervision_brief(project_name: str, purpose: str, analysis: dict[str, object], workflow_mode: str) -> str:
    mode = analysis["project_mode"]
    workflow_summary_line = (
        "- Workflow infrastructure: `standard` mode with dated handoff / execution-report history. [E]"
        if workflow_mode == "standard"
        else "- Workflow infrastructure: `sans-sucre` mode with active handoff and active execution-report artifacts only; no dated history directory. [E]"
    )
    active_report_rule = (
        "- Dated handoffs and execution reports should be read from `./.suplex/handoffs/history/` when present. [E]"
        if workflow_mode == "standard"
        else "- The live execution report should be read from `./.suplex/handoffs/active/current_execution_report.md`; no `./.suplex/handoffs/history/` record is required in this mode. [E]"
    )
    if mode == "greenfield":
        latest_state_line = "- The repo was initialized in `greenfield` mode from its own `README.md`. [E]"
        scope_line = "- Scope boundary: full control-layer initialization and supervision only; no computation or publication scaffolding by default"
        next_decision_lines = dedent(
            """
            - Ask the user whether they want to provide more detail about the project before planning begins. [E]
            - Treat architecture-planning or structure-confirmation as the default first bounded supervisory pass unless the user already provided enough detail to make that unnecessary. [E]
            """
        ).strip()
    else:
        preserved = analysis["code_dirs"] + analysis["data_dirs"] + analysis["public_dirs"]
        preserved_line = ""
        if preserved:
            preserved_line = f"- `{', '.join(preserved)}` remained in place during initialization. [E]"
        latest_state_line = "- The repo was initialized in `overlay` mode from its own `README.md`. [E]"
        scope_line = "- Scope boundary: initialize and supervise the full control layer without restructuring the current project architecture"
        next_decision_lines = dedent(
            """
            - Ask the user whether they want to provide more detail about the project before repo-state reconstruction begins. [E]
            - Treat repo-state audit or local reconstruction as the default first bounded supervisory pass so the next task can be defined from current repo evidence rather than assumptions. [E]
            """
        ).strip()

    extra_state = ""
    if mode != "greenfield" and analysis["code_dirs"] + analysis["data_dirs"] + analysis["public_dirs"]:
        extra_state = f"{preserved_line}\n"

    return dedent(
        f"""
        # 09 Supervision Brief

        ## 1. Purpose of the supervision brief

        This file is the portable supervision packet for {project_name} when the supervisor cannot read the repository files in the current session.

        ## 2. How this file should be used

        - Read this file together with the active handoff and latest checkpoint or report.
        - Use it to decide the next bounded supervisory action without assuming unseen repo context.
        - This brief was rewritten during target-repo initialization and is not a verbatim template copy. [E]

        ## 3. Project identity

        - Project: `{project_name}`
        - Purpose: {purpose}
        {scope_line}

        ## 4. SUPLEX workflow summary

        - The first active layer after initialization is supervision.
        {workflow_summary_line}
        - Reconstruction level is chosen explicitly.
        - Supervision must decide whether an architecture-planning pass is needed before implementation work begins.
        - Execution remains bounded by handoffs.

        ## 5. Current bounded task family

        - Task family: initialization complete; awaiting supervision bootstrap
        - Active mode set: `checkpoint`

        ## 6. Active source-of-truth rule

        - `./.suplex/docs/` is canonical SUPLEX control memory.
        - `./.suplex/handoffs/` defines bounded task packets.
        {active_report_rule}
        - Stable SUPLEX governance remains in `./.suplex/AGENTS.md` and `./.suplex/CLAUDE.md`.

        ## 7. Active handoff summary

        - Initialization prepared the control layer and rewrote target-state docs before supervision bootstrap. [E]

        ## 8. Latest validated state

        {latest_state_line}
        {extra_state}- `./.suplex/docs/00_project_scope.md`, `./.suplex/docs/01_source_of_truth_and_provenance.md`, `./.suplex/docs/08_status_checkpoint.md`, and this brief now describe the target repo rather than the template. [E]
        - The same full SUPLEX agentic control layer was installed regardless of target-repo shape. [E]
        - No computation or publication scaffolding was introduced. [E]

        ## 9. Latest execution report summary

        - Initialization completed and left the repo ready for the first supervisory decision. [E]

        ## 10. Open discrepancies / blockers

        - No blocker is currently recorded inside the control layer. [E]

        ## 11. Exact next supervisory decision

        - If you can read the repository files in this session, inspect the repo and `README.md` before deciding what happens next. [E]
        - If you cannot read the repository files in this session, do not guess hidden repo state; use this brief, `./.suplex/docs/08_status_checkpoint.md`, and `./.suplex/handoffs/initialization.md` as your working state instead. [E]
        - Ask the user what they want to do next. [E]
        {next_decision_lines}
        - Propose exactly one next bounded task for {project_name}. [E]

        ## 12. Update rule

        - Refresh this file whenever supervisory state changes materially.
        """
    )


def build_validation_ledger(today: str, analysis: dict[str, object], workflow_mode: str) -> str:
    mode = analysis["project_mode"]
    overlay_note = (
        "Existing project structure remained in place while the control layer was added."
        if mode == "overlay"
        else "The control layer was added to the current repo without extra project scaffolding."
    )
    return dedent(
        f"""
        # Validation Ledger

        ## {today} - Target-Repo Initialization

        | Check | Result | Notes |
        |---|---|---|
        | `README.md` precondition satisfied before initialization | PASS | Initialization ran only after confirming the target repo had its own `README.md` |
        | SUPLEX kernel copied without cloning the template repo into the target repo | PASS | Only `SUPLEX.md` and the canonical control layer under `./.suplex/` were added |
        | Requested workflow mode installed | PASS | Initialization configured `{workflow_mode}` workflow infrastructure in the target repo |
        | Repo-state docs rewritten before supervision bootstrap | PASS | `./.suplex/docs/00_project_scope.md`, `./.suplex/docs/01_source_of_truth_and_provenance.md`, `./.suplex/docs/08_status_checkpoint.md`, and `./.suplex/docs/09_supervision_brief.md` were rewritten for the target repo |
        | `.suplex/init_state.yaml` written for the current working directory | PASS | Init state now records the target repo mode and initialization metadata |
        | Existing repo structure preserved | PASS | {overlay_note} |
        | No computation/publication scaffolding introduced by initialization | PASS | No new `src/`, `scripts/`, `data/`, `notebooks/`, `site/`, `public/`, or `.github/workflows/` directories were created by SUPLEX init |
        | Ready message and first supervision prompt emitted | PASS | The bootstrap ends with a ready message and the first supervision prompt |
        """
    )


def build_discrepancy_log() -> str:
    return dedent(
        """
        # Discrepancy Log

        Use this file to record operational mismatches, ambiguities, or conflicts that matter to bounded execution.

        Suggested fields:
        - date
        - task family
        - discrepancy
        - impact
        - current status
        - next action

        ## Current status

        | date | task family | discrepancy | impact | current status | next action |
        |---|---|---|---|---|---|
        | none | `initialization` | No active discrepancy recorded at initialization close. | None. | Clear. [E] | Bootstrap supervision and define the first bounded task. [E] |
        """
    )


def build_init_state(
    today_iso: str,
    analysis: dict[str, object],
    repo_url: str,
    ref: str,
    workflow_mode: str,
) -> str:
    notes = [
        "SUPLEX was initialized into the current working directory without cloning the template repo.",
        "Target-state docs were rewritten before supervision bootstrap.",
        "The first active layer after init is supervision, not execution.",
    ]
    if analysis["project_mode"] == "greenfield":
        notes.append(
            "Because only metadata-like repo content was present at init, the first supervisory decision should normally ask for more project detail and then decide whether architecture planning is needed."
        )
    else:
        notes.append(
            "Because preexisting project content was present at init, the first supervisory decision should normally ask for any missing project detail and then reconstruct current repo state before defining the next bounded task."
        )
    lines = [
        'schema_version: "1.0"',
        'readme_path: "./README.md"',
        'readme_present: true',
        f'project_mode: "{analysis["project_mode"]}"',
        f'workflow_mode: "{workflow_mode}"',
        f'public_surface: "{analysis["public_surface"]}"',
        f'compiled_validation: {"true" if analysis["compiled_validation"] else "false"}',
        "governance_files:",
        '  - "SUPLEX.md"',
        '  - "./.suplex/AGENTS.md"',
        '  - "./.suplex/CLAUDE.md"',
        "inference_basis:",
        "  repo_scan: true",
        "  readme_present: true",
        f'  existing_code_structure_detected: {"true" if analysis["existing_code_structure_detected"] else "false"}',
        f'  existing_publication_structure_detected: {"true" if analysis["existing_publication_structure_detected"] else "false"}',
        f'  existing_agent_governance_detected: {"true" if analysis["existing_agent_governance_detected"] else "false"}',
        "  notes:",
    ]
    for note in notes:
        lines.append(f"    - {quote_yaml(note)}")
    lines.extend(
        [
            "source_template:",
            f"  repo_url: {quote_yaml(repo_url)}",
            f"  ref: {quote_yaml(ref)}",
            f"initialized_at: {quote_yaml(today_iso)}",
            f"last_updated: {quote_yaml(today_iso)}",
        ]
    )
    return "\n".join(lines) + "\n"


def mode_specific_first_step(analysis: dict[str, object]) -> str:
    mode = analysis["project_mode"]
    if mode == "greenfield":
        return dedent(
            """
            Ask the user whether they want to provide more detail about the project before planning begins.
            Treat architecture-planning or structure-confirmation as the default first bounded supervisory pass unless the user already provided enough detail to make that unnecessary.
            If you identify a material blocker or ambiguity that could affect scope, architecture, correctness, cost, or irreversible change, restate it and ask whether the user wants to resolve it directly or authorize best judgment.
            """
        ).strip()
    return dedent(
        """
        Ask the user whether they want to provide more detail about the project before repo-state reconstruction begins.
        Treat repo-state audit or local reconstruction as the default first bounded supervisory pass so the next task can be defined from current repo evidence rather than assumptions.
        If you identify a material blocker or ambiguity that could affect scope, architecture, correctness, cost, or irreversible change, restate it and ask whether the user wants to resolve it directly or authorize best judgment.
        """
    )


def first_supervision_prompt_ide(project_name: str, analysis: dict[str, object], workflow_mode: str) -> str:
    mode = analysis["project_mode"]
    mode_guidance = mode_specific_first_step(analysis)
    workflow_guidance = (
        "Use `./.suplex/handoffs/active/current_handoff.md` as the active pass pointer and use dated handoffs and dated execution reports in `./.suplex/handoffs/history/` as the bounded-pass record."
        if workflow_mode == "standard"
        else "Use `./.suplex/handoffs/active/current_handoff.md` plus `./.suplex/handoffs/active/current_execution_report.md` as the live pass artifacts; do not expect a dated history directory."
    )
    governance_guidance = ""
    if analysis["existing_agent_governance_detected"]:
        governance_guidance = dedent(
            """
            If root governance files such as `./AGENTS.md` or `./CLAUDE.md` already exist, inspect them early in the first pass.
            Explain to the user that root governance and SUPLEX governance now coexist and may not be equivalent in scope or authority.
            If you detect a meaningful conflict, ambiguity, or missing delegation boundary between root governance and SUPLEX governance, say so explicitly and ask whether the user wants a bounded governance-alignment pass before other work proceeds.
            """
        ).strip()
    if mode == "greenfield":
        startup_guidance = dedent(
            """
            Read `./.suplex/handoffs/active/current_handoff.md` first and confirm that initialization left the repo in the expected no-active-handoff state.
            """
        ).strip()
        sequencing_guidance = (
            "Use `./.suplex/docs/13_bounded_task_backlog.md` as the default sequencing reference unless a blocker or discrepancy justifies a deviation."
        )
    else:
        startup_guidance = dedent(
            """
            Read `./.suplex/handoffs/active/current_handoff.md` first and confirm that initialization left the repo in the expected no-active-handoff state.
            Treat preexisting repo state and any unfinished project work as context to reconstruct, not as an already-active bounded SUPLEX pass.
            """
        ).strip()
        sequencing_guidance = (
            "Use `./.suplex/docs/13_bounded_task_backlog.md` as a default reference only after you have reconstructed enough repo state to decide the next bounded task safely."
        )

    return normalize_prompt(
        f"""
        You are supervising a repository in which SUPLEX has just been initialized.
        The repository is `{project_name}`.
        The repo was initialized in `{mode}` mode.
        SUPLEX canonical control-layer files live under `./.suplex/`.
        {startup_guidance}
        Then read `SUPLEX.md`, `./.suplex/AGENTS.md`, `./.suplex/CLAUDE.md`, `README.md`, `./.suplex/docs/00_project_scope.md`, `./.suplex/docs/01_source_of_truth_and_provenance.md`, `./.suplex/docs/08_status_checkpoint.md`, `./.suplex/docs/09_supervision_brief.md`, `./.suplex/docs/10_supervision_layer_spec.md`, `./.suplex/docs/13_bounded_task_backlog.md`, and `./.suplex/handoffs/initialization.md`.
        Inspect the repo and `README.md` before deciding what happens next.
        {governance_guidance}
        Ask the user what they want to do next.
        {mode_guidance}
        {workflow_guidance}
        Do not offer to execute the bounded pass yourself unless the user explicitly authorizes collapsing the normal supervisor / execution split for that pass.
        If an active bounded pass remains open, say so explicitly, frame the next choice against that open pass, and state that context cannot yet be cleared.
        Do not silently make a user-owned material judgment call. If best judgment is authorized, state the assumption you adopt and report it again when the bounded pass closes.
        {sequencing_guidance}
        Choose the minimum reconstruction level needed and propose exactly one next bounded task only.
        """
    )


def first_supervision_prompt_browser(project_name: str, analysis: dict[str, object], workflow_mode: str) -> str:
    mode = analysis["project_mode"]
    mode_guidance = mode_specific_first_step(analysis)
    packet_description = (
        "Use only the provided supervision packet as working state: `SUPLEX.md`, `./.suplex/AGENTS.md`, `./.suplex/docs/09_supervision_brief.md`, `./.suplex/handoffs/active/current_handoff.md`, `./.suplex/docs/08_status_checkpoint.md`, and `./.suplex/docs/10_supervision_layer_spec.md`."
        if workflow_mode == "standard"
        else "Use only the provided supervision packet as working state: `SUPLEX.md`, `./.suplex/AGENTS.md`, `./.suplex/docs/09_supervision_brief.md`, `./.suplex/handoffs/active/current_handoff.md`, `./.suplex/handoffs/active/current_execution_report.md`, `./.suplex/docs/08_status_checkpoint.md`, and `./.suplex/docs/10_supervision_layer_spec.md`."
    )
    workflow_guidance = (
        "Use `./.suplex/handoffs/active/current_handoff.md` as the active pass pointer and use dated handoffs and dated execution reports in `./.suplex/handoffs/history/` if they are present in the packet."
        if workflow_mode == "standard"
        else "Use `./.suplex/handoffs/active/current_handoff.md` plus `./.suplex/handoffs/active/current_execution_report.md` as the live bounded-pass packet; do not expect a dated history directory."
    )
    governance_guidance = ""
    if analysis["existing_agent_governance_detected"]:
        governance_guidance = dedent(
            """
            If the user provides root governance files such as `./AGENTS.md` or `./CLAUDE.md`, inspect them early.
            Explain any meaningful conflict, ambiguity, or missing delegation boundary between root governance and SUPLEX governance before defining other work.
            """
        ).strip()
    if mode == "greenfield":
        startup_guidance = dedent(
            """
            Read `./.suplex/handoffs/active/current_handoff.md` first and treat it as a no-active-handoff confirmation, not as an unfinished bounded pass.
            """
        ).strip()
        sequencing_guidance = (
            "Use `./.suplex/docs/13_bounded_task_backlog.md` only if it is present in the provided packet or quoted to you by the user."
        )
    else:
        startup_guidance = dedent(
            """
            Read `./.suplex/handoffs/active/current_handoff.md` first and treat it as a no-active-handoff confirmation, not as an unfinished bounded pass.
            Treat preexisting repo state described in the packet as context to reconstruct, not as an already-active bounded SUPLEX pass.
            """
        ).strip()
        sequencing_guidance = (
            "Use `./.suplex/docs/13_bounded_task_backlog.md` only if it is present in the provided packet or quoted to you by the user, and only after you have reconstructed enough repo state to decide the next bounded task safely."
        )

    return dedent(
        f"""
        You are supervising a repository in which SUPLEX has just been initialized, without direct repo access.
        The repository is `{project_name}`.
        The repo was initialized in `{mode}` mode.
        {packet_description}
        {startup_guidance}
        Read the rest of the provided packet before defining new work.
        Do not guess hidden repo state beyond the provided packet.
        {governance_guidance}
        Ask the user what they want to do next.
        {mode_guidance}
        {workflow_guidance}
        Do not offer to execute the bounded pass yourself unless the user explicitly authorizes collapsing the normal supervisor / execution split for that pass.
        If an active bounded pass remains open, say so explicitly, frame the next choice against that open pass, and state that context cannot yet be cleared.
        Do not silently make a user-owned material judgment call. If best judgment is authorized, state the assumption you adopt and report it again when the bounded pass closes.
        {sequencing_guidance}
        Choose the minimum reconstruction level justified by the packet and propose exactly one next bounded task only.
        """
    ).strip()


def build_ready_message(target_dir: Path, project_name: str, analysis: dict[str, object], workflow_mode: str) -> str:
    supervisor_prompt_ide = first_supervision_prompt_ide(project_name, analysis, workflow_mode)
    supervisor_prompt_browser = first_supervision_prompt_browser(project_name, analysis, workflow_mode)
    separator = "=" * 72
    packet_lines = [
        "- `SUPLEX.md`",
        "- `./.suplex/AGENTS.md`",
        "- `./.suplex/docs/09_supervision_brief.md`",
        "- `./.suplex/handoffs/active/current_handoff.md`",
        "- `./.suplex/docs/08_status_checkpoint.md`",
        "- `./.suplex/docs/10_supervision_layer_spec.md`",
    ]
    if workflow_mode == "sans-sucre":
        packet_lines.insert(4, "- `./.suplex/handoffs/active/current_execution_report.md`")
    return "\n".join(
        [
            separator,
            f"SUPLEX ready in {target_dir}",
            separator,
            f"Workflow mode: {workflow_mode}",
            separator,
            "IDE or terminal supervision: pass only the IDE prompt below.",
            "Browser-chat supervision without repo access: pass the browser prompt below together with these files:",
            *packet_lines,
            separator,
            "Supervisor Prompt For IDE Or Terminal",
            separator,
            supervisor_prompt_ide,
            separator,
            "Supervisor Prompt For Browser Chat",
            separator,
            supervisor_prompt_browser,
            separator,
        ]
    )


def initialize(target_dir: Path, source_root: Path, repo_url: str, ref: str, workflow_mode: str) -> int:
    readme_path = target_dir / "README.md"
    if not readme_path.exists():
        return fail(
            "SUPLEX bootstrap halted: `README.md` is missing in the current repository.\n"
            "Add `README.md` first, or provide a short project description so a README can be drafted before initialization.",
            exit_code=2,
        )

    readme_text = readme_path.read_text(encoding="utf-8")
    project_name, purpose = extract_title_and_purpose(readme_text, target_dir.name)
    analysis = analyze_target(target_dir)

    template_root = resolve_template_root(source_root)
    copy_kernel(template_root, target_dir)
    configure_workflow_layout(target_dir, workflow_mode)

    today = os.environ.get("SUPLEX_INIT_DATE", "2026-04-13")
    today_iso = os.environ.get("SUPLEX_INIT_TIMESTAMP", f"{today}T00:00:00Z")

    write_text(target_dir / ".suplex" / "docs" / "00_project_scope.md", build_scope_doc(project_name, purpose, analysis, workflow_mode))
    write_text(target_dir / ".suplex" / "docs" / "01_source_of_truth_and_provenance.md", build_provenance_doc(project_name))
    write_text(target_dir / ".suplex" / "docs" / "08_status_checkpoint.md", build_checkpoint_doc(project_name, today, analysis, workflow_mode))
    write_text(target_dir / ".suplex" / "docs" / "09_supervision_brief.md", build_supervision_brief(project_name, purpose, analysis, workflow_mode))
    write_text(target_dir / ".suplex" / "docs" / "validation_ledger.md", build_validation_ledger(today, analysis, workflow_mode))
    write_text(target_dir / ".suplex" / "docs" / "discrepancy_log.md", build_discrepancy_log())
    write_text(target_dir / ".suplex" / "init_state.yaml", build_init_state(today_iso, analysis, repo_url, ref, workflow_mode))

    print(build_ready_message(target_dir, project_name, analysis, workflow_mode))
    return 0


def main() -> int:
    args = parse_args()
    target_dir = Path(args.target_dir).resolve()
    if not target_dir.is_dir():
        return fail(f"Target directory does not exist: {target_dir}")

    temp_dir: str | None = None
    try:
        source_root, temp_dir = stage_source(args.source_root, args.repo_url, args.ref, args.archive_url)
        template_root = resolve_template_root(source_root)
        required_paths = [template_root / path for path in TEMPLATE_REQUIRED_FILES + TEMPLATE_REQUIRED_DIRS]
        missing = [str(path) for path in required_paths if not path.exists()]
        if missing:
            return fail("Bootstrap source is missing required kernel assets:\n" + "\n".join(missing))
        return initialize(target_dir, source_root, args.repo_url, args.ref, args.workflow_mode)
    except Exception as exc:  # noqa: BLE001
        return fail(f"SUPLEX bootstrap failed: {exc}")
    finally:
        if temp_dir:
            shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
