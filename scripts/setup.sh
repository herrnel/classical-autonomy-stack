#!/usr/bin/env bash
# One-time setup: makes the project's scripts runnable from anywhere.
#
# It marks every script in this folder as executable and symlinks each one
# (without the .sh extension) into ~/.local/bin, adding that dir to your PATH
# if it isn't already there.
#
# Usage:
#   ./scripts/setup.sh
# Then, from any directory, you can run e.g.:
#   publish "my commit message"

set -euo pipefail

SCRIPTS_DIR="$(cd "$(dirname "$0")" && pwd)"
BIN_DIR="$HOME/.local/bin"

mkdir -p "$BIN_DIR"

echo "Linking scripts from $SCRIPTS_DIR into $BIN_DIR:"
for script in "$SCRIPTS_DIR"/*.sh; do
  name="$(basename "$script" .sh)"
  # Don't create a "setup" command for this installer itself
  [ "$name" = "setup" ] && continue
  chmod +x "$script"
  ln -sf "$script" "$BIN_DIR/$name"
  echo "  $name  ->  $script"
done

# Ensure ~/.local/bin is on PATH (persist in the shell rc if missing)
add_to_path() {
  local rc="$1"
  [ -f "$rc" ] || return 0
  if ! grep -qsF 'HOME/.local/bin' "$rc"; then
    {
      echo ''
      echo '# Added by classical-autonomy-stack setup.sh'
      echo 'export PATH="$HOME/.local/bin:$PATH"'
    } >> "$rc"
    echo "Added ~/.local/bin to PATH in $rc"
  fi
}

case ":$PATH:" in
  *":$BIN_DIR:"*)
    : # already on PATH
    ;;
  *)
    add_to_path "$HOME/.bashrc"
    add_to_path "$HOME/.zshrc"
    echo ''
    echo "PATH updated. Open a new terminal, or run:  export PATH=\"\$HOME/.local/bin:\$PATH\""
    ;;
esac

echo ''
echo "✓ Setup complete. From anywhere you can now run, for example:"
echo "    publish \"your commit message\""
