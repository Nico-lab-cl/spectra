Add-Type -AssemblyName System.Drawing
$imagePath = "c:\Users\quile\.gemini\antigravity\scratch\Calculadora\spectra\surgery_laptop.png"
$bitmap = [System.Drawing.Bitmap]::FromFile($imagePath)
$pixel = $bitmap.GetPixel(0, 0)
Write-Host "Color: #$("{0:X2}{1:X2}{2:X2}" -f $pixel.R, $pixel.G, $pixel.B)"
$bitmap.Dispose()
