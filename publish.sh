#!/usr/bin/env bash
# Quick commit + push helper.
# Usage:
#   ./publish.sh "your commit message"
#   ./publish.sh your commit message      (quotes optional)
# If no message is given, a timestamped default is used.

set -euo pipefail

# Move to the repo root (directory this script lives in)
cd "$(dirname "$0")"

# Join all arguments into the commit message, or use a timestamp default
if [ "$#" -gt 0 ]; then
  msg="$*"
else
  msg="Update $(date '+%Y-%m-%d %H:%M:%S')"
fi

# Nothing to commit? Bail early.
if git diff --quiet && git diff --cached --quiet; then
  echo "Nothing to commit — working tree clean."
  exit 0
fi

git add -A
git commit -m "$msg"
git push

echo "✓ Published: $msg"
