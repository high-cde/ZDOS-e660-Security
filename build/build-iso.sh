#!/usr/bin/env bash
# Build ISO ZDOS minimale per hardware legacy (Compaq e660 / Evo N610c)
# Richiede: grub-mkrescue, xorriso, qemu-system-i386 (per test)
set -euo pipefail

echo "=== Build ZDOS-e660 ISO (legacy BIOS) ==="
mkdir -p build/iso/boot/grub

# Placeholder kernel / initramfs (sostituire con artefatti reali da ZDOS)
cat > build/iso/boot/grub/grub.cfg << 'EOF'
set timeout=5
set default=0
menuentry "ZDOS e660 Security" {
    linux /boot/vmlinuz root=/dev/ram0 zdos.legacy=1 zdos.security=global
    initrd /boot/initrd.img
}
EOF

echo "ISO skeleton creato. Integra kernel reale da repo ZDOS e riesegui grub-mkrescue."
echo "Comando tipico: grub-mkrescue -o build/zdos-e660.iso build/iso"
