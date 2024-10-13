@router.post("/scan")
async def scan(target_url: str):
    """Scan a target URL for vulnerabilities and log the results."""
    # Replace this with actual scanning logic
    results = {"vulnerabilities": ["SQL Injection", "XSS"], "status": "Completed"}
    
    # Save results to the database
    db = SessionLocal()
    scan_result = ScanResult(target=target_url, scan_type="web", result=str(results))
    db.add(scan_result)
    db.commit()
    db.refresh(scan_result)
    
    return {"message": "Scan completed", "scan_id": scan_result.id, "results": results}
