"""
Enhanced AI Code Analyzer with Advanced Features & GitHub Integration
Supports: Local files, GitHub repos, PRs, and security analysis
"""

import ast
import re
import time
from typing import Dict, List, Optional, Tuple
import requests
from dataclasses import dataclass
from enum import Enum


class Severity(Enum):
    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class Issue:
    line_number: int
    severity: Severity
    issue_type: str
    description: str
    code_snippet: str
    suggested_fix: Optional[str] = None
    explanation: Optional[str] = None
    cwe_id: Optional[str] = None  # Common Weakness Enumeration ID


class EnhancedCodeAnalyzer:
    """Enhanced analyzer with security, performance, and GitHub integration"""
    
    def __init__(self, hf_token: Optional[str] = None, github_token: Optional[str] = None):
        self.hf_token = hf_token
        self.github_token = github_token
        self.issues: List[Issue] = []
        
    def analyze_code(self, code: str, options: Dict) -> Dict:
        """Main analysis with all features"""
        start_time = time.time()
        self.issues = []
        
        # Run all analysis types
        if options.get('syntax', True):
            self._check_syntax(code)
        
        if options.get('security', True):
            self._check_security(code)
        
        if options.get('performance', True):
            self._check_performance(code)
        
        if options.get('code_smells', True):
            self._check_code_smells(code)
        
        if options.get('complexity', True):
            complexity_score = self._calculate_complexity(code)
        else:
            complexity_score = 0.0
        
        if options.get('dead_code', True):
            self._detect_dead_code(code)
        
        if options.get('type_hints', True):
            self._suggest_type_hints(code)
        
        # Calculate metrics
        metrics = self._calculate_metrics(code)
        
        # Generate summary
        summary = self._generate_summary(metrics)
        
        processing_time = (time.time() - start_time) * 1000
        
        return {
            'total_issues': len(self.issues),
            'critical': sum(1 for i in self.issues if i.severity == Severity.CRITICAL),
            'errors': sum(1 for i in self.issues if i.severity == Severity.ERROR),
            'warnings': sum(1 for i in self.issues if i.severity == Severity.WARNING),
            'info': sum(1 for i in self.issues if i.severity == Severity.INFO),
            'complexity_score': complexity_score,
            'maintainability_index': metrics['maintainability'],
            'security_score': metrics['security_score'],
            'performance_score': metrics['performance_score'],
            'issues': [self._issue_to_dict(i) for i in self.issues],
            'summary': summary,
            'processing_time_ms': processing_time,
            'metrics': metrics
        }
    
    def _check_syntax(self, code: str):
        """Enhanced syntax checking"""
        try:
            tree = ast.parse(code)
            # Check for common syntax patterns
            self._check_ast_patterns(tree, code)
        except SyntaxError as e:
            self.issues.append(Issue(
                line_number=e.lineno or 1,
                severity=Severity.ERROR,
                issue_type='syntax',
                description=f"Syntax Error: {e.msg}",
                code_snippet=e.text or "",
                suggested_fix=self._suggest_syntax_fix(e)
            ))
    
    def _check_security(self, code: str):
        """Security vulnerability detection"""
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            # SQL Injection
            if re.search(r'execute\s*\(["\'].*%s.*["\']\s*%', line):
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.CRITICAL,
                    issue_type='security',
                    description='SQL Injection vulnerability detected',
                    code_snippet=line.strip(),
                    suggested_fix='Use parameterized queries: cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))',
                    explanation='Never use string formatting with SQL queries',
                    cwe_id='CWE-89'
                ))
            
            # Command Injection
            if re.search(r'os\.system\(.*\+.*\)|subprocess\.(call|run)\(.*\+.*\)', line):
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.CRITICAL,
                    issue_type='security',
                    description='Command Injection vulnerability',
                    code_snippet=line.strip(),
                    suggested_fix='Use subprocess with list arguments: subprocess.run(["command", arg1, arg2])',
                    explanation='Never concatenate user input into shell commands',
                    cwe_id='CWE-78'
                ))
            
            # Hardcoded credentials
            if re.search(r'(password|passwd|pwd|secret|token|api_key)\s*=\s*["\'][^"\']+["\']', line, re.IGNORECASE):
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.CRITICAL,
                    issue_type='security',
                    description='Hardcoded credentials detected',
                    code_snippet=line.strip(),
                    suggested_fix='Use environment variables: password = os.getenv("DB_PASSWORD")',
                    explanation='Never hardcode sensitive credentials in code',
                    cwe_id='CWE-798'
                ))
            
            # Weak cryptography
            if 'md5' in line.lower() or 'sha1' in line.lower():
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.WARNING,
                    issue_type='security',
                    description='Weak cryptographic algorithm',
                    code_snippet=line.strip(),
                    suggested_fix='Use SHA-256 or better: hashlib.sha256(data.encode())',
                    explanation='MD5 and SHA1 are cryptographically broken',
                    cwe_id='CWE-327'
                ))
            
            # eval() usage
            if re.search(r'\beval\s*\(', line):
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.CRITICAL,
                    issue_type='security',
                    description='Dangerous eval() usage',
                    code_snippet=line.strip(),
                    suggested_fix='Use ast.literal_eval() for safe evaluation or parse manually',
                    explanation='eval() can execute arbitrary code',
                    cwe_id='CWE-95'
                ))
            
            # Pickle usage
            if 'pickle.loads' in line:
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.WARNING,
                    issue_type='security',
                    description='Unsafe deserialization with pickle',
                    code_snippet=line.strip(),
                    suggested_fix='Use json.loads() for untrusted data',
                    explanation='Pickle can execute arbitrary code during deserialization',
                    cwe_id='CWE-502'
                ))
    
    def _check_performance(self, code: str):
        """Performance bottleneck detection"""
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            # List concatenation in loop
            if '+=' in line and any(word in line for word in ['list', 'array', '[]']):
                if i > 1 and 'for' in lines[i-2]:
                    self.issues.append(Issue(
                        line_number=i,
                        severity=Severity.WARNING,
                        issue_type='performance',
                        description='Inefficient list concatenation in loop',
                        code_snippet=line.strip(),
                        suggested_fix='Use list.append() or list comprehension',
                        explanation='List concatenation is O(n), append is O(1)'
                    ))
            
            # Multiple string concatenations
            if line.count('+') > 2 and '"' in line or "'" in line:
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.INFO,
                    issue_type='performance',
                    description='Multiple string concatenations',
                    code_snippet=line.strip(),
                    suggested_fix='Use f-string or str.join(): f"{var1}{var2}{var3}"',
                    explanation='String concatenation creates intermediate objects'
                ))
            
            # Global variable in loop
            if 'global' in line:
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.WARNING,
                    issue_type='performance',
                    description='Global variable usage affects performance',
                    code_snippet=line.strip(),
                    suggested_fix='Use local variables or pass as parameters',
                    explanation='Global lookups are slower than local lookups'
                ))
    
    def _check_code_smells(self, code: str):
        """Code smell detection"""
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Long line
            if len(line) > 120:
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.INFO,
                    issue_type='style',
                    description='Line too long (>120 characters)',
                    code_snippet=line[:50] + '...',
                    suggested_fix='Break into multiple lines or refactor'
                ))
            
            # Magic numbers
            if re.search(r'\b\d{4,}\b', line) and 'return' not in line:
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.INFO,
                    issue_type='style',
                    description='Magic number detected',
                    code_snippet=line.strip(),
                    suggested_fix='Define as named constant: MAX_RETRIES = 1000',
                    explanation='Magic numbers reduce code readability'
                ))
            
            # Commented out code
            if line.strip().startswith('#') and any(char in line for char in ['(', ')', '=', '.']):
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.INFO,
                    issue_type='style',
                    description='Commented out code',
                    code_snippet=line.strip(),
                    suggested_fix='Remove commented code, use version control',
                    explanation='Commented code creates clutter'
                ))
            
            # Multiple statements on one line
            if line.count(';') > 0:
                self.issues.append(Issue(
                    line_number=i,
                    severity=Severity.WARNING,
                    issue_type='style',
                    description='Multiple statements on one line',
                    code_snippet=line.strip(),
                    suggested_fix='Put each statement on separate line'
                ))
    
    def _detect_dead_code(self, code: str):
        """Detect unused variables and functions"""
        try:
            tree = ast.parse(code)
            defined_names = set()
            used_names = set()
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    defined_names.add(node.name)
                elif isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            defined_names.add(target.id)
                elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                    used_names.add(node.id)
            
            unused = defined_names - used_names
            for name in unused:
                if not name.startswith('_'):  # Ignore private variables
                    self.issues.append(Issue(
                        line_number=1,  # Would need more analysis to get exact line
                        severity=Severity.INFO,
                        issue_type='dead_code',
                        description=f"Unused variable or function: '{name}'",
                        code_snippet='',
                        suggested_fix=f'Remove unused {name} or prefix with _ if intentional'
                    ))
        except:
            pass
    
    def _suggest_type_hints(self, code: str):
        """Suggest adding type hints"""
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Function without type hints
            if re.match(r'^\s*def\s+\w+\s*\([^)]*\)\s*:', line):
                if '->' not in line and ':' not in line.split('(')[1].split(')')[0]:
                    self.issues.append(Issue(
                        line_number=i,
                        severity=Severity.INFO,
                        issue_type='type_hint',
                        description='Function missing type hints',
                        code_snippet=line.strip(),
                        suggested_fix='def function(param: str) -> int:',
                        explanation='Type hints improve code clarity and catch bugs'
                    ))
    
    def _calculate_complexity(self, code: str) -> float:
        """Calculate cyclomatic complexity"""
        try:
            tree = ast.parse(code)
            complexity = 1  # Base complexity
            
            for node in ast.walk(tree):
                if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                    complexity += 1
                elif isinstance(node, ast.BoolOp):
                    complexity += len(node.values) - 1
            
            return complexity
        except:
            return 1.0
    
    def _calculate_metrics(self, code: str) -> Dict:
        """Calculate various code metrics"""
        lines = code.split('\n')
        code_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')]
        
        # Count issues by type
        security_issues = sum(1 for i in self.issues if i.issue_type == 'security')
        performance_issues = sum(1 for i in self.issues if i.issue_type == 'performance')
        
        # Calculate scores (0-100)
        security_score = max(0, 100 - (security_issues * 20))
        performance_score = max(0, 100 - (performance_issues * 10))
        
        errors = sum(1 for i in self.issues if i.severity == Severity.ERROR)
        warnings = sum(1 for i in self.issues if i.severity == Severity.WARNING)
        
        maintainability = max(20, 100 - (errors * 15) - (warnings * 5))
        
        return {
            'total_lines': len(lines),
            'code_lines': len(code_lines),
            'comment_lines': len([l for l in lines if l.strip().startswith('#')]),
            'blank_lines': len([l for l in lines if not l.strip()]),
            'security_score': security_score,
            'performance_score': performance_score,
            'maintainability': maintainability,
            'code_to_comment_ratio': len(code_lines) / max(1, len(lines) - len(code_lines))
        }
    
    def _generate_summary(self, metrics: Dict) -> str:
        """Generate analysis summary"""
        critical = sum(1 for i in self.issues if i.severity == Severity.CRITICAL)
        errors = sum(1 for i in self.issues if i.severity == Severity.ERROR)
        warnings = sum(1 for i in self.issues if i.severity == Severity.WARNING)
        
        status = "🔴 CRITICAL" if critical > 0 else "⚠️ NEEDS ATTENTION" if errors > 0 else "✅ GOOD"
        
        return f"""
╔════════════════════════════════════════════════════════════╗
║           ENHANCED CODE ANALYSIS REPORT                     ║
╚════════════════════════════════════════════════════════════╝

📊 OVERVIEW
  Status: {status}
  Total Issues: {len(self.issues)}
    🔴 Critical: {critical}
    ❌ Errors: {errors}
    ⚠️  Warnings: {warnings}
    ℹ️  Info: {sum(1 for i in self.issues if i.severity == Severity.INFO)}

📈 CODE METRICS
  Lines of Code: {metrics['code_lines']}
  Comment Lines: {metrics['comment_lines']}
  Complexity: {self._calculate_complexity(''):.2f}
  Maintainability: {metrics['maintainability']:.1f}/100

🔒 SECURITY SCORE: {metrics['security_score']:.1f}/100
  {self._get_score_emoji(metrics['security_score'])} {self._get_score_label(metrics['security_score'])}

⚡ PERFORMANCE SCORE: {metrics['performance_score']:.1f}/100
  {self._get_score_emoji(metrics['performance_score'])} {self._get_score_label(metrics['performance_score'])}

💡 RECOMMENDATIONS
  {self._generate_recommendations()}
"""
    
    def _get_score_emoji(self, score: float) -> str:
        if score >= 80: return "🟢"
        if score >= 60: return "🟡"
        return "🔴"
    
    def _get_score_label(self, score: float) -> str:
        if score >= 80: return "Excellent"
        if score >= 60: return "Good"
        if score >= 40: return "Needs Improvement"
        return "Critical"
    
    def _generate_recommendations(self) -> str:
        recommendations = []
        
        security_issues = [i for i in self.issues if i.issue_type == 'security']
        if security_issues:
            recommendations.append("• Fix security vulnerabilities immediately")
        
        performance_issues = [i for i in self.issues if i.issue_type == 'performance']
        if performance_issues:
            recommendations.append("• Optimize performance bottlenecks")
        
        if not recommendations:
            recommendations.append("• Code quality is good! Keep it up!")
        
        return "\n  ".join(recommendations)
    
    def _suggest_syntax_fix(self, error: SyntaxError) -> Optional[str]:
        """Generate syntax fix suggestions"""
        if 'invalid syntax' in str(error.msg):
            return "Check for missing colons, parentheses, or quotes"
        elif 'EOF' in str(error.msg):
            return "Check for unclosed brackets, quotes, or parentheses"
        return None
    
    def _check_ast_patterns(self, tree: ast.AST, code: str):
        """Check AST for common patterns"""
        for node in ast.walk(tree):
            # Catch Exception without using it
            if isinstance(node, ast.ExceptHandler):
                if node.type and isinstance(node.type, ast.Name):
                    if node.type.id == 'Exception' and not node.name:
                        self.issues.append(Issue(
                            line_number=node.lineno,
                            severity=Severity.INFO,
                            issue_type='style',
                            description='Catching Exception without using it',
                            code_snippet='',
                            suggested_fix='except Exception as e: # Use e for logging'
                        ))
    
    def _issue_to_dict(self, issue: Issue) -> Dict:
        """Convert Issue to dictionary"""
        return {
            'line_number': issue.line_number,
            'severity': issue.severity.value,
            'issue_type': issue.issue_type,
            'description': issue.description,
            'code_snippet': issue.code_snippet,
            'suggested_fix': issue.suggested_fix,
            'explanation': issue.explanation,
            'cwe_id': issue.cwe_id
        }
    
    # === GITHUB INTEGRATION ===
    
    def analyze_github_repo(self, repo_url: str, branch: str = 'main') -> Dict:
        """Analyze entire GitHub repository"""
        if not self.github_token:
            return {'error': 'GitHub token required'}
        
        # Parse repo URL
        parts = repo_url.replace('https://github.com/', '').split('/')
        if len(parts) < 2:
            return {'error': 'Invalid GitHub URL'}
        
        owner, repo = parts[0], parts[1]
        
        # Get repository contents
        headers = {'Authorization': f'token {self.github_token}'}
        api_url = f'https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1'
        
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            tree = response.json()
            
            python_files = [
                item for item in tree.get('tree', [])
                if item['path'].endswith('.py')
            ]
            
            results = []
            for file_info in python_files[:10]:  # Limit to 10 files for demo
                file_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_info['path']}"
                file_response = requests.get(file_url, headers=headers)
                
                if file_response.status_code == 200:
                    import base64
                    content = base64.b64decode(file_response.json()['content']).decode('utf-8')
                    
                    analysis = self.analyze_code(content, {
                        'syntax': True,
                        'security': True,
                        'performance': True,
                        'code_smells': True,
                        'complexity': True
                    })
                    
                    results.append({
                        'file': file_info['path'],
                        'analysis': analysis
                    })
            
            return {
                'repo': f"{owner}/{repo}",
                'branch': branch,
                'files_analyzed': len(results),
                'results': results
            }
            
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
    
    def analyze_github_pr(self, pr_url: str) -> Dict:
        """Analyze GitHub Pull Request changes"""
        if not self.github_token:
            return {'error': 'GitHub token required'}
        
        # Parse PR URL: https://github.com/owner/repo/pull/123
        parts = pr_url.replace('https://github.com/', '').split('/')
        if len(parts) < 4 or parts[2] != 'pull':
            return {'error': 'Invalid PR URL'}
        
        owner, repo, _, pr_number = parts[0], parts[1], parts[2], parts[3]
        
        headers = {'Authorization': f'token {self.github_token}'}
        api_url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files'
        
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            files = response.json()
            
            results = []
            for file_info in files:
                if file_info['filename'].endswith('.py'):
                    # Analyze the patch/changes
                    patch = file_info.get('patch', '')
                    
                    # Extract added lines
                    added_lines = [
                        line[1:] for line in patch.split('\n')
                        if line.startswith('+') and not line.startswith('+++')
                    ]
                    
                    if added_lines:
                        code = '\n'.join(added_lines)
                        analysis = self.analyze_code(code, {
                            'syntax': True,
                            'security': True,
                            'performance': True
                        })
                        
                        results.append({
                            'file': file_info['filename'],
                            'additions': file_info['additions'],
                            'deletions': file_info['deletions'],
                            'analysis': analysis
                        })
            
            return {
                'pr': f"{owner}/{repo}#{pr_number}",
                'files_changed': len(results),
                'results': results
            }
            
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
    
    def create_github_issue(self, repo_url: str, title: str, body: str) -> Dict:
        """Create GitHub issue for detected problems"""
        if not self.github_token:
            return {'error': 'GitHub token required'}
        
        parts = repo_url.replace('https://github.com/', '').split('/')
        if len(parts) < 2:
            return {'error': 'Invalid GitHub URL'}
        
        owner, repo = parts[0], parts[1]
        
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        api_url = f'https://api.github.com/repos/{owner}/{repo}/issues'
        
        data = {
            'title': title,
            'body': body,
            'labels': ['bug', 'automated']
        }
        
        try:
            response = requests.post(api_url, headers=headers, json=data)
            response.raise_for_status()
            issue = response.json()
            
            return {
                'success': True,
                'issue_number': issue['number'],
                'url': issue['html_url']
            }
            
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}


# Example usage
if __name__ == "__main__":
    # Test code with various issues
    test_code = '''
import os
import hashlib

password = "admin123"  # Hardcoded password
api_key = "sk_live_123456"  # Hardcoded API key

def get_user(user_id):
    # SQL Injection vulnerability
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)
    return cursor.fetchone()

def hash_password(pwd):
    # Weak cryptography
    return hashlib.md5(pwd.encode()).hexdigest()

def process_data(items):
    result = []
    for item in items:
        result += [item * 2]  # Inefficient list concatenation
    return result

def calculate_average(numbers):
    return sum(numbers) / len(numbers)  # Division by zero risk

# Dead code
unused_variable = 42

def unused_function():
    pass
'''
    
    analyzer = EnhancedCodeAnalyzer()
    results = analyzer.analyze_code(test_code, {
        'syntax': True,
        'security': True,
        'performance': True,
        'code_smells': True,
        'complexity': True,
        'dead_code': True,
        'type_hints': True
    })
    
    print(results['summary'])
    print(f"\n📋 Found {results['total_issues']} issues")
    print(f"🔒 Security Score: {results['security_score']}/100")
    print(f"⚡ Performance Score: {results['performance_score']}/100")