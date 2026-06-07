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
            'RSA': {
                'threat': "Shor's algorithm factors large integers exponentially faster",
                'migration': 'ML-KEM-768 or ML-DSA-65',
                'risk': 95
            },
            'ECDSA': {
                'threat': "Shor's algorithm solves elliptic curve discrete logarithm",
                'migration': 'ML-DSA-65',
                'risk': 95
            },
            'Ed25519': {
                'threat': "Vulnerable to Shor's algorithm on Edwards curves",
                'migration': 'SLH-DSA or FALCON',
                'risk': 85
            },
            'ECDH': {
                'threat': "Key exchange broken by Shor's algorithm",
                'migration': 'ML-KEM (Kyber) for key exchange',
                'risk': 95
            },
            'AES-128': {
                'threat': "Grover's algorithm reduces effective key size to 64 bits",
                'migration': 'AES-256',
                'risk': 70
            }
        }
    
    def scan_file(self, filepath: str) -> Dict:
        result = {'file': filepath, 'vulnerabilities': []}
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                
                for algo, info in self.vulnerability_database.items():
                    pattern = rf'\b{algo}[-\s]?(?:128|192|256|1024|2048|3072|4096)?\b'
                    matches = list(re.finditer(pattern, content, re.IGNORECASE))
                    
                    for match in matches:
                        line_num = content[:match.start()].count('\n') + 1
                        result['vulnerabilities'].append({
                            'algorithm': algo,
                            'line': line_num,
                            'context': lines[line_num-1].strip()[:100],
                            'risk': info['risk'],
                            'threat': info['threat'],
                            'migration': info['migration']
                        })
        except Exception as e:
            pass
        return result
    
    def scan_project(self, path: str) -> List[Dict]:
        results = []
        extensions = ['.py', '.js', '.ts', '.java', '.go', '.rs', '.c', '.cpp', '.cs', '.md', '.txt']
        path_obj = Path(path)
        
        for ext in extensions:
            for file_path in path_obj.rglob(f'*{ext}'):
                if file_path.is_file():
                    result = self.scan_file(str(file_path))
                    if result['vulnerabilities']:
                        results.append(result)
        return results
    
    def generate_report(self, results: List[Dict]) -> str:
        if not results:
            return "No quantum-vulnerable cryptography found."
        
        lines = []
        lines.append("=" * 60)
        lines.append("PQC HACKING TOOL - SECURITY ASSESSMENT REPORT")
        lines.append(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("=" * 60)
        
        total_risks = 0
        critical_count = 0
        
        for result in results:
            lines.append(f"\n[*] {result['file']}")
            for vuln in result['vulnerabilities']:
                total_risks += 1
                if vuln['risk'] >= 90:
                    critical_count += 1
                    risk_symbol = "[!] CRITICAL"
                elif vuln['risk'] >= 70:
                    risk_symbol = "[W] HIGH"
                else:
                    risk_symbol = "[I] MEDIUM"
                
                lines.append(f"\n    {risk_symbol} | Line {vuln['line']}")
                lines.append(f"    Algorithm: {vuln['algorithm']}")
                lines.append(f"    Context: {vuln['context']}")
                lines.append(f"    Threat: {vuln['threat']}")
                lines.append(f"    Migrate to: {vuln['migration']}")
        
        lines.append("\n" + "=" * 60)
        lines.append(f"SUMMARY: {len(results)} files affected | {total_risks} total risks")
        
        if critical_count > 0:
            lines.append(f"\n[!!!] CRITICAL: {critical_count} quantum-vulnerable findings!")
            lines.append("    Immediate migration to NIST PQC standards required.")
        
        lines.append("=" * 60)
        return "\n".join(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("PQC Hacking Tool - Post-Quantum Cryptography Vulnerability Scanner")
        print("=" * 50)
        print("Usage: python pqc_hacking_tool.py <directory_to_scan>")
        print("\nExample:")
        print("  python pqc_hacking_tool.py ./my_project")
        print("  python pqc_hacking_tool.py C:\\path\\to\\code")
        sys.exit(1)
    
    target_path = sys.argv[1]
    
    if not os.path.exists(target_path):
        print(f"[!] Error: Path '{target_path}' does not exist")
        sys.exit(1)
    
    print(f"[*] Scanning: {target_path}")
    tool = PQCHackingTool()
    results = tool.scan_project(target_path)
    print(tool.generate_report(results))