# Sicurezza globale ZDOS-e660

Layer multitasking che:

1. Intercetta tutte le richieste in entrata (rete, serial, input).
2. Le inoltra a K.I.R.A. per analisi.
3. Cattura su file (`/var/log/zdos-attacks.log`) i dati sospetti.
4. Protegge l'ecosistema interno.

## Componenti

- `security/interceptor.py` — skeleton intercettore.
- `security/kira-bridge.md` — protocollo di comunicazione con K.I.R.A.
- `security/capture.sh` — script di cattura.

## Limiti

Su hardware e660 le risorse sono scarse. Il multitasking è best-effort.
