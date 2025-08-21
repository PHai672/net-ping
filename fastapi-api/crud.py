import pandas as pd
from models import Branch

CSV_FILE = "../branches.csv"  # ใช้ไฟล์ร่วมกับ collector

def read_all_branches():
    df = pd.read_csv(CSV_FILE)
    return df.to_dict(orient="records")

def add_branch(branch: Branch):
    df = pd.read_csv(CSV_FILE)
    if branch.ip in df["ip"].values:
        raise ValueError("IP already exists")
    df = pd.concat([df, pd.DataFrame([branch.dict()])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

def update_branch(ip: str, branch: Branch):
    df = pd.read_csv(CSV_FILE)
    if ip not in df["ip"].values:
        raise ValueError("Branch not found")
    df.loc[df["ip"] == ip, "branch_name"] = branch.branch_name
    df.to_csv(CSV_FILE, index=False)

def delete_branch(ip: str):
    df = pd.read_csv(CSV_FILE)
    if ip not in df["ip"].values:
        raise ValueError("Branch not found")
    df = df[df["ip"] != ip]
    df.to_csv(CSV_FILE, index=False)
