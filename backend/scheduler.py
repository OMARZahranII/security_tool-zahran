
from apscheduler.schedulers.background import BackgroundScheduler
from services.network_scanner import run_nmap_scan

scheduler = BackgroundScheduler()

def schedule_scan():
    scheduler.add_job(run_nmap_scan, 'interval', days=1, args=["192.168.1.1"])
    scheduler.start()
