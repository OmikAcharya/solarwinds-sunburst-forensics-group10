#!/usr/bin/env bash
# ==============================================================================
# Setup & Initialization Script
# Project: solarwinds-sunburst-forensics-group10
# Department of Computer Engineering, KJ Somaiya School of Engineering
# Somaiya Vidyavihar University, Mumbai, Maharashtra
# Authors: Amandeep Singh, Omik Acharya, Om Lanke
# ==============================================================================

set -euo pipefail

# ANSI Styling
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BLUE}${BOLD}==============================================================================${NC}"
echo -e "${BLUE}${BOLD}  INITIALIZING DFIR LAB ENVIRONMENT: GROUP 10 FORENSIC REPOSITORY            ${NC}"
echo -e "${CYAN}  KJ Somaiya School of Engineering | Department of Computer Engineering       ${NC}"
echo -e "${BLUE}${BOLD}==============================================================================${NC}"
echo ""

# 1. Ensure executable permissions on all shell and python scripts
echo -e "${CYAN}[*] Applying execute permissions (chmod +x) to forensic scripts...${NC}"
chmod +x scripts/verify_hashes.sh
chmod +x scripts/run_forensics.py
chmod +x scripts/generate_bsa_cert.py
echo -e "${GREEN}[+] Scripts marked executable.${NC}"

# 2. Python Version Detection (Requires Python >= 3.10 for match/case pattern matching in vivisect)
PYTHON_BIN=""
CANDIDATES=(
    "python3.12"
    "python3.11"
    "python3.10"
    "/usr/local/bin/python3.11"
    "/opt/homebrew/bin/python3.11"
    "/opt/homebrew/bin/python3.10"
    "python3"
)

for cand in "${CANDIDATES[@]}"; do
    if command -v "$cand" >/dev/null 2>&1; then
        ver=$("$cand" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null || true)
        major=$(echo "$ver" | cut -d. -f1)
        minor=$(echo "$ver" | cut -d. -f2)
        if [ -n "$major" ] && [ -n "$minor" ]; then
            if [ "$major" -eq 3 ] && [ "$minor" -ge 10 ]; then
                PYTHON_BIN="$cand"
                echo -e "${GREEN}[+] Selected Python ${ver} ($cand) [Supports PEP 634 pattern matching]${NC}"
                break
            fi
        fi
    fi
done

if [ -z "$PYTHON_BIN" ]; then
    PYTHON_BIN="python3"
    echo -e "${YELLOW}[!] WARNING: Python >= 3.10 not found. Falling back to default 'python3'.${NC}"
fi

# 3. Virtual Environment & Dependency Installation
VENV_DIR=".venv"

if command -v uv >/dev/null 2>&1; then
    echo -e "${CYAN}[*] Fast package manager 'uv' detected.${NC}"
    if [ ! -d "${VENV_DIR}" ]; then
        echo -e "${CYAN}[*] Creating virtual environment via uv with ${PYTHON_BIN}...${NC}"
        uv venv --python "${PYTHON_BIN}" "${VENV_DIR}"
        echo -e "${GREEN}[+] Virtual environment initialized with uv.${NC}"
    fi
    # shellcheck source=/dev/null
    source "${VENV_DIR}/bin/activate"
    echo -e "${CYAN}[*] Installing dependencies with uv pip...${NC}"
    uv pip install -r requirements.txt
    echo -e "${GREEN}[+] Dependencies installed via uv.${NC}"
else
    if [ ! -d "${VENV_DIR}" ]; then
        echo -e "${CYAN}[*] Creating virtual environment using ${PYTHON_BIN} in ${VENV_DIR}...${NC}"
        "${PYTHON_BIN}" -m venv "${VENV_DIR}"
        echo -e "${GREEN}[+] Virtual environment initialized.${NC}"
    else
        echo -e "${YELLOW}[!] Existing virtual environment found at ${VENV_DIR}.${NC}"
    fi
    # shellcheck source=/dev/null
    source "${VENV_DIR}/bin/activate"
    echo -e "${CYAN}[*] Installing dependencies from requirements.txt...${NC}"
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt
    echo -e "${GREEN}[+] Dependencies installed successfully.${NC}"
fi

# 4. Verify Cryptographic Integrity
echo ""
echo -e "${CYAN}[*] Executing initial cryptographic baseline validation...${NC}"
bash scripts/verify_hashes.sh

# 5. Run Pytest Suite
echo ""
echo -e "${CYAN}[*] Running forensic pipeline verification tests...${NC}"
pytest tests/ -v

echo ""
echo -e "${GREEN}${BOLD}==============================================================================${NC}"
echo -e "${GREEN}${BOLD}[+] SETUP COMPLETE: All forensic tooling, scripts, and tests verified!       ${NC}"
echo -e "${GREEN}${BOLD}==============================================================================${NC}"
