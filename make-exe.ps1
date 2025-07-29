pyinstaller --name img_mover --icon=.\assets\img-org-icon.ico --onefile file_organizer.py; #command line version

pyinstaller --name img-move-gui --icon=.\assets\img-org-icon.ico --onefile file-org-gui.py; #gui version

Read-Host -Prompt "Done. Press Enter to exit";