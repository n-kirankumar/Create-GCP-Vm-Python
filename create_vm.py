import subprocess

PROJECT_ID = "eng-archery-480704-i7"
ZONE = "asia-south1-a"
VM_NAME = "dev-backend-vm"
MACHINE_TYPE = "e2-medium"
IMAGE_FAMILY = "ubuntu-2204-lts"
IMAGE_PROJECT = "ubuntu-os-cloud"

def create_vm():
    cmd = [
        "gcloud", "compute", "instances", "create", VM_NAME,
        "--project", PROJECT_ID,
        "--zone", ZONE,
        "--machine-type", MACHINE_TYPE,
        "--image-family", IMAGE_FAMILY,
        "--image-project", IMAGE_PROJECT,
        "--boot-disk-size", "20GB",
        "--boot-disk-type", "pd-balanced",
        "--tags", "http-server,https-server"
    ]

    print("🚀 Creating GCP VM...")
    subprocess.run(cmd, check=True)
    print("✅ VM created successfully")

if __name__ == "__main__":
    create_vm()

