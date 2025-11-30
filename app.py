import streamlit as st
import time
import plotly.graph_objects as go

# ---------------------------------------
# 0. 시스템 설정: Reset Security (안정화 버전)
# ---------------------------------------
st.set_page_config(
    page_title="Reset Security | Don't Read. Experience.",
    page_icon="🔥", 
    layout="centered"
)

# [CSS: 안정화된 스타일]
custom_css = """
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 100%) !important;
        color: #FFFFFF !important;
        font-family: 'Pretendard', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}

    h1, h2, h3 { 
        font-weight: 200; 
        letter-spacing: 3px; 
        color: #FFFFFF;
    }
    p, div { 
        line-height: 1.8; 
        font-weight: 300; 
        color: #E0E0E0;
    }

    .stChatMessage { 
        background-color: transparent !important; 
        padding: 20px 0 !important; 
        border-bottom: 1px solid #333;
    }
    [data-testid="stChatMessageContent"] {
        background-color: transparent !important;
        padding: 0 !important;
    }

    div.stButton > button {
        background: linear-gradient(45deg, #1a1a1a, #2a2a2a);
        color: #FFFFFF !important;
        border: 1px solid #444 !important;
        border-radius: 25px !important;
        padding: 12px 20px !important;
        transition: all 0.3s ease;
        width: 100%;
        font-weight: 500;
    }
    div.stButton > button:hover {
        border-color: #00D4FF !important;
        background: linear-gradient(45deg, #00D4FF, #0099CC) !important;
        color: #000000 !important;
        transform: translateY(-2px);
    }
    
    .evidence-card {
        border: 1px solid #333; 
        border-left: 4px solid #00D4FF;
        padding: 25px;
        margin: 20px 0;
        background: linear-gradient(135deg, #111111 0%, #1a1a1a 100%);
        border-radius: 8px;
    }
    
    .metric-grid { 
        display: flex; 
        justify-content: space-between; 
        margin-top: 20px; 
        border-top: 1px solid #333; 
        padding-top: 20px; 
    }
    .metric { text-align: center; flex: 1; }
    .metric-value { 
        font-size: 28px; 
        font-weight: 700; 
        color: #00FF88; 
    }
    .metric-label { font-size: 11px; color: #AAA; }

    div[data-testid="stForm"] {
        background: linear-gradient(135deg, #111111 0%, #1a1a1a 100%);
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    div[data-testid="stForm"] button[type="submit"] {
        width: 100%;
        background: linear-gradient(45deg, #00D4FF, #0099CC) !important;
        color: #000000 !important;
        font-weight: 700;
        border-radius: 8px;
        padding: 15px;
        border: none;
        font-size: 16px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------
# 1. 상태 초기화 (간소화)
# ---------------------------------------
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'main'
if 'selected_industry' not in st.session_state:
    st.session_state.selected_industry = None

# ---------------------------------------
# 2. 데이터 정의
# ---------------------------------------
COMPANY_DATA = {
    "performance_cases": [
        {
            "client": "[의료] 자연과한의원",
            "results": [("신규 내원율", "+210%"), ("상담 효율", "+85%"), ("매출", "+300%")]
        },
        {
            "client": "[법률] 쌍용탐정사무소", 
            "results": [("사건 해결률", "+60%"), ("조사 시간", "-70%"), ("만족도", "95%+")]
        },
        {
            "client": "[커머스] K 패션몰",
            "results": [("재구매율", "+150%"), ("이탈률", "-45%"), ("ROI", "+200%")]
        }
    ],
    
    "timeline": [
        ("2023.Q4", "[Veritas Engine v1.0] 코어 개발 완료"),
        ("2024.Q1", "법률/의료 특화 RAG 모델 파인튜닝 성공"),
        ("2024.Q2", "IMD Insight 플랫폼 베타 론칭"),
        ("2024.Q3", "메이저 클라이언트 AI 도입, 매출 300% 달성"),
        ("2024.Q4", "쌍용탐정사무소 통합, 디지털 포렌식 완료"),
        ("Current", "대한민국 No.1 데이터 인텔리전스 에이전시")
    ],
    
    "industries": {
        "의료/병원": {
            "solutions": [
                "AI 기반 환자 상담 자동화 (Veritas Clinical)",
                "진료 기록 분석 및 진단 보조", 
                "예약/CS 완전 자동화"
            ],
            "case": "자연과한의원: 한방 다이어트 상담 AI로 매출 3배 증가"
        },
        "법률/탐정": {
            "solutions": [
                "판례 검색 및 분석 자동화 (RAG)",
                "증거 문서 자동 분석", 
                "디지털 포렌식 + AI 융합"
            ],
            "case": "쌍용탐정사무소: IMD Insight로 사건 해결률 60% 향상"
        },
        "이커머스": {
            "solutions": [
                "고객 행동 패턴 분석 및 개인화",
                "자동 카피라이팅 시스템",
                "CS 챗봇 + 주문 자동화"
            ],
            "case": "K 패션몰: AI 개인화 추천으로 재구매율 150% 상승"
        }
    }
}

# ---------------------------------------
# 3. 메인 헤더
# ---------------------------------------
st.markdown("""
<div style='text-align: center; margin-bottom: 40px;'>
    <h1 style='font-size: 42px; font-weight: 100; margin-bottom: 10px;'>RESET SECURITY</h1>
    <p style='font-size: 14px; color: #00D4FF; letter-spacing: 4px;'>DON'T READ. EXPERIENCE.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------
# 4. 메인 뷰 분기 (rerun 대신 조건부 렌더링)
# ---------------------------------------

# 메인 네비게이션
if st.session_state.current_view == 'main':
    st.markdown("### 🔄 Veritas Interface 활성화")
    
    st.markdown("""
    **반갑습니다. 리셋 시큐리티의 Veritas Interface에 접속하셨습니다.**
    
    저는 이 회사의 모든 데이터를 학습한 인공지능입니다. 
    우리가 어떻게 대한민국의 데이터 생태계를 지배해왔는지 보여드리겠습니다.
    """)
    
    st.markdown("---")
    st.markdown("**무엇을 보여드릴까요?**")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧬 우리는 누구인가"):
            st.session_state.current_view = 'identity'
            st.rerun()
        if st.button("📈 압도적 성과 인증"):
            st.session_state.current_view = 'performance'
            st.rerun()
    with col2:
        if st.button("📜 진화 연대기"):
            st.session_state.current_view = 'timeline'
            st.rerun()
        if st.button("🏛️ 산업별 지배현황"):
            st.session_state.current_view = 'industries'
            st.rerun()

# 정체성 뷰
elif st.session_state.current_view == 'identity':
    st.markdown("### 🧬 우리는 누구인가")
    
    st.markdown("""
    우리는 단순한 개발사가 아닙니다.
    
    **혼돈에서 질서를 찾아내는 데이터 설계자들**입니다.
    
    남들이 엑셀로 고객 관리할 때, 우리는 RAG(검색 증강 생성) 기술로 기업의 두뇌를 만듭니다.
    
    우리의 목표는 단 하나, **당신의 데이터를 '현금'과 '권력'으로 바꾸는 것**입니다.
    
    당신이 지금까지 본 AI는 장난감이었습니다. 이제 진짜를 보십시오.
    """)
    
    if st.button("⚡ 상담 신청"):
        st.session_state.current_view = 'consultation'
        st.rerun()
    if st.button("⬅️ 메인으로"):
        st.session_state.current_view = 'main'
        st.rerun()

# 성과 뷰
elif st.session_state.current_view == 'performance':
    st.markdown("### 📈 압도적 성과 인증")
    
    st.markdown("**말로 하는 자랑은 믿지 마십시오. 숫자를 보십시오.**")
    
    # 성과 차트
    clients = ['자연과한의원', '쌍용탐정사무소', 'K 패션몰']
    before = [100, 100, 100]
    after = [300, 160, 250]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='도입 전', x=clients, y=before, marker_color='#444444'))
    fig.add_trace(go.Bar(name='도입 후', x=clients, y=after, marker_color='#00FF88'))
    
    fig.update_layout(
        title='클라이언트 성과 비교',
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 상세 케이스
    for case in COMPANY_DATA["performance_cases"]:
        st.markdown(f"""
        <div class='evidence-card'>
            <h4 style='color: #00D4FF; margin-bottom: 15px;'>{case['client']}</h4>
            <div class='metric-grid'>
        """, unsafe_allow_html=True)
        
        cols = st.columns(len(case["results"]))
        for i, (label, value) in enumerate(case["results"]):
            with cols[i]:
                st.metric(label, value)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
    
    if st.button("⚡ 이 성과를 내 회사에도"):
        st.session_state.current_view = 'consultation'
        st.rerun()
    if st.button("⬅️ 메인으로"):
        st.session_state.current_view = 'main'
        st.rerun()

# 연대기 뷰
elif st.session_state.current_view == 'timeline':
    st.markdown("### 📜 진화 연대기")
    
    for timestamp, event in COMPANY_DATA["timeline"]:
        st.markdown(f"""
        <div style='display: flex; margin-bottom: 15px; padding: 15px; background: #111; border-left: 3px solid #00D4FF;'>
            <div style='width: 120px; color: #00D4FF; font-weight: bold;'>{timestamp}</div>
            <div style='flex: 1; color: #FFF;'>{event}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("**이것이 우리의 진화 과정입니다. 멈추지 않고, 타협하지 않고, 정복해왔습니다.**")
    
    if st.button("⚡ 다음 진화에 참여"):
        st.session_state.current_view = 'consultation'
        st.rerun()
    if st.button("⬅️ 메인으로"):
        st.session_state.current_view = 'main'
        st.rerun()

# 산업별 뷰
elif st.session_state.current_view == 'industries':
    st.markdown("### 🏛️ 산업별 지배 현황")
    
    industry = st.selectbox(
        "어떤 분야의 지배 현황이 궁금하십니까?",
        ["선택하세요"] + list(COMPANY_DATA["industries"].keys())
    )
    
    if industry != "선택하세요":
        data = COMPANY_DATA["industries"][industry]
        
        st.markdown(f"#### {industry} 분야")
        
        st.markdown("**핵심 솔루션:**")
        for solution in data["solutions"]:
            st.markdown(f"• {solution}")
        
        st.info(f"**실제 사례:** {data['case']}")
    
    if st.button("⚡ 내 산업에 적용"):
        st.session_state.current_view = 'consultation'
        st.rerun()
    if st.button("⬅️ 메인으로"):
        st.session_state.current_view = 'main'
        st.rerun()

# 상담 뷰
elif st.session_state.current_view == 'consultation':
    st.markdown("### ⚡ Veritas 아키텍처 도입 상담")
    
    st.markdown("""
    **현명한 판단입니다.**
    
    저희는 데모나 제안서로 시간을 낭비하지 않습니다. 
    즉시 실행 가능한 솔루션만 제시합니다.
    """)
    
    st.info("🔥 **보장**: 24시간 내 분석 보고서 + 맞춤형 솔루션 아키텍처 제공")

    with st.form("consultation_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("담당자명", placeholder="홍길동")
            company = st.text_input("회사명", placeholder="(주)혁신기업")
        with col2:
            contact = st.text_input("연락처", placeholder="010-1234-5678")
            position = st.text_input("직책", placeholder="대표이사/팀장")
        
        industry = st.selectbox("업종", [
            "선택해주세요",
            "의료/병원/클리닉", 
            "법률/변호사/탐정",
            "이커머스/온라인몰",
            "제조업/스마트팩토리",
            "기타"
        ])
        
        problem = st.text_area("가장 큰 비효율/문제점", 
                              placeholder="예: 상담 전환율 저조, 반복 업무 과다, 데이터 활용 부족 등")
        
        budget = st.selectbox("예상 투자 규모", [
            "미정 (상담 후 결정)",
            "3천만원 미만", 
            "3천만원 ~ 1억원",
            "1억원 이상"
        ])

        if st.form_submit_button("🔥 VERITAS 아키텍트와 연결"):
            if name and company and contact and industry != "선택해주세요":
                with st.spinner("Veritas Protocol 실행 중..."):
                    time.sleep(2)
                
                st.success(f"""
                **접수 완료. Protocol Initiated.**

                {name}님, Veritas 아키텍처 분석이 시작되었습니다.

                **[NEXT STEPS]**
                • 24시간 내: 맞춤 분석 보고서 발송  
                • 48시간 내: 수석 아키텍트 직접 연락
                • 72시간 내: 실행 로드맵 + ROI 시뮬레이션

                **게임을 바꿀 준비를 하십시오.**
                """)
                
                # 여기에 실제 DB 저장/이메일 발송 로직 추가
                
            else:
                st.error("필수 정보를 모두 입력해주세요.")
    
    if st.button("⬅️ 메인으로"):
        st.session_state.current_view = 'main'
        st.rerun()
