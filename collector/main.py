import pandas as pd
from ping3 import ping
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import datetime

# ==== CONFIG ====
BRANCHES_FILE = "branches.csv"
INFLUX_URL = "http://10.0.7.72:8086/"
INFLUX_TOKEN = "UZ8JIsMkoW0hpqsI_rFgLN7IK7lwtcKxDeEpTcqHW0PsjLa4Yo4ReaQiDW_Fb-nOHdurI85ZCc06__g8o48ztw=="
INFLUX_ORG = "phai-org"
INFLUX_BUCKET = "network"

# ==== Connect to InfluxDB ====
client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

# ==== Load branches ====
branches = pd.read_csv(BRANCHES_FILE)

def ping_branch(ip):
    try:
        latency = ping(ip, timeout=1)
        if latency is None:
            return {"status": "down", "latency": None}
        else:
            return {"status": "up", "latency": latency * 1000}  # ms
    except Exception as e:
        return {"status": "error", "latency": None}

def write_to_influx(branch, result):
    try:
        point = (
        Point("branch_status")
        .tag("branch", branch)
        .field("status", 1 if result["status"] == "up" else 0)
        .field("latency", result["latency"] if result["latency"] else 0)
        .time(datetime.datetime.utcnow())
        )
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
    except Exception as e:
        print(f"[ERROR] Failed to write to InfluxDB: {e}")

def main():
    while True:
        for _, row in branches.iterrows():
            result = ping_branch(row["ip"])
            print(f"{datetime.datetime.now().isoformat()} | {row['branch_name']}: {result}")
            write_to_influx(row["branch_name"], result)
        time.sleep(60)  # ping ทุก 60 วินาที

if __name__ == "__main__":
    main()
