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

# 2. Virtual Environment Setup
VENV_DIR=".venv"
if [ ! -d "${VENV_DIR}" ]; then
    echo -e "${CYAN}[*] Creating Python virtual environment in ${VENV_DIR}...${NC}"
    python3 -m venv "${VENV_DIR}"
    echo -e "${GREEN}[+] Virtual environment initialized.${NC}"
else
    echo -e "${YELLOW}[!] Existing virtual environment found at ${VENV_DIR}.${NC}"
fi

# Activate virtual environment
# shellcheck source=/dev/null
source "${VENV_DIR}/bin/activate"

# 3. Upgrade pip and install dependencies
echo -e "${CYAN}[*] Installing dependencies from requirements.txt...${NC}"
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
echo -e "${GREEN}[+] Dependencies installed successfully.${NC}"

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
