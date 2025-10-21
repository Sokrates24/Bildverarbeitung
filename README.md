# 🧑‍💻 Git & VS Code – Arbeiten mit diesem Repository

## 🔄 Änderungen vom Remote-Repository holen

Wenn du sicherstellen möchtest, dass dein lokaler Stand aktuell ist:

```bash
git pull
```

Das lädt alle Änderungen vom Remote-Repository herunter und integriert sie in deinen lokalen Branch.

---

## ✏️ Änderungen machen und hochladen

1. Änderungen vornehmen (Dateien bearbeiten, hinzufügen oder löschen).  
2. Änderungen zum Commit vorbereiten:

   ```bash
   git add .
   ```

3. Commit erstellen:

   ```bash
   git commit -m "angepasst"
   ```

4. Änderungen hochladen (pushen):

   ```bash
   git push
   ```

---

## 💡 Git in VS Code verwenden

VS Code hat eingebaute Git-Unterstützung:

- **Quellcodeverwaltung öffnen** (Symbol mit drei Punkten/Verzweigungen links in der Seitenleiste).  
- Änderungen werden dort angezeigt.  
- Mit den Buttons kannst du *Commit*, *Pull* und *Push* direkt ausführen.

---

## 🧩 Nützliche Befehle

| Befehl | Beschreibung |
|--------|---------------|
| `git status` | Zeigt den aktuellen Status deiner Arbeitskopie |
| `git pull` | Holt die neuesten Änderungen vom Remote-Repository |
| `git add .` | Fügt alle Änderungen zum nächsten Commit hinzu |
| `git commit -m "Nachricht"` | Speichert deine Änderungen lokal |
| `git push` | Schiebt Commits ins Remote-Repository (GitHub) |