[Unit]
Description=Smart Cat Care System
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/phan/catcare/main.py
WorkingDirectory=/home/phan/catcare
StandardOutput=journal
StandardError=journal
Restart=always
RestartSec=5
User=phan

[Install]
WantedBy=multi-user.target
