# 🚀 Enhanced AI Code Analyzer

AI-powered code analysis tool with security scanning, GitHub integration, and auto-fix capabilities.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## ✨ Features

- 🔒 **Security Scan** - Detects SQL injection, XSS, hardcoded credentials
- ⚡ **Performance** - Finds bottlenecks and optimization opportunities
- 🐙 **GitHub Integration** - Analyze repos, PRs, create issues
- 🔧 **Auto-Fix** - AI-powered automatic code fixes
- 📊 **Metrics** - Complexity, maintainability, quality scores

## 🚀 Quick Start

### 1. Install

```bash
# Clone repository
git clone https://github.com/yourusername/enhanced-code-analyzer.git
cd enhanced-code-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure

Create `.env` file:

```env
HF_TOKEN=hf_your_huggingface_token_here
GITHUB_TOKEN=ghp_your_github_token_here  # Optional
```

Get tokens:
- **HuggingFace**: https://huggingface.co/settings/tokens (Required)
- **GitHub**: https://github.com/settings/tokens (Optional)

### 3. Run

**Web Interface:**
```bash
streamlit run app.py
```
Open: http://localhost:8501

**API Server:**
```bash
python -m uvicorn enhanced_api_server:app --reload
```
Docs: http://localhost:8000/docs

## 💡 Usage

### Python Code

```python
from enhanced_analyzer import EnhancedCodeAnalyzer

analyzer = EnhancedCodeAnalyzer(hf_token="your_token")

results = analyzer.analyze_code("""
password = "admin123"  # Security issue
def divide(a, b):
    return a / b  # Potential error
""", {'security': True, 'performance': True})

print(f"Issues: {results['total_issues']}")
print(f"Security Score: {results['security_score']}/100")
```

### API Request

```bash
curl -X POST "http://localhost:8000/api/v2/analyze" \
  -H "X-HuggingFace-Token: YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"code": "def test():\n    pass", "model_name": "codellama"}'
```

## 📚 Documentation

- **API Docs**: http://localhost:8000/docs
- **Full README**: [Detailed version](README_FULL.md)
- **Examples**: `/examples` folder

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | `pip install -r requirements.txt` |
| Port in use | Use `--server.port 8502` for Streamlit |
| Invalid token | Verify at https://huggingface.co/settings/tokens |
| Import error | Rename files: `mv "Code_Analyzer_with_GitHub_Integration.py" enhanced_analyzer.py` |

## 🤖 AI Models

- **CodeLlama** ⭐ - Best for Python (Recommended)
- **StarCoder** - Multi-language support
- **WizardCoder** - Complex bug detection
- **Mistral** - Detailed explanations

## 📊 What It Detects

**Security**: SQL injection, XSS, hardcoded credentials, weak crypto, command injection

**Performance**: Inefficient loops, memory leaks, slow algorithms

**Quality**: Dead code, missing type hints, code smells, complexity issues

## 🤝 Contributing

Contributions welcome! Please check [CONTRIBUTING.md](CONTRIBUTING.md)

```bash
git checkout -b feature/your-feature
# Make changes
git commit -m "Add: feature description"
git push origin feature/your-feature
```

## 📄 License

MIT License - See [LICENSE](LICENSE) file

## 🙏 Credits

Built with: Streamlit • FastAPI • HuggingFace • Plotly

---

**Made with ❤️ for developers** | [⭐ Star this repo](https://github.com/yourusername/enhanced-code-analyzer)
