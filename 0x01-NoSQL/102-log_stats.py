#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

def log_stats():
    """
    Script to provide stats about Nginx logs stored in MongoDB
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    collection = db.nginx

    # Count total number of logs
    total_logs = collection.count_documents({})

    # Count number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})

    # Count number of logs for method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Count occurrences of each IP address
    ip_counts = {}
    for log in collection.find({}, {"ip": 1}):
        ip = log["ip"]
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

    # Sort IPs by occurrence counts and select top 10
    top_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    # Display stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")
    print("IPs:")
    for ip, count in top_ips:
        print(f"\t{ip}: {count}")

if __name__ == "__main__":
    log_stats()
