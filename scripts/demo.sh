#!/usr/bin/env bash
# Live demo runner: press Enter to run each step, in slide order.
# Usage: bash scripts/demo.sh

cd "$(dirname "$0")/.." || exit 1
export PATH="$PWD/.venv/bin:$PATH"

BOLD='\033[1m'; CYAN='\033[0;36m'; YELLOW='\033[1;33m'; NC='\033[0m'

step() {
  local slide="$1"; shift
  clear
  echo -e "${CYAN}${BOLD}── ${slide} ──${NC}"
  echo -e "${YELLOW}\$ $*${NC}"
  read -rp $'\n[Enter to run] '
  echo
  eval "$@"
  echo
  read -rp $'[Enter to go back to slides] '
}

step "Slide 3 · Evidence integrity" \
  "bash scripts/verify_hashes.sh"

step "Slide 6 · Decrypting SUNBURST strings (Base64 + raw Deflate)" \
  "python3 -c \"import base64,zlib;[print(s,'->',zlib.decompress(base64.b64decode(s),-15).decode()) for s in ['SywrLstNzskvTdFLzs8FAA==','801MzsjMS3UvzUwBAA==']]\""

step "Slide 7 · FNV-1a blocklist: security tool" \
  "python3 scripts/run_forensics.py --check-process wireshark"

step "Slide 7 · FNV-1a blocklist: normal app" \
  "python3 scripts/run_forensics.py --check-process chrome"

step "Slide 8 · CAPA + ATT&CK behaviour reconstruction" \
  "capa --version && python3 scripts/run_forensics.py --simulate --simulate-behavior victim"

step "Slide 10 · Section 63 BSA certificate" \
  "python3 scripts/generate_bsa_cert.py --format both && less legal_compliance/Section_63_BSA_Certificate.md"

step "Slide 11 · Automated test suite" \
  "pytest tests/ -v"

clear
echo -e "${CYAN}${BOLD}Demo complete. Back to slides.${NC}"
