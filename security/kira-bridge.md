# Bridge ZDOS ↔ K.I.R.A.

Comunicazione bidirezionale di laboratorio.

## Messaggi

- `ATTACK_REPORT` → ZDOS invia a KIRA payload sospetto + metadata.
- `POLICY_UPDATE` ← KIRA risponde con regola di blocco o allow.
- `HEARTBEAT` ↔ stato mutuo.

## Cattura

Ogni `ATTACK_REPORT` viene scritto in `/var/log/zdos-attacks.log` (JSON lines).

Implementazione skeleton in `security/interceptor.py`.
