def checkinstall():
    # Check if pygame is installed
    try:
        import pygame
        import subprocess
        import speech_recognition
    except ImportError:
        print("pygame is not installed. Installing...")
        
        # Use pip to install pygame
        subprocess.check_call(["pip", "install", "pygame"])
        subprocess.check_call(["pip", "install", "SpeechRecognition"])
        subprocess.check_call(["pip", "install", "PyAudio"])