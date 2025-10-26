"""
Enhanced Streamlit App with Modern UI/UX, Animations & Custom Background
Run with: streamlit run fixed_streamlit_app.py
"""

import streamlit as st
import os
import json
import time
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import base64
from Code_Analyzer_with_GitHub_Integration import EnhancedCodeAnalyzer

# Page config
st.set_page_config(
    page_title="🚀 FIX FORGE",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to load background image
def get_base64_image(image_path):
    """Convert image to base64 for CSS background"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Try to load custom background
bg_image = get_base64_image("background.jpg")

# Enhanced Custom CSS with Animations
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;900&display=swap');
    
    * {{
        font-family: 'Poppins', sans-serif;
    }}
    
    .stApp {{
        background: {'url(data:image/jpg;base64,' + bg_image + ') no-repeat center center fixed' if bg_image else 'linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%)'};
        background-size: cover;
    }}
    
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(8px);
        z-index: -1;
    }}
    
    @keyframes gradientShift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    .main-header {{
        font-size: 4rem;
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 50%, #a6c1ee 100%);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 900;
        margin-bottom: 0.5rem;
        animation: gradientShift 5s ease infinite, float 3s ease-in-out infinite;
    }}
    
    @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
    }}
    
    .sub-header {{
        text-align: center;
        color: #fff;
        font-size: 1.4rem;
        margin-bottom: 2rem;
        animation: fadeInUp 1s ease;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}
    
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .critical-issue {{
        background: linear-gradient(135deg, rgba(255, 107, 107, 0.9) 0%, rgba(201, 42, 42, 0.9) 100%);
        border-left: 5px solid #ff1744;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 15px;
        color: white;
        animation: pulse 2s infinite;
    }}
    
    @keyframes pulse {{
        0%, 100% {{ box-shadow: 0 8px 25px rgba(255, 23, 68, 0.4); }}
        50% {{ box-shadow: 0 8px 35px rgba(255, 23, 68, 0.7); }}
    }}
    
    .error-issue {{
        background: rgba(255, 235, 238, 0.95);
        border-left: 5px solid #f44336;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 15px;
        transition: all 0.3s;
        color: #333;
    }}
    
    .warning-issue {{
        background: rgba(255, 243, 224, 0.95);
        border-left: 5px solid #ff9800;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 15px;
        transition: all 0.3s;
        color: #333;
    }}
    
    .info-issue {{
        background: rgba(227, 242, 253, 0.95);
        border-left: 5px solid #2196f3;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 15px;
        transition: all 0.3s;
        color: #333;
    }}
    
    .stButton>button {{
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 1rem 2.5rem;
        font-size: 1.1rem;
        font-weight: 700;
        transition: all 0.4s;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }}
    
    .stButton>button:hover {{
        transform: scale(1.08) translateY(-3px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.6);
    }}
    
    .feature-badge {{
        display: inline-block;
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 0.7rem 1.5rem;
        border-radius: 30px;
        margin: 0.5rem;
        font-size: 1rem;
        font-weight: 700;
        box-shadow: 0 5px 15px rgba(245, 87, 108, 0.4);
        transition: all 0.3s;
    }}
    
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, rgba(30, 30, 60, 0.95) 0%, rgba(20, 20, 40, 0.95) 100%);
        backdrop-filter: blur(20px);
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚀 FIX FORGE</h1>', unsafe_allow_html=True)
st.markdown("""
<p class="sub-header">
🔒 Security • ⚡ Performance • 🔀 GitHub Integration • 🎯 Advanced Analysis
</p>
""", unsafe_allow_html=True)

# Feature badges
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <span class="feature-badge">✅ FREE</span>
    <span class="feature-badge">🔒 Security Scan</span>
    <span class="feature-badge">⚡ Performance</span>
    <span class="feature-badge">🔀 GitHub</span>
    <span class="feature-badge">🤖 AI Powered</span>
    <span class="feature-badge">📊 Metrics</span>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://huggingface.co/front/assets/huggingface_logo.svg", width=200)
    st.header("⚙️ Configuration")
    
    st.markdown("### 🔑 API Tokens")
    hf_token = st.text_input(
        "HuggingFace Token",
        type="password",
        value=os.getenv('HF_TOKEN', ''),
        help="Get free token: https://huggingface.co/settings/tokens"
    )
    
    github_token = st.text_input(
        "GitHub Token (Optional)",
        type="password",
        value=os.getenv('GITHUB_TOKEN', ''),
        help="For GitHub integration: https://github.com/settings/tokens"
    )
    
    if hf_token:
        st.success("✅ HuggingFace configured")
    else:
        st.warning("⚠️ Add HF token for AI features")
    
    if github_token:
        st.success("✅ GitHub configured")
    
    st.divider()
    
    st.header("🔍 Analysis Options")
    run_syntax = st.checkbox("✓ Syntax Analysis", value=True)
    run_security = st.checkbox("🔒 Security Scan", value=True)
    run_performance = st.checkbox("⚡ Performance Check", value=True)
    run_code_smells = st.checkbox("👃 Code Smells", value=True)
    run_complexity = st.checkbox("📊 Complexity Metrics", value=True)
    run_dead_code = st.checkbox("💀 Dead Code Detection", value=True)
    run_type_hints = st.checkbox("🏷️ Type Hints", value=True)

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📝 Code Input", 
    "📊 Analysis Results", 
    "🔀 GitHub Integration",
    "📚 Documentation"
])

# Tab 1: Code Input
with tab1:
    st.header("Enter Your Code")
    
    input_method = st.radio(
        "Input Method",
        ["✏️ Paste Code", "📁 Upload File", "🔀 GitHub URL"],
        horizontal=True
    )
    
    code_input = ""
    file_name = "input.py"
    
    if input_method == "✏️ Paste Code":
        code_input = st.text_area(
            "Python Code",
            height=400,
            placeholder="""# Example: Code with security issues
import os

password = "admin123"  # Hardcoded password!
api_key = "sk_live_xyz"  # Hardcoded API key!

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = '%s'" % user_id  # SQL Injection!
    return execute(query)

def calculate_avg(numbers):
    return sum(numbers) / len(numbers)  # Division by zero risk!

# Add your code here...
""",
            help="Paste your Python code for comprehensive analysis"
        )
    
    elif input_method == "📁 Upload File":
        uploaded_file = st.file_uploader(
            "Choose Python file",
            type=['py'],
            help="Upload .py file"
        )
        
        if uploaded_file:
            file_name = uploaded_file.name
            code_input = uploaded_file.getvalue().decode("utf-8")
            st.success(f"✅ Loaded: {file_name}")
            
            with st.expander("👀 Preview Code"):
                st.code(code_input, language='python')
    
    else:  # GitHub URL
        st.markdown("### 🔀 Analyze from GitHub")
        
        github_input_type = st.radio(
            "GitHub Source",
            ["📦 Repository", "🔀 Pull Request"],
            horizontal=True
        )
        
        if github_input_type == "📦 Repository":
            col1, col2 = st.columns([3, 1])
            with col1:
                repo_url = st.text_input(
                    "Repository URL",
                    placeholder="https://github.com/username/repo"
                )
            with col2:
                branch = st.text_input("Branch", value="main")
            
            if st.button("🔍 Analyze Repository", type="primary"):
                if not github_token:
                    st.error("❌ GitHub token required!")
                elif repo_url:
                    with st.spinner("🔄 Analyzing repository..."):
                        try:
                            analyzer = EnhancedCodeAnalyzer(
                                hf_token=hf_token if hf_token else None,
                                github_token=github_token
                            )
                            results = analyzer.analyze_github_repo(repo_url, branch)
                            
                            if 'error' in results:
                                st.error(f"❌ Error: {results['error']}")
                            else:
                                st.session_state.github_repo_results = results
                                st.success("✅ Repository analyzed!")
                                st.info("👉 Check GitHub Integration tab for results")
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")
        
        elif github_input_type == "🔀 Pull Request":
            pr_url = st.text_input(
                "Pull Request URL",
                placeholder="https://github.com/username/repo/pull/123"
            )
            
            if st.button("🔍 Analyze PR", type="primary"):
                if not github_token:
                    st.error("❌ GitHub token required!")
                elif pr_url:
                    with st.spinner("🔄 Analyzing PR changes..."):
                        try:
                            analyzer = EnhancedCodeAnalyzer(
                                hf_token=hf_token if hf_token else None,
                                github_token=github_token
                            )
                            results = analyzer.analyze_github_pr(pr_url)
                            
                            if 'error' in results:
                                st.error(f"❌ Error: {results['error']}")
                            else:
                                st.session_state.github_pr_results = results
                                st.success("✅ PR analyzed!")
                                st.info("👉 Check GitHub Integration tab")
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")
    
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        analyze_button = st.button(
            "🔍 Analyze Code",
            type="primary",
            use_container_width=True,
            disabled=not code_input
        )
    
    with col2:
        clear_button = st.button("🗑️ Clear", use_container_width=True)
    
    # Handle analyze button click
    if analyze_button and code_input:
        with st.spinner("🔄 Analyzing code... This may take a moment."):
            try:
                # Store original code
                st.session_state.original_code = code_input
                st.session_state.file_name = file_name
                
                # Initialize analyzer with tokens
                analyzer = EnhancedCodeAnalyzer(
                    hf_token=hf_token if hf_token else None,
                    github_token=github_token if github_token else None
                )
                
                # Create analysis options dictionary matching the analyzer's expected format
                options = {
                    'syntax': run_syntax,
                    'security': run_security,
                    'performance': run_performance,
                    'code_smells': run_code_smells,
                    'complexity': run_complexity,
                    'dead_code': run_dead_code,
                    'type_hints': run_type_hints
                }
                
                # Run analysis - using the correct method signature
                results = analyzer.analyze_code(code_input, options)
                
                # Store results in session state
                st.session_state.analysis_results = results
                
                st.success("✅ Analysis complete! Check the 'Analysis Results' tab.")
                st.balloons()
                
                # Show quick preview
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Issues", results.get('total_issues', 0))
                with col2:
                    st.metric("Critical", results.get('critical', 0))
                with col3:
                    st.metric("Security Score", f"{results.get('security_score', 0)}/100")
                
            except Exception as e:
                st.error(f"❌ Analysis failed: {str(e)}")
                with st.expander("🐛 Error Details"):
                    st.exception(e)
    
    # Handle clear button
    if clear_button:
        for key in ['analysis_results', 'original_code', 'file_name', 'github_repo_results', 'github_pr_results']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# Tab 2: Analysis Results
with tab2:
    st.header("📊 Analysis Results")
    
    if 'analysis_results' not in st.session_state:
        st.info("👈 Enter code in the 'Code Input' tab and click 'Analyze Code'")
        
        with st.expander("📖 See Example Analysis"):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Issues", "12", delta="-3")
            with col2:
                st.metric("Security Score", "78/100", delta="12")
            with col3:
                st.metric("Performance", "85/100", delta="5")
            with col4:
                st.metric("Maintainability", "82/100", delta="8")
    
    else:
        results = st.session_state.analysis_results
        
        # Metrics row
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("📋 Issues", results.get('total_issues', 0))
        
        with col2:
            critical = results.get('critical', 0)
            st.metric(
                "🔴 Critical",
                critical,
                delta="Urgent!" if critical > 0 else "None",
                delta_color="inverse" if critical > 0 else "off"
            )
        
        with col3:
            security = results.get('security_score', 0)
            st.metric(
                "🔒 Security",
                f"{security}/100",
                delta="Good" if security >= 70 else "Poor",
                delta_color="normal" if security >= 70 else "inverse"
            )
        
        with col4:
            performance = results.get('performance_score', 0)
            st.metric(
                "⚡ Performance",
                f"{performance}/100",
                delta="Optimized" if performance >= 80 else "Needs work"
            )
        
        with col5:
            maintainability = results.get('maintainability_index', 0)
            st.metric(
                "📈 Maintainability",
                f"{maintainability:.0f}/100"
            )
        
        st.divider()
        
        # Summary
        st.subheader("📋 Summary")
        st.code(results.get('summary', 'No summary available'), language='text')
        
        st.divider()
        
        # Issues and Visualization
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("🔍 Detected Issues")
            
            issues = results.get('issues', [])
            
            if not issues:
                st.success("🎉 No issues detected! Your code looks great!")
            else:
                # Filters
                severity_filter = st.multiselect(
                    "Filter by Severity",
                    ["critical", "error", "warning", "info"],
                    default=["critical", "error", "warning", "info"]
                )
                
                filtered_issues = [
                    i for i in issues
                    if i.get('severity') in severity_filter
                ]
                
                st.write(f"Showing {len(filtered_issues)} of {len(issues)} issues")
                
                # Display issues
                for idx, issue in enumerate(filtered_issues, 1):
                    severity = issue.get('severity', 'info')
                    
                    if severity == 'critical':
                        icon = "🔴"
                        severity_class = "critical-issue"
                    elif severity == 'error':
                        icon = "❌"
                        severity_class = "error-issue"
                    elif severity == 'warning':
                        icon = "⚠️"
                        severity_class = "warning-issue"
                    else:
                        icon = "ℹ️"
                        severity_class = "info-issue"
                    
                    with st.container():
                        st.markdown(f"""
                        <div class="{severity_class}">
                            <h4>{icon} Issue #{idx} - Line {issue.get('line_number', '?')} 
                            <span style="background: #333; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;">
                            {severity.upper()}</span></h4>
                            <strong>Type:</strong> {issue.get('issue_type', 'unknown')}<br>
                            <strong>Description:</strong> {issue.get('description', '')}<br>
                            {f"<strong>CWE:</strong> {issue.get('cwe_id')}<br>" if issue.get('cwe_id') else ""}
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if issue.get('code_snippet'):
                            st.code(issue['code_snippet'], language='python')
                        
                        if issue.get('suggested_fix'):
                            with st.expander("🛠️ View Suggested Fix"):
                                st.code(issue['suggested_fix'], language='python')
                                if issue.get('explanation'):
                                    st.info(f"💡 **Why:** {issue['explanation']}")
        
        with col2:
            st.subheader("📊 Issue Breakdown")
            
            severity_counts = {
                'Critical': results.get('critical', 0),
                'Errors': results.get('errors', 0),
                'Warnings': results.get('warnings', 0),
                'Info': results.get('info', 0)
            }
            
            # Only show chart if there are issues
            if sum(severity_counts.values()) > 0:
                fig = go.Figure(data=[go.Pie(
                    labels=list(severity_counts.keys()),
                    values=list(severity_counts.values()),
                    hole=.3,
                    marker_colors=['#c92a2a', '#f44336', '#ff9800', '#2196f3']
                )])
                fig.update_layout(height=300, margin=dict(l=0, r=0, t=30, b=0))
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.success("✨ No issues to display!")
            
            # Gauges
            st.subheader("🔒 Security Score")
            security_score = results.get('security_score', 0)
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=security_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 40], 'color': "#ffebee"},
                        {'range': [40, 70], 'color': "#fff3e0"},
                        {'range': [70, 100], 'color': "#e8f5e9"}
                    ]
                }
            ))
            fig.update_layout(height=200, margin=dict(l=20, r=20, t=20, b=20))
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("⚡ Performance Score")
            performance_score = results.get('performance_score', 0)
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=performance_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "darkorange"},
                    'steps': [
                        {'range': [0, 40], 'color': "#ffebee"},
                        {'range': [40, 70], 'color': "#fff3e0"},
                        {'range': [70, 100], 'color': "#e8f5e9"}
                    ]
                }
            ))
            fig.update_layout(height=200, margin=dict(l=20, r=20, t=20, b=20))
            st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        
        # Export
        st.subheader("📥 Export Report")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            json_report = json.dumps(results, indent=2)
            st.download_button(
                "📄 Download JSON",
                data=json_report,
                file_name=f"analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col2:
            # Create text report
            text_report = f"""
CODE ANALYSIS REPORT
{'='*50}
File: {st.session_state.get('file_name', 'Unknown')}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

METRICS
{'='*50}
Total Issues: {results.get('total_issues', 0)}
Critical: {results.get('critical', 0)}
Errors: {results.get('errors', 0)}
Warnings: {results.get('warnings', 0)}
Info: {results.get('info', 0)}

Security Score: {results.get('security_score', 0)}/100
Performance Score: {results.get('performance_score', 0)}/100
Maintainability: {results.get('maintainability_index', 0):.1f}/100

SUMMARY
{'='*50}
{results.get('summary', 'N/A')}

ISSUES DETECTED
{'='*50}
"""
            for idx, issue in enumerate(results.get('issues', []), 1):
                text_report += f"\n{idx}. [{issue.get('severity', 'info').upper()}] Line {issue.get('line_number', '?')}\n"
                text_report += f"   Type: {issue.get('issue_type', 'unknown')}\n"
                text_report += f"   Description: {issue.get('description', '')}\n"
                if issue.get('cwe_id'):
                    text_report += f"   CWE: {issue['cwe_id']}\n"
            
            st.download_button(
                "📝 Download TXT",
                data=text_report,
                file_name=f"analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )

# Tab 3: GitHub Integration
with tab3:
    st.header("🔀 GitHub Integration")
    
    if not github_token:
        st.warning("⚠️ GitHub token required for this feature")
        st.markdown("""
        ### How to get GitHub token:
        1. Go to [GitHub Settings → Tokens](https://github.com/settings/tokens)
        2. Click "Generate new token (classic)"
        3. Select scopes: `repo`, `read:org`
        4. Copy token and paste in sidebar
        """)
    else:
        st.success("✅ GitHub configured!")
        
        if 'github_repo_results' in st.session_state:
            results = st.session_state.github_repo_results
            
            st.success(f"✅ Analyzed: {results.get('repo', 'Repository')}")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Files Analyzed", results.get('files_analyzed', 0))
            with col2:
                total_issues = sum(r['analysis']['total_issues'] for r in results.get('results', []))
                st.metric("Total Issues", total_issues)
            with col3:
                total_critical = sum(r['analysis'].get('critical', 0) for r in results.get('results', []))
                st.metric("Critical", total_critical)
            with col4:
                total_errors = sum(r['analysis'].get('errors', 0) for r in results.get('results', []))
                st.metric("Errors", total_errors)
            
            st.divider()
            st.subheader("📁 File-by-File Analysis")
            
            for file_result in results.get('results', []):
                with st.expander(f"📄 {file_result['file']}"):
                    analysis = file_result['analysis']
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Issues", analysis['total_issues'])
                    with col2:
                        st.metric("Critical", analysis.get('critical', 0))
                    with col3:
                        st.metric("Security", f"{analysis.get('security_score', 0)}/100")
                    
                    if analysis.get('issues'):
                        st.markdown("**Top Issues:**")
                        for issue in analysis['issues'][:5]:
                            st.markdown(f"- **Line {issue['line_number']}**: {issue['description']}")
        
        if 'github_pr_results' in st.session_state:
            results = st.session_state.github_pr_results
            
            st.success(f"✅ Analyzed PR: {results.get('pr', 'Pull Request')}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Files Changed", results.get('files_changed', 0))
            with col2:
                total_issues = sum(r['analysis']['total_issues'] for r in results.get('results', []))
                st.metric("Issues Found", total_issues)
            
            st.divider()
            st.subheader("📝 Changed Files Analysis")
            
            for file_result in results.get('results', []):
                with st.expander(f"📄 {file_result['file']} (+{file_result.get('additions', 0)} -{file_result.get('deletions', 0)})"):
                    analysis = file_result['analysis']
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Issues", analysis['total_issues'])
                    with col2:
                        st.metric("Critical", analysis.get('critical', 0))
                    with col3:
                        st.metric("Security", f"{analysis.get('security_score', 0)}/100")
                    
                    if analysis.get('issues'):
                        st.markdown("**Detected Issues:**")
                        for issue in analysis['issues']:
                            st.markdown(f"- **[{issue['severity'].upper()}]** Line {issue['line_number']}: {issue['description']}")

# Tab 4: Documentation
with tab4:
    st.header("📚 Documentation")
    
    st.markdown("""
    ## 🚀 Quick Start Guide
    
    ### Step 1: Configure API Tokens
    1. **HuggingFace Token** (Required for AI features)
       - Visit: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
       - Generate new token (Read access)
       - Paste in sidebar
    
    2. **GitHub Token** (Optional - for GitHub integration)
       - Visit: [github.com/settings/tokens](https://github.com/settings/tokens)
       - Generate token with `repo` scope
       - Paste in sidebar
    
    ### Step 2: Input Your Code
    Choose one of three methods:
    - ✏️ **Paste Code**: Direct input
    - 📁 **Upload File**: Upload .py file
    - 🔀 **GitHub URL**: Analyze from GitHub
    
    ### Step 3: Configure Analysis Options
    Enable/disable checks in the sidebar:
    - ✓ Syntax Analysis
    - 🔒 Security Scan
    - ⚡ Performance Check
    - 👃 Code Smells
    - 📊 Complexity Metrics
    - 💀 Dead Code Detection
    - 🏷️ Type Hints
    
    ### Step 4: Run Analysis
    Click "🔍 Analyze Code" and wait for results!
    
    ---
    
    ## 🔒 Security Features Detected
    
    ### Critical Vulnerabilities
    - **SQL Injection** (CWE-89) - Unsanitized database queries
    - **Command Injection** (CWE-78) - Shell command vulnerabilities
    - **Hardcoded Credentials** (CWE-798) - Passwords/API keys in code
    - **Code Injection** (CWE-95) - eval() and exec() usage
    - **Unsafe Deserialization** (CWE-502) - pickle.loads() on untrusted data
    
    ### Security Warnings
    - **Weak Cryptography** (CWE-327) - MD5/SHA1 usage
    - **Path Traversal** - Unsafe file operations
    - **XSS Vulnerabilities** - Unsanitized user input
    
    ---
    
    ## ⚡ Performance Issues Detected
    
    - **Inefficient List Operations** - Using += in loops
    - **String Concatenation** - Multiple string operations
    - **Global Variables** - Performance impact in loops
    - **Unnecessary Computations** - Repeated calculations
    - **Memory Leaks** - Unclosed resources
    
    ---
    
    ## 📊 Code Metrics Explained
    
    ### Security Score (0-100)
    - **90-100**: 🟢 Excellent - No security issues
    - **70-89**: 🟡 Good - Minor issues
    - **40-69**: 🟠 Fair - Some vulnerabilities
    - **0-39**: 🔴 Poor - Critical vulnerabilities
    
    ### Performance Score (0-100)
    - **90-100**: 🟢 Optimized - Excellent performance
    - **70-89**: 🟡 Good - Minor optimizations needed
    - **40-69**: 🟠 Needs work - Performance issues
    - **0-39**: 🔴 Critical - Major bottlenecks
    
    ### Maintainability Index (0-100)
    - **80-100**: Easy to maintain
    - **60-79**: Moderate complexity
    - **40-59**: Difficult to maintain
    - **0-39**: Legacy code status
    
    ### Cyclomatic Complexity
    - **1-10**: Simple, easy to test
    - **11-20**: Moderate complexity
    - **21-50**: Complex, needs refactoring
    - **50+**: Very complex, high risk
    
    ---
    
    ## 🎯 Best Practices
    
    ### Security
    ```python
    # ❌ BAD - Hardcoded password
    password = "admin123"
    
    # ✅ GOOD - Environment variable
    password = os.getenv("DB_PASSWORD")
    
    # ❌ BAD - SQL Injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    
    # ✅ GOOD - Parameterized query
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    ```
    
    ### Performance
    ```python
    # ❌ BAD - Inefficient list concatenation
    result = []
    for item in items:
        result += [item * 2]
    
    # ✅ GOOD - Use append or list comprehension
    result = [item * 2 for item in items]
    
    # ❌ BAD - Multiple string concatenations
    text = str1 + str2 + str3 + str4
    
    # ✅ GOOD - Use f-strings or join
    text = f"{str1}{str2}{str3}{str4}"
    ```
    
    ### Code Quality
    ```python
    # ❌ BAD - No type hints
    def calculate(x, y):
        return x + y
    
    # ✅ GOOD - With type hints
    def calculate(x: int, y: int) -> int:
        return x + y
    
    # ❌ BAD - Magic numbers
    if age > 18 and score > 750:
        approve()
    
    # ✅ GOOD - Named constants
    MIN_AGE = 18
    MIN_CREDIT_SCORE = 750
    if age > MIN_AGE and score > MIN_CREDIT_SCORE:
        approve()
    ```
    
    ---
    
    ## 🔀 GitHub Integration Features
    
    ### Repository Analysis
    - Scan all Python files in a repository
    - Get comprehensive report for each file
    - Track issues across entire codebase
    - Export results in multiple formats
    
    ### Pull Request Review
    - Analyze only changed files
    - Focus on new code additions
    - Prevent introducing new bugs
    - Automated code review
    
    ### Issue Creation
    - Automatically create GitHub issues for bugs
    - Well-formatted issue descriptions
    - Include fix suggestions
    - Link to specific code lines
    
    ---
    
    ## 💡 Tips for Best Results
    
    1. **Enable All Checks**: For comprehensive analysis, enable all analysis options
    2. **Regular Scanning**: Analyze code before committing
    3. **Fix Critical First**: Address critical and error severity issues first
    4. **Review Suggestions**: Carefully review auto-fix suggestions before applying
    5. **Use Type Hints**: Add type hints for better analysis accuracy
    6. **Keep Code Simple**: Lower complexity scores = easier maintenance
    7. **Test After Fixes**: Always test code after applying fixes
    
    ---
    
    ## 🆘 Common Issues & Solutions
    
    ### "No issues detected but I know there are problems"
    - Enable more analysis options in sidebar
    - Check if code syntax is valid
    - Some patterns may not be detected yet
    
    ### "Analysis is slow"
    - Normal for large files (>1000 lines)
    - GitHub analysis limited to 10 files by default
    - Consider analyzing specific files instead of entire repo
    
    ### "GitHub analysis fails"
    - Verify GitHub token has `repo` scope
    - Check repository URL is correct
    - Ensure repository is accessible with your token
    
    ### "HuggingFace token error"
    - Verify token is valid at huggingface.co/settings/tokens
    - Check token has Read access
    - Some AI features may require token even for basic analysis
    
    ---
    
    ## 📞 Support & Resources
    
    ### Documentation
    - **Full README**: Check GitHub repository
    - **API Docs**: Available for API integration
    - **Examples**: Sample code in `/examples` folder
    
    ### Get Help
    - **GitHub Issues**: Report bugs or request features
    - **Discussions**: Ask questions in GitHub Discussions
    - **Email**: support@fixforge.dev
    
    ### Learn More
    - **OWASP Top 10**: https://owasp.org/www-project-top-ten/
    - **CWE List**: https://cwe.mitre.org/
    - **Python Best Practices**: https://docs.python-guide.org/
    
    ---
    
    ## 🎓 Understanding Results
    
    ### Issue Severity Levels
    
    **🔴 CRITICAL** - Requires immediate attention
    - Security vulnerabilities that could be exploited
    - Potential data breaches
    - Critical bugs that crash the application
    
    **❌ ERROR** - Should be fixed soon
    - Logic errors that affect functionality
    - Performance issues impacting users
    - Code that will fail in certain conditions
    
    **⚠️ WARNING** - Should be addressed
    - Code smells and anti-patterns
    - Potential future problems
    - Style violations that reduce readability
    
    **ℹ️ INFO** - Nice to fix
    - Suggestions for improvement
    - Best practice recommendations
    - Documentation suggestions
    
    ---
    
    ## 🚀 Advanced Features
    
    ### Batch Analysis
    - Upload multiple files at once
    - Compare analysis across versions
    - Track improvements over time
    
    ### Custom Rules (Coming Soon)
    - Define project-specific rules
    - Configure severity levels
    - Whitelist certain patterns
    
    ### CI/CD Integration (Coming Soon)
    - GitHub Actions integration
    - Pre-commit hooks
    - Automated PR comments
    
    ---
    
    ## 📜 Version History
    
    ### Version 2.0 (Current)
    - ✅ Enhanced security scanning
    - ✅ GitHub integration
    - ✅ Performance analysis
    - ✅ Modern UI/UX
    - ✅ Multiple AI models
    
    ### Coming in Version 2.1
    - 🔜 JavaScript/TypeScript support
    - 🔜 Custom rules editor
    - 🔜 Team collaboration features
    - 🔜 CI/CD integration
    
    ---
    
    **Made with ❤️ for developers, by developers**
    
    *FIX FORGE - Your AI-Powered Code Guardian* 🛡️
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: white; padding: 2rem;">
    <p style="font-size: 1.5rem; font-weight: bold;"><strong>🚀 FIX FORGE v2.0</strong></p>
    <p style="font-size: 1.1rem; opacity: 0.9;">100% Free • Open Source • Powered by HuggingFace 🤗</p>
    <p style="font-size: 1rem; margin-top: 1rem;">
        🔒 Security • ⚡ Performance • 🔀 GitHub Integration • 🤖 AI Powered
    </p>
    <p style="font-size: 0.9rem; opacity: 0.8; margin-top: 0.5rem;">
        Built with care for developers everywhere.
    </p>
</div>
""", unsafe_allow_html=True)
