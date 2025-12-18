
Notion Link
https://www.notion.so/Create-a-GCP-VM-using-a-Python-script-from-your-local-machine-2cd23cb201b5804f9c4bd3c73b6ec5b0?source=copy_link


### 1️⃣ Install Google Cloud SDK (Local)

```bash
gcloud --version

```

If not installed, install from: https://cloud.google.com/sdk

---

### 2️⃣ Authenticate Your Local Machine

```bash
gcloud auth login

```

This opens a browser → login with your GCP account.

---

### 3️⃣ Set Project & Zone

```bash
gcloud configset project eng-archery-480704-i7
gcloud configset compute/zone asia-south1-a

```

Verify:

```bash
gcloud config list

```

---

### 4️⃣ Enable Compute Engine API

```bash
gcloud servicesenable compute.googleapis.com

```

---

## 🧠 Two Ways to Create VM Using Python

### 🔹 Option A (Recommended for DevOps):

**Python script calling `gcloud` CLI**

✔ Simple

✔ Interview-friendly

✔ No complex SDK setup

---

### 🔹 Option B (Advanced):

**Python using GCP Compute API (google-cloud-compute)**

✔ Pure API

✔ Production automation

✔ Used in infra platforms

---

I’ll show **Option A first** (best starting point).

---

## 🚀 OPTION A: Create GCP VM Using Python (via gcloud)

### 📁 Project Structure

```bash
mkdir gcp-vm-python
cd gcp-vm-python

```

---

### 📄 create_vm.py

```python
import subprocess

PROJECT_ID ="eng-archery-480704-i7"
ZONE ="asia-south1-a"
VM_NAME ="dev-backend-vm"
MACHINE_TYPE ="e2-medium"
IMAGE_FAMILY ="ubuntu-2204-lts"
IMAGE_PROJECT ="ubuntu-os-cloud"

defcreate_vm():
    cmd = [
"gcloud","compute","instances","create", VM_NAME,
"--project", PROJECT_ID,
"--zone", ZONE,
"--machine-type", MACHINE_TYPE,
"--image-family", IMAGE_FAMILY,
"--image-project", IMAGE_PROJECT,
"--boot-disk-size","20GB",
"--boot-disk-type","pd-balanced",
"--tags","http-server,https-server"
    ]

print("🚀 Creating GCP VM...")
    subprocess.run(cmd, check=True)
print("✅ VM created successfully")

if __name__ =="__main__":
    create_vm()

```

---

### ▶️ Execute Script

```bash
python3 create_vm.py

```

---

### ✅ Output (Expected)

```
Creating instance(s) dev-backend-vm...
Created [https://www.googleapis.com/compute/v1/projects/eng-archery-480704-i7/zones/asia-south1-a/instances/dev-backend-vm].

```

---

## 🔍 Verify VM

```bash
gcloud compute instances list

```

---

## 🛡️ Production-Level Considerations

| Concern | Best Practice |
| --- | --- |
| Authentication | Use `gcloud auth login` or Service Account |
| Error Handling | `subprocess.run(check=True)` |
| Logging | Add Python logging |
| Idempotency | Check if VM exists before create |
| Security | Avoid hardcoding credentials |
| Automation | Run via CI/CD or cron |

---

## 🧠 Interview Explanation (Short & Crisp)

> “Yes, I can create GCP VMs using Python.
> 
> 
> From my local machine, I authenticate using `gcloud auth login`.
> 
> Then I either call `gcloud compute instances create` via Python for simplicity, or use the GCP Compute API for full automation.
> 
> This approach is commonly used in DevOps for repeatable infrastructure provisioning.”
> 

![image.png](attachment:45bded21-7eac-4949-90c0-461f1929c082:image.png)




