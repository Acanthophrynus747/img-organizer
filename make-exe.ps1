pyinstaller --name img-mover --icon=.\assets\img-org-icon.ico --onefile img-organizer.py; #command line version

pyinstaller --name img-mover-gui --icon=.\assets\img-org-icon.ico --onefile file-org-gui.py; #gui version

Read-Host -Prompt "Done! Press Enter to exit";