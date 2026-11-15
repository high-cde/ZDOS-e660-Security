# ZDOS-Compaq-e660-Security

ISO e ambiente ZDOS adattato per hardware legacy tipo **Compaq Evo N610c / e660** (Pentium 4-M, BIOS legacy, max ~1 GB RAM, IDE).

## Obiettivo

- Build ISO bootabile su hardware vecchio (legacy BIOS, no UEFI).
- Layer di **sicurezza globale multitasking** che protegge l'ecosistema ZDOS da richieste esterne.
- Comunicazione bidirezionale con **K.I.R.A.** (interno).
- Cattura su file (`/var/log/zdos-attacks.log`) dei dati di attacco / richieste sospette.

## Stato

Prototipo di laboratorio. Non è un'immagine pronta al download. Serve build locale.

## Hardware target (stima)

- CPU: Intel Pentium 4-M (1.6–2.4 GHz)
- RAM: 256 MB – 1 GB DDR
- Storage: IDE 2.5"
- BIOS: Legacy (no UEFI)
- Grafica: ATI Mobility Radeon 7500 (opzionale)

## Come generare l'ISO

```sh
# Requisiti: grub-mkrescue, xorriso, gcc, make, cpio, (qemu-system-i386 per test)
git clone https://github.com/high-cde/ZDOS-e660-Security.git
cd ZDOS-e660-Security
chmod +x build/build-iso.sh
./build/build-iso.sh
# Poi: grub-mkrescue -o build/zdos-e660.iso build/iso
```

## Sicurezza globale

Vedi `security/README.md`.

## Avvertenze

- Hardware molto limitato: multitasking reale è vincolato.
- Nessuna garanzia di boot su ogni variante e660.
- Policy di verità ZDOS: sperimentale. Integra kernel reale dal repo ZDOS principale.
