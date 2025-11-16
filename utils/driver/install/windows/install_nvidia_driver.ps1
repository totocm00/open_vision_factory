# PowerShell 5.1+ / 7.x Compatible

chcp 65001 > $null
Write-Host "### STEP 1: GPU 정보 확인 중... (Detecting GPU info...) ###"
Get-CimInstance Win32_VideoController | Select-Object Name, DriverVersion

Write-Host "`n### STEP 2: NVIDIA 드라이버 자동 설치 안내 (Driver Install Guide) ###"
Write-Host "※ PowerShell은 자동 다운로드 기능이 제한적입니다."
Write-Host "다음 경로에서 최신 드라이버를 직접 다운로드해주세요:"
Write-Host "👉 https://www.nvidia.com/Download/index.aspx"

$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Warning "⚠️ 관리자 권한으로 PowerShell을 실행해야 드라이버 설치가 가능합니다."
}

$choice = Read-Host "드라이버 설치 파일을 수동 실행할까요? (y/N)"
if ($choice -match "^[yY]$") {
    $installerPath = "C:\NVIDIA\setup.exe"
    if (Test-Path $installerPath) {
        Write-Host "설치 파일 실행 중... (Running installer...)"
        Start-Process -FilePath $installerPath -ArgumentList "/s" -Wait
        Write-Host "[DONE] 설치 완료! 재부팅 후 적용됩니다. (Installation finished! Please reboot.)"
    } else {
        Write-Warning "⚠️ 설치 파일을 찾을 수 없습니다: $installerPath"
        Write-Host "직접 다운로드 후 다시 실행하세요."
    }
} else {
    Write-Host "설치를 취소했습니다. (Installation cancelled.)"
}