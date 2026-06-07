import re 
import os 
import sys 
import hashlib 
from pathlib import Path 
from datetime import datetime 
from typing import List, Dict 
import warnings 
warnings.filterwarnings('ignore') 
 
if sys.platform == 'win32': 
    import io 
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace') 
 
class PQCHackingTool: 
    def __init__(self): 
        self.vulnerability_database = { 
            'RSA': {'threat': "Shor's algorithm", 'migration': 'ML-KEM-768', 'risk': 95}, 
            'ECDSA': {'threat': "Shor's algorithm", 'migration': 'ML-DSA-65', 'risk': 95}, 
            'Ed25519': {'threat': "Shor's algorithm", 'migration': 'SLH-DSA', 'risk': 85}, 
        } 
 
    def scan_file(self, filepath): 
        result = {'file': filepath, 'vulnerabilities': []} 
        try: 
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f: 
                content = f.read() 
                lines = content.split('\n') 
                for algo, info in self.vulnerability_database.items(): 
                    if re.search(rf'\b{algo}\b', content, re.IGNORECASE): 
                        for i, line in enumerate(lines, 1): 
                            if re.search(rf'\b{algo}\b', line, re.IGNORECASE): 
                                result['vulnerabilities'].append({ 
                                    'algorithm': algo, 
                                    'line': i, 
                                    'context': line.strip()[:80], 
                                    'risk': info['risk'], 
                                    'threat': info['threat'], 
                                    'migration': info['migration'] 
                                }) 
                                break 
        except Exception as e: 
            result['error'] = str(e) 
        return result 
 
    def scan_project(self, path): 
        results = [] 
        for ext in ['*.py', '*.js', '*.java', '*.go', '*.rs']: 
            for file_path in Path(path).rglob(ext): 
                result = self.scan_file(str(file_path)) 
                if result['vulnerabilities']: 
                    results.append(result) 
        return results 
 
    def generate_report(self, results): 
        lines = ["="*60, "PQC HACKING TOOL - SECURITY REPORT", "="*60] 
        for r in results: 
            lines.append(f"\n[*] {r['file']}") 
            for v in r['vulnerabilities']: 
                lines.append(f"    [!] Line {v['line']}: {v['algorithm']} (Risk: {v['risk']})") 
                lines.append(f"        Context: {v['context']}") 
                lines.append(f"        Threat: {v['threat']}") 
                lines.append(f"        Migrate to: {v['migration']}") 
        return "\n".join(lines) 
 
if __name__ == "__main__": 
    if len(sys.argv) 
        tool = PQCHackingTool() 
        results = tool.scan_project(sys.argv[1]) 
        print(tool.generate_report(results)) 
    else: 
        print("Usage: python pqc_hacking_tool.py ^<directory^>") 
