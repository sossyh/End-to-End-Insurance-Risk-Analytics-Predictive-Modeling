# setup_dvc.ps1 - DVC Setup Script for Windows PowerShell

Write-Host "[INFO] Starting DVC setup for Windows + PowerShell..."

# Navigate to project root
Write-Host "[INFO] Navigating to project root..."
Set-Location -Path "C:\Users\soswo\OneDrive\Desktop\projects\End-to-End-Insurance-Risk-Analytics-Predictive-Modeling"

# Activate virtual environment
Write-Host "[INFO] Activating virtual environment..."
& "venv\Scripts\Activate.ps1"

# Install DVC
Write-Host "[INFO] Installing DVC..."
pip install dvc

# Initialize DVC
Write-Host "[INFO] Initializing DVC..."
dvc init

# Create local DVC storage directory
Write-Host "[INFO] Creating local DVC storage directory..."
$storagePath = "..\dvc-storage"
if (-Not (Test-Path $storagePath)) {
    New-Item -ItemType Directory -Force -Path $storagePath
} else {
    Write-Host "[INFO] DVC storage directory already exists."
}

# Add local DVC remote
Write-Host "[INFO] Adding local DVC remote..."
dvc remote add -d localstorage $storagePath

# Track dataset with DVC
Write-Host "[INFO] Tracking dataset with DVC..."
dvc add data/raw/MachineLearningRating_v3.txt

# Commit DVC changes to Git
Write-Host "[INFO] Staging and committing DVC files to Git..."
git add data/raw/MachineLearningRating_v3.txt.dvc .gitignore .dvc/config
git commit -m "Add DVC tracking and remote for MachineLearningRating_v3.txt"

# Push dataset to remote
Write-Host "[INFO] Pushing dataset to local remote..."
dvc push

Write-Host "[SUCCESS] DVC setup complete!"
