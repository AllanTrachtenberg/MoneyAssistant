# Installing Tkinter on macOS with Homebrew

Follow these steps to install Python and Tkinter using Homebrew:

## Prerequisites
- Homebrew must be installed. If not, install it from https://brew.sh

## Installation Steps

1. **Install Python 3:**
   ```bash
   brew install python3
   ```

2. **Install Tkinter:**
   ```bash
   brew install python-tk
   ```

## Verification
After installation, verify Tkinter is working:

```bash
python3 -m tkinter
```

A small window should appear. If you see an error, make sure your PATH is set to use Homebrew's Python.

## Notes
- If you use a virtual environment, recreate it after installing Python and Tkinter.
- For more troubleshooting, see the official Python and Homebrew documentation.
