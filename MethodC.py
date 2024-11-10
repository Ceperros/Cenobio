# Metodos.py
import os
from typing import List

class MethodC:
    
    def __init__(self):
        self.keywords_politica = ['presidente', 'gobierno', 'elecciones', 'política', 'congreso']
    
    def asignar_label(self, text: str) -> str:
        if any(keyword in text.lower() for keyword in self.keywords_politica):
            return '1'
        else:
            return '0'