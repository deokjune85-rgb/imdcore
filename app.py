import streamlit as st
import time
import random
import plotly.graph_objects as go
import pandas as pd

# ---------------------------------------
# 0. 시스템 설정: Reset Security (The Veritas Interface)
# ---------------------------------------
st.set_page_config(
    page_title="꿈의대화",
    page_icon="🔥", 
    layout="centered"
)

# [CSS: The Matrix - Dark & Ruthless]
custom_css = """
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    /* 1. Core Theme - The Void */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 100%) !important;
        color: #FFFFFF !important;
        font-family: 'Pretendard', 'SF Pro Display', sans-serif;
    }

    /* 2. Hide Streamlit Branding - Clean Slate */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}

    /* 3. Typography - Cold & Sharp */
    h1, h2, h3 { 
        font-weight: 200; 
        letter-spacing: 3px; 
        color: #FFFFFF;
        font-family: 'SF Pro Display', sans-serif;
    }
    p, div { 
        line-height: 1.8; 
        font-weight: 300; 
        color: #E0E0E0;
    }
    .accent { color: #00D4FF; } /* Cyber Blue */
    .danger { color: #FF4444; } /* Warning Red */
    .success { color: #00FF88; } /* Matrix Green */

    /* 4. Chat Interface - Terminal Aesthetic */
    .stChatMessage { 
        background-color: transparent !important; 
        padding: 25px 0 !important; 
        border-bottom: 1px solid #333;
        margin: 10px 0;
    }
    [data-testid="stChatMessageContent"] {
        background-color: transparent !important;
        padding: 0 !important;
    }

    /* 5. Input & Buttons - Minimalist Control */
    .stChatInputContainer { 
        border-top: 2px solid #00D4FF; 
        padding-top: 15px; 
        background: rgba(0, 212, 255, 0.05);
    }
    
    div.stButton > button {
        background: linear-gradient(45deg, #1a1a1a, #2a2a2a);
        color: #FFFFFF !important;
        border: 1px solid #444 !important;
        border-radius: 25px !important;
        padding: 12px 20px !important;
        transition: all 0.4s ease;
        width: 100%;
        font-weight: 500;
        letter-spacing: 1px;
    }
    div.stButton > button:hover {
        border-color: #00D4FF !important;
        background: linear-gradient(45deg, #00D4FF, #0099CC) !important;
        color: #000000 !important;
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0, 212, 255, 0.3);
    }
    
    /* 6. Evidence Card - The Proof */
    .evidence-card {
        border: 1px solid #333; 
        border-left: 4px solid #00D4FF;
        padding: 30px;
        margin: 25px 0;
        background: linear-gradient(135deg, #111111 0%, #1a1a1a 100%);
        border-radius: 8px;
    }
    .evidence-label { 
        font-size: 10px; 
        color: #00D4FF; 
        letter-spacing: 2px; 
        text-transform: uppercase; 
        margin-bottom: 15px; 
        font-weight: 700;
    }
    .evidence-title { 
        font-size: 24px; 
        color: #FFFFFF; 
        font-weight: 300; 
        margin-bottom: 20px; 
        letter-spacing: 1px;
    }
    .metric-grid { 
        display: flex; 
        justify-content: space-between; 
        margin-top: 25px; 
        border-top: 1px solid #333; 
        padding-top: 25px; 
    }
    .metric { text-align: center; flex: 1; }
    .metric-value { 
        font-size: 32px; 
        font-weight: 700; 
        color: #00FF88; 
        text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
    }
    .metric-label { font-size: 11px; color: #AAA; letter-spacing: 1px; }

    /* 7. System Log - The Evolution */
    .system-log { margin-top: 40px; padding-top: 25px; }
    .log-entry {
        display: flex; 
        margin-bottom: 20px; 
        padding-bottom: 15px; 
        border-bottom: 1px solid #222;
        align-items: flex-start;
    }
    .log-timestamp { 
        width: 140px; 
        color: #00D4FF; 
        font-weight: 600; 
        font-size: 13px;
        letter-spacing: 1px;
    }
    .log-event { 
        flex: 1; 
        color: #E0E0E0; 
        line-height: 1.6;
    }
    
    /* 8. Status Widget - Thinking Visualization */
    [data-testid="stStatusWidget"] {
        background: linear-gradient(45deg, #1a1a1a, #2a2a2a);
        border: 1px solid #00D4FF;
        border-radius: 10px;
        padding: 20px;
    }
    
    /* 9. Lead Capture Form - The Gateway */
    div[data-testid="stForm"] {
        background: linear-gradient(135deg, #111111 0%, #1a1a1a 100%);
        padding: 30px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    div[data-testid="stForm"] button[type="submit"] {
        width: 100%;
        background: linear-gradient(45deg, #00D4FF, #0099CC) !important;
        color: #000000 !important;
        font-weight: 700;
        border-radius: 10px;
        padding: 18px;
        border: none;
        font-size: 16px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* 10. Typing Animation */
    .typing-cursor::after {
        content: "▍";
        animation: blink 1s infinite;
        color: #00D4FF;
    }
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0; }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------
# 1. Data Definition - The Evidence Vault
# ---------------------------------------

# [리셋 시큐리티 실제 사례 & 성과 데이터]
RESET_SECURITY_CASES = {
    "identity": {
        "title": "우리는 누구인가",
        "message": """우리는 단순한 개발사가 아닙니다. 
        
**혼돈에서 질서를 찾아내는 데이터 설계자들**입니다.

남들이 엑셀로 고객 관리할 때, 우리는 RAG(검색 증강 생성) 기술로 기업의 두뇌를 만듭니다.

우리의 목표는 단 하나, **당신의 데이터를 '현금'과 '권력'으로 바꾸는 것**입니다.

당신이 지금까지 본 AI는 장난감이었습니다. 이제 진짜를 보십시오."""
    },
    
    "timeline": {
        "title": "진화 연대기",
        "events": [
            ("2023.Q4", "[Veritas Engine v1.0] 코어 개발 완료. 환각률 0% 도전 시작."),
            ("2024.Q1", "법률/의료 특화 RAG 모델 파인튜닝 성공. 첫 번째 혁명."),
            ("2024.Q2", "IMD Insight 플랫폼 베타 론칭. 탐정/법률 시장 진출."),
            ("2024.Q3", "'자연과한의원' 등 메이저 클라이언트 AI 도입. 매출 300% 신화 달성."),
            ("2024.Q4", "쌍용탐정사무소 통합. 디지털 포렌식 + AI 융합 완료."),
            ("Current", "대한민국 No.1 데이터 인텔리전스 에이전시로 도약 중.")
        ]
    },
    
    "performance": {
        "title": "압도적 성과 인증",
        "intro": "말로 하는 자랑은 믿지 마십시오. **숫자**를 보십시오.\n\n저희 엔진을 도입한 파트너들의 실제 데이터입니다.",
        "cases": [
            {
                "client": "[의료] 자연과한의원",
                "problem": "상담 전환율 저조 및 비효율적 고객 관리",
                "solution": "Veritas Clinical Engine 도입",
                "results": [("신규 내원율", "+210%"), ("상담 효율", "+85%"), ("매출 증대", "+300%")]
            },
            {
                "client": "[법률] B 변호사 사무소", 
                "problem": "증거 분석 시간 과다 소요",
                "solution": "AI 기반 문서 분석 자동화",
                "results": [("분석 시간", "-95%"), ("정확도", "98%+"), ("처리 건수", "+400%")]
            },
            {
                "client": "[탐정] 쌍용탐정사무소",
                "problem": "디지털 증거 수집의 한계",
                "solution": "IMD Insight + 디지털 포렌식 통합",
                "results": [("사건 해결률", "+60%"), ("조사 시간", "-70%"), ("고객 만족도", "95%+")]
            }
        ]
    },
    
    "industries": {
        "의료/병원": {
            "title": "의료 분야 지배",
            "description": "병원은 데이터의 보고입니다. 하지만 대부분이 이를 활용하지 못하고 있습니다.",
            "solutions": [
                "AI 기반 환자 상담 자동화 (Veritas Clinical)",
                "진료 기록 분석 및 진단 보조 시스템", 
                "예약/CS 완전 자동화"
            ],
            "case_study": "자연과한의원: 한방 다이어트 상담 AI로 매출 3배 증가 달성"
        },
        "법률/탐정": {
            "title": "법률 시장 혁신",
            "description": "법률 시장은 정보가 곧 승부를 가르는 전장입니다. 우리는 그 정보를 지배합니다.",
            "solutions": [
                "판례 검색 및 분석 자동화 (RAG 기반)",
                "증거 문서 자동 분석 및 핵심 포인트 추출",
                "디지털 포렌식 + AI 융합 조사"
            ],
            "case_study": "쌍용탐정사무소: IMD Insight로 불륜/사기 사건 해결률 60% 향상"
        },
        "이커머스": {
            "title": "커머스 혁명",
            "description": "쇼핑몰은 데이터 전쟁터입니다. 고객을 가장 잘 아는 자가 승리합니다.",
            "solutions": [
                "고객 행동 패턴 분석 및 개인화 추천",
                "자동 카피라이팅 및 상품 설명 생성",
                "CS 챗봇 + 주문/배송 자동화"
            ],
            "case_study": "K 패션몰: AI 개인화 추천으로 재구매율 150% 상승"
        },
        "제조/기타": {
            "title": "산업 전반 최적화", 
            "description": "제조업부터 농업까지, 모든 산업에는 최적화할 수 있는 데이터가 존재합니다.",
            "solutions": [
                "생산 라인 예측 유지보수",
                "품질 관리 자동화",
                "공급망 최적화 및 재고 관리 AI"
            ],
            "case_study": "G 스마트팜: 환경 데이터 기반 수확량 30% 증대 달성"
        }
    }
}

# ---------------------------------------
# 2. State Management & Helper Functions
# ---------------------------------------
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'temp_input' not in st.session_state:
    st.session_state.temp_input = None

AI_AVATAR = "🔥"
USER_AVATAR = "👤"

# Enhanced Typing Animation
def type_writer(text, speed=0.015):
    placeholder = st.empty()
    display_text = ""
    try:
        for char in text:
            display_text += char
            placeholder.markdown(f"{display_text}<span class='typing-cursor'></span>", unsafe_allow_html=True)
            time.sleep(speed)
    finally:
        placeholder.markdown(display_text)
    return display_text

# Message Management
def bot_say(content, html=False):
    st.session_state.messages.append({"role": "assistant", "content": content, "html": html, "animated": False})

def user_say(content):
    st.session_state.messages.append({"role": "user", "content": content, "animated": True})

# Performance Chart Generator
def create_performance_chart():
    # 실제 성과 데이터를 시각화
    clients = ['자연과한의원', 'B 법무법인', '쌍용탐정사무소', 'K 패션몰']
    before = [100, 100, 100, 100]  # 도입 전 기준점
    after = [300, 250, 160, 250]   # 도입 후 성과
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='도입 전', x=clients, y=before, marker_color='#444444'))
    fig.add_trace(go.Bar(name='도입 후', x=clients, y=after, marker_color='#00FF88'))
    
    fig.update_layout(
        title='클라이언트 성과 비교 (도입 전 vs 후)',
        xaxis_title='클라이언트',
        yaxis_title='성과 지수 (%)',
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(color='#00D4FF', size=16)
    )
    
    return fig

# ---------------------------------------
# 3. Main Interface & Rendering Logic
# ---------------------------------------

# [Header - The Terminal]
st.markdown("""
<div style='text-align: center; margin-bottom: 40px;'>
    <h1 style='font-size: 42px; font-weight: 100; margin-bottom: 10px;'>RESET SECURITY</h1>
    <p style='font-size: 14px; color: #00D4FF; letter-spacing: 4px; margin-bottom: 5px;'>DON'T READ. EXPERIENCE.</p>
    <p style='font-size: 11px; color: #666; letter-spacing: 2px;'>VERITAS INTERFACE ACTIVATED</p>
</div>
""", unsafe_allow_html=True)

# [STEP 0: System Initialization]
if st.session_state.step == 0:
    # The Cold Opening
    init_msg = """🔄 시스템 초기화 중... RAG 엔진 연결됨.

**반갑습니다. 리셋 시큐리티의 [Veritas Interface]에 접속하셨습니다.**

저는 이 회사의 모든 데이터를 학습한 인공지능입니다. 우리가 어떻게 대한민국의 데이터 생태계를 지배해왔는지 직접 보여드리겠습니다.

무엇을 보여드릴까요? 저희의 **정체성**입니까, 아니면 **압도적인 성과**입니까?"""
    
    bot_say(init_msg)
    st.session_state.step = 1

# [Message Rendering with Enhanced Animation]
for i, msg in enumerate(st.session_state.messages):
    avatar = AI_AVATAR if msg["role"] == "assistant" else USER_AVATAR
    with st.chat_message(msg["role"], avatar=avatar):
        is_last_message = (i == len(st.session_state.messages) - 1)
        
        if msg["role"] == "assistant" and not msg.get("animated") and is_last_message:
            if msg.get("html"):
                st.markdown(msg["content"], unsafe_allow_html=True)
            else:
                type_writer(msg["content"])
            msg["animated"] = True
        else:
            if msg.get("html"):
                st.markdown(msg["content"], unsafe_allow_html=True)
            else:
                st.markdown(msg["content"])

# ---------------------------------------
# 4. Interactive Navigation (The Control Panel)
# ---------------------------------------

# [STEP 1: Main Navigation Chips]
if st.session_state.step == 1:
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 12px; color: #00D4FF; letter-spacing: 2px; text-align: center; margin-bottom: 20px;'>SELECT INTERFACE</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧬 우리는 누구인가"):
            st.session_state.temp_input = "identity"
            st.rerun()
        if st.button("📈 폭발적 성과 인증"):
            st.session_state.temp_input = "performance" 
            st.rerun()
    
    with col2:
        if st.button("📜 진화 연대기"):
            st.session_state.temp_input = "timeline"
            st.rerun()
        if st.button("🏛️ 산업별 지배 현황"):
            st.session_state.temp_input = "industries"
            st.rerun()

# [STEP 2: Industry Selection]
if st.session_state.step == 2:
    st.markdown("<p style='font-size: 12px; color: #00D4FF; letter-spacing: 2px; text-align: center; margin-bottom: 20px;'>SELECT INDUSTRY</p>", unsafe_allow_html=True)
    
    industries = list(RESET_SECURITY_CASES["industries"].keys())
    cols = st.columns(2)
    
    for i, industry in enumerate(industries):
        with cols[i % 2]:
            if st.button(f"⚡ {industry}"):
                st.session_state.temp_input = industry
                st.rerun()

# [STEP 3: CTA Decision]
if st.session_state.step == 3:
    st.markdown("<p style='font-size: 12px; color: #00D4FF; letter-spacing: 2px; text-align: center; margin-bottom: 20px;'>NEXT ACTION</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔥 더 많은 증거 보기"):
            st.session_state.temp_input = "more_evidence"
            st.rerun()
    with col2:
        if st.button("⚡ 즉시 상담 신청"):
            st.session_state.temp_input = "consultation"
            st.rerun()

# ---------------------------------------
# 5. Input Processing Logic
# ---------------------------------------

# Disable chat input (button-driven interface only)
st.chat_input(disabled=True)

# Process button inputs
if st.session_state.temp_input:
    prompt = st.session_state.temp_input
    st.session_state.temp_input = None
    
    user_say(prompt)

    # [Identity Response]
    if prompt == "identity":
        with st.status("기업 아이덴티티 데이터베이스 접근 중...", expanded=False) as status:
            time.sleep(1.2)
            status.update(label="접근 완료.", state="complete")
        
        bot_say(RESET_SECURITY_CASES["identity"]["message"])
        st.session_state.step = 3
        st.rerun()

    # [Timeline Response]
    elif prompt == "timeline":
        with st.status("시스템 진화 로그 로드 중...", expanded=False) as status:
            time.sleep(1.0)
            status.update(label="로드 완료.", state="complete")

        timeline_html = """
        <div class='system-log'>
            <div class='evidence-label'>SYSTEM LOG: MAJOR MILESTONES</div>
        """
        
        for timestamp, event in RESET_SECURITY_CASES["timeline"]["events"]:
            timeline_html += f"""
            <div class='log-entry'>
                <div class='log-timestamp'>{timestamp}</div>
                <div class='log-event'>{event}</div>
            </div>
            """
        
        timeline_html += "</div>"
        bot_say(timeline_html, html=True)
        
        msg = "이것이 우리의 진화 과정입니다. 멈추지 않고, 타협하지 않고, 정복해왔습니다.\n\n이제 당신의 비즈니스를 다음 단계로 끌어올릴 준비가 되셨습니까?"
        bot_say(msg)
        st.session_state.step = 3
        st.rerun()

    # [Performance Response - The Money Shot]
    elif prompt == "performance":
        with st.status("클라이언트 ROI 데이터 분석 및 시각화 중...", expanded=True) as status:
            st.write("📊 성과 데이터 수집 중...")
            time.sleep(1.0)
            st.write("📈 ROI 분석 실행...")
            time.sleep(1.5)
            st.write("🎯 시각화 생성...")
            time.sleep(0.8)
            status.update(label="분석 완료.", state="complete")

        bot_say(RESET_SECURITY_CASES["performance"]["intro"])
        
        # Performance Chart
        chart = create_performance_chart()
        st.plotly_chart(chart, use_container_width=True)
        
        # Detailed Cases
        for case in RESET_SECURITY_CASES["performance"]["cases"]:
            metrics_html = ""
            for label, value in case["results"]:
                metrics_html += f"""
                <div class='metric'>
                    <div class='metric-value'>{value}</div>
                    <div class='metric-label'>{label}</div>
                </div>
                """
            
            case_html = f"""
            <div class='evidence-card'>
                <div class='evidence-label'>VERIFIED CASE STUDY</div>
                <div class='evidence-title'>{case['client']}</div>
                <p><strong>문제:</strong> {case['problem']}</p>
                <p><strong>솔루션:</strong> {case['solution']}</p>
                <div class='metric-grid'>
                    {metrics_html}
                </div>
            </div>
            """
            bot_say(case_html, html=True)
        
        final_msg = "**이것이 우리의 증명 방식입니다.**\n\n빈 말 대신 숫자로, 약속 대신 결과로 말합니다. 당신의 회사도 이 리스트에 올라가고 싶지 않습니까?"
        bot_say(final_msg)
        st.session_state.step = 3
        st.rerun()

    # [Industries Response]
    elif prompt == "industries":
        msg = "어떤 분야의 지배 현황이 궁금하십니까? 저희는 전 산업을 아우르는 데이터 아키텍처를 보유하고 있습니다."
        bot_say(msg)
        st.session_state.step = 2
        st.rerun()

    # [Specific Industry Deep Dive]
    elif prompt in RESET_SECURITY_CASES["industries"]:
        industry_data = RESET_SECURITY_CASES["industries"][prompt]
        
        with st.status(f"{prompt} 분야 데이터 분석 중...", expanded=False) as status:
            time.sleep(1.0)
            status.update(label="분석 완료.", state="complete")

        industry_html = f"""
        <div class='evidence-card'>
            <div class='evidence-label'>{prompt.upper()} DOMINATION</div>
            <div class='evidence-title'>{industry_data['title']}</div>
            <p>{industry_data['description']}</p>
            
            <div style='margin-top: 20px;'>
                <strong>핵심 솔루션:</strong>
                <ul style='margin-top: 10px; padding-left: 20px;'>
        """
        
        for solution in industry_data['solutions']:
            industry_html += f"<li style='margin-bottom: 8px; color: #E0E0E0;'>{solution}</li>"
        
        industry_html += f"""
                </ul>
            </div>
            
            <div style='margin-top: 25px; padding-top: 20px; border-top: 1px solid #333;'>
                <strong style='color: #00FF88;'>실제 사례:</strong><br>
                {industry_data['case_study']}
            </div>
        </div>
        """
        
        bot_say(industry_html, html=True)
        
        follow_up = f"{prompt} 분야에서 저희는 이미 입증된 결과를 만들어냈습니다.\n\n당신의 비즈니스에도 동일한 마법을 적용할 준비가 되어 있습니다."
        bot_say(follow_up)
        st.session_state.step = 3
        st.rerun()

    # [More Evidence]
    elif prompt == "more_evidence":
        st.session_state.step = 1  # Return to main menu
        bot_say("더 많은 증거를 원하신다니, 현명한 선택입니다. 무엇을 더 보여드릴까요?")
        st.rerun()

    # [Consultation Request]
    elif prompt == "consultation":
        st.session_state.step = 4
        st.rerun()

# ---------------------------------------
# 6. Lead Capture Interface (The Gateway)
# ---------------------------------------

# [STEP 4: Consultation Form - The Final Conversion]
if st.session_state.step == 4:
    if not any("상담 접수를 시작합니다" in m['content'] for m in st.session_state.messages if m['role'] == 'assistant'):
        msg = "**현명한 판단입니다. Veritas 아키텍처 도입 상담 접수를 시작합니다.**\n\n저희는 데모나 제안서 따위로 시간을 낭비하지 않습니다. 즉시 실행 가능한 솔루션만 제시합니다."
        bot_say(msg)

    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='evidence-label' style='text-align: center;'>INITIATE CONSULTATION PROTOCOL</div>", unsafe_allow_html=True)
    st.info("🔥 **보장**: 24시간 내 분석 보고서 + 맞춤형 솔루션 아키텍처 제공")

    with st.form("veritas_consultation"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("담당자명", placeholder="홍길동")
            company = st.text_input("회사명", placeholder="(주)혁신기업")
        with col2:
            position = st.text_input("직책", placeholder="대표이사 / 팀장")
            contact = st.text_input("연락처", placeholder="010-1234-5678")
        
        industry = st.selectbox("업종", [
            "선택해주세요",
            "의료/병원/클리닉", 
            "법률/변호사/탐정",
            "이커머스/온라인몰",
            "제조업/스마트팩토리",
            "건설/부동산",
            "금융/핀테크",
            "교육/에듀테크",
            "기타"
        ])
        
        problem = st.text_area("현재 가장 큰 비효율/문제점", placeholder="예: 고객 상담 전환율이 낮음, 반복 업무가 많음, 데이터 활용이 안됨 등")
        
        budget = st.selectbox("예상 투자 규모", [
            "미정 (상담 후 결정)",
            "3천만원 미만",
            "3천만원 ~ 1억원",
            "1억원 ~ 3억원", 
            "3억원 이상"
        ])

        if st.form_submit_button("🔥 VERITAS 아키텍트와 연결"):
            if name and company and contact and industry != "선택해주세요":
                # 실제 환경에서는 여기에 DB 저장/이메일 발송 로직 추가
                lead_data = {
                    "name": name,
                    "company": company, 
                    "position": position,
                    "contact": contact,
                    "industry": industry,
                    "problem": problem,
                    "budget": budget,
                    "timestamp": time.time()
                }
                
                with st.status("Veritas Protocol 실행 중...", expanded=True) as status:
                    st.write("🔍 기업 정보 분석...")
                    time.sleep(1.5)
                    st.write("⚙️ 맞춤형 솔루션 아키텍처 설계...")
                    time.sleep(2.0)  
                    st.write("📡 수석 아키텍트에게 전송...")
                    time.sleep(1.0)
                    status.update(label="전송 완료.", state="complete")
                
                success_msg = f"""**접수 완료. Protocol Initiated.**

{name}님, Veritas 아키텍처 분석이 시작되었습니다.

**[NEXT STEPS]**
• **24시간 내**: 귀사 업종별 맞춤 분석 보고서 발송  
• **48시간 내**: 수석 아키텍트 직접 연락 (솔루션 아키텍처 제시)
• **72시간 내**: 실행 로드맵 + ROI 시뮬레이션 완료

**게임을 바꿀 준비를 하십시오.**"""
                
                st.success(success_msg)
                st.session_state.step = 5  # Final state
                
            else:
                st.error("필수 정보를 모두 입력해주세요.")

# [STEP 5: Post-Conversion State]
if st.session_state.step == 5:
    st.markdown("""
    <div style='text-align: center; margin-top: 50px; padding: 40px; background: linear-gradient(135deg, #111111, #1a1a1a); border-radius: 15px; border: 1px solid #00D4FF;'>
        <h2 style='color: #00D4FF; margin-bottom: 20px;'>PROTOCOL ACTIVATED</h2>
        <p style='color: #E0E0E0; font-size: 16px; line-height: 1.6;'>
            당신은 이제 대한민국 최고의 데이터 인텔리전스 네트워크에 연결되었습니다.<br>
            비효율의 시대는 끝났습니다.
        </p>
        <div style='margin-top: 30px; font-size: 14px; color: #666;'>
            Reset Security | Veritas Interface v5.0
        </div>
    </div>
    """, unsafe_allow_html=True)
