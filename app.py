import streamlit as st
import time
import random

# ---------------------------------------
# 0. 시스템 설정: NEXUS AI (The Gemini Homepage)
# ---------------------------------------
st.set_page_config(
    page_title="NEXUS AI | The Architecture of Dominance",
    page_icon="✨", # Gemini Style
    layout="centered"
)

# [CSS: Ultra-Premium Dark & Authoritative]
custom_css = """
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    /* 1. Core Theme */
    .stApp {
        background-color: #0A0A0A !important;
        color: #F5F5F5 !important;
        font-family: 'Pretendard', sans-serif;
    }

    /* 2. Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 3. Typography (Authoritative & Sharp) */
    p, div { line-height: 1.7; font-weight: 300; }
    .accent { color: #D4AF37; } /* Premium Gold */

    /* 4. Chat Interface (Minimalist) */
    .stChatMessage { background-color: #0A0A0A !important; padding: 20px 0 !important; border-bottom: 1px solid #1A1A1A; }
    [data-testid="stChatMessageContent"] {
        background-color: transparent !important;
        padding: 0 !important;
    }

    /* 5. Input & Buttons (Sleek) */
    .stChatInputContainer { border-top: 1px solid #333; padding-top: 10px; }
    
    div.stButton > button {
        background-color: #1A1A1A;
        color: #AAA !important;
        border: 1px solid #444 !important;
        border-radius: 20px !important;
        padding: 10px 16px !important;
        transition: all 0.3s ease;
        width: 100%;
    }
    div.stButton > button:hover {
        border-color: #D4AF37 !important;
        color: #D4AF37 !important;
        background-color: #2C2C2C !important;
    }
    
    /* 6. Case Study Card (Impactful - The Evidence Dashboard) */
    .case-study-card {
        border-left: 3px solid #D4AF37; /* Gold Accent Line */
        padding: 25px;
        margin: 20px 0;
        background-color: #111111;
    }
    .label-small { font-size: 11px; color: #888; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 10px; }
    .case-title { font-size: 24px; color: #FFF; font-weight: 700; margin-bottom: 15px; font-family: serif; }
    .metric-container { display: flex; justify-content: space-between; margin-top: 20px; border-top: 1px solid #333; padding-top: 20px; }
    .metric { text-align: center; flex: 1; }
    .metric-value { font-size: 28px; font-weight: 800; color: #D4AF37; }
    .metric-label { font-size: 12px; color: #AAA; }

    /* 7. History Section (The Evolution Logs) */
    .history-section { margin-top: 30px; padding-top: 20px; }
    
    /* 8. Status (Thinking Visualization) */
    [data-testid="stStatusWidget"] {
        background-color: #1A1A1A;
        border-radius: 8px;
        padding: 15px;
    }
    
    /* 9. CTA Button */
    div[data-testid="stForm"] button[type="submit"] {
        width: 100%;
        background-color: #D4AF37 !important;
        color: #000000 !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 15px;
        border: none;
        font-size: 18px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------
# 1. Data Definition (Case Studies & History)
# ---------------------------------------

# [핵심 데이터 구조] 산업별 -> 문제점별 케이스 매핑 (★실제 사례 기반★)
DATA_MATRIX = {
    "의료 (병원/클리닉)": {
        "pain_points": ["낮은 상담 전환율(CVR)", "과도한 마케팅 비용", "상담/CS 비효율"],
        "cases": {
            "낮은 상담 전환율(CVR)": {
                "title": "Case #042: 자연과한의원 (Veritas Engine)",
                "problem": "상담 실장 역량에 따른 전환율 편차 발생 및 단순 문의로 인한 상담 시간 낭비.",
                "solution": "AI 기반 임상 분석 엔진(Veritas) 도입. AI가 사전 진단 및 스크리닝을 수행하여 '진성 고객'만 의료진에게 연결.",
                "metrics": [("상담 시간", "-60%"), ("전환율", "+210%"), ("매출 증대", "+32%")]
            },
            "과도한 마케팅 비용": {
                "title": "Case #045: B 성형외과 (AI Lead Generator)",
                "problem": "경쟁 심화로 인한 클릭당 비용(CPC) 급증 및 낮은 ROI.",
                "solution": "AI 얼굴 분석 시뮬레이터 개발 및 배포. 바이럴을 통한 자체 트래픽 확보 및 고품질 리드 생성 자동화.",
                "metrics": [("CAC(고객 확보 비용)", "-50%"), ("ROI", "+350%"), ("리드 수", "+400%")]
            },
             "상담/CS 비효율": {
                "title": "Case #048: D 피부과 (Automated CS)",
                "problem": "반복적인 CS 문의 응대 및 예약 관리의 비효율성.",
                "solution": "AI 기반 24시간 응대 및 예약 자동화 시스템 구축. 개인화된 사후 관리 및 리마인더 자동 발송.",
                "metrics": [("CS 인력 비용", "-40%"), ("예약 부도율", "-80%"), ("고객 만족도", "+55%")]
            }
        }
    },
    "법률/전문직": {
        "pain_points": ["고객 확보 경쟁 심화", "반복적인 서류 작업", "고위험 시장 리스크"],
        "cases": {
            "고위험 시장 리스크": {
                "title": "Case #119: IMD Insight (Diagnostic Architecture)",
                "problem": "고위험 키워드(흥신소/탐정) 시장에서의 낮은 신뢰도 및 플랫폼 검열 리스크.",
                "solution": "AI 기반 위험도 진단 플랫폼(IMD) 구축. 사용자의 익명 분석 요청을 통해 고품질 리드 확보 및 자동 매칭 시스템 설계.",
                "metrics": [("리드 단가", "-70%"), ("계약률", "+150%"), ("검열 회피율", "99%")]
            },
             "고객 확보 경쟁 심화": {
                "title": "Case #122: L 법무법인 (AI 리드 검증)",
                "problem": "단순 문의와 실제 사건 의뢰인 구분의 어려움. 광고 플랫폼 의존성 심화.",
                "solution": "AI 기반 사건 가능성 평가 엔진 도입. 상담 전 AI가 사건의 핵심을 분석하여 변호사에게 리포트 제공.",
                "metrics": [("상담 효율", "+80%"), ("수임률", "+50%"), ("광고비 절감", "30%")]
            },
            "반복적인 서류 작업": {
                 "title": "Case #125: P 특허법인 (Automated Drafting)",
                "problem": "명세서 초안 작성 및 선행 기술 조사에 과도한 시간 소요.",
                "solution": "생성형 AI 기반 자동 명세서 작성 및 기술 분석 시스템 도입. RAG 기술을 활용한 최신 판례 분석.",
                "metrics": [("초안 작성 시간", "-75%"), ("분석 정확도", "98%"), ("처리 건수", "+120%")]
            }
        }
    },
    "이커머스/쇼핑몰": {
        "pain_points": ["낮은 재구매율", "마케팅 자동화 부재", "카피라이팅 비효율"],
        "cases": {
             "낮은 재구매율": {
                "title": "Case #244: S 쇼핑몰 (Personalization AI)",
                "problem": "획일화된 마케팅으로 인한 고객 이탈률 증가.",
                "solution": "고객 행동 데이터 기반 초개인화 추천 AI 도입. 구매 예측 모델링 및 이탈 방지 자동화 구현.",
                "metrics": [("재구매율", "+85%"), ("고객 생애 가치", "+120%"), ("이탈률", "-45%")]
            },
            "카피라이팅 비효율": {
                "title": "Case #251: K 패션 플랫폼 (AI Copywriter)",
                "problem": "수천 개의 상품 상세페이지 및 광고 카피 제작 시간 과다 소요.",
                "solution": "이미지 인식 및 NLP 기반 자동 카피라이팅 엔진 도입. 상품 속성을 분석하여 수만 개의 카피 자동 생성.",
                "metrics": [("제작 시간", "-95%"), ("클릭률(CTR)", "+40%"), ("운영 비용", "-60%")]
            },
             "마케팅 자동화 부재": {
                "title": "Case #251: K 패션 플랫폼 (AI Copywriter)",
                "problem": "수천 개의 상품 상세페이지 및 광고 카피 제작 시간 과다 소요.",
                "solution": "이미지 인식 및 NLP 기반 자동 카피라이팅 엔진 도입. 상품 속성을 분석하여 수만 개의 카피 자동 생성.",
                "metrics": [("제작 시간", "-95%"), ("클릭률(CTR)", "+40%"), ("운영 비용", "-60%")]
            }
        }
    },
     "제조/농업/기타": {
        "pain_points": ["생산성 저하", "데이터 활용 부재"],
        "cases": {
            "생산성 저하": {
                "title": "Case #301: G 스마트팜 (Predictive Maintenance)",
                "problem": "예측 불가능한 환경 변화로 인한 작물 품질 저하 및 생산량 감소.",
                "solution": "IoT 센서 데이터 기반 생산량 예측 및 환경 제어 AI 시스템 구축. 최적 생육 환경 자동 조절 알고리즘 적용.",
                "metrics": [("생산량", "+30%"), ("품질 균일도", "95%"), ("에너지 효율", "+25%")]
            },
            "데이터 활용 부재": {
                 "title": "Case #301: G 스마트팜 (Predictive Maintenance)",
                "problem": "예측 불가능한 환경 변화로 인한 작물 품질 저하 및 생산량 감소.",
                "solution": "IoT 센서 데이터 기반 생산량 예측 및 환경 제어 AI 시스템 구축. 최적 생육 환경 자동 조절 알고리즘 적용.",
                "metrics": [("생산량", "+30%"), ("품질 균일도", "95%"), ("에너지 효율", "+25%")]
            }
        }
    },
}

# 기본값 설정 (Fallback)
DEFAULT_INDUSTRY = "의료 (병원/클리닉)"

COMPANY_HISTORY = [
    ("v1.0 (2023.01)", "프로젝트 '오메가' 시작 - 데이터 마이닝 및 검색 알고리즘 역설계(Reverse Engineering) 성공."),
    ("v2.0 (2024.05)", "Veritas Clinical Engine 개발 완료 - 의료 분야 상담 자동화 및 효율화 시스템 구축."),
    ("v3.0 (2024.11)", "IMD Insight 플랫폼 론칭 - 법률/고위험 시장 진단 및 리드 생성 자동화."),
    ("v4.0 (2025.03)", "초개인화 커머스 AI 솔루션 상용화 및 AgriTech/제조 분야 확장."),
    ("v5.0 (Current)", "NEXUS AI 아키텍처 완성 - 전 산업군 비즈니스 최적화 시스템 통합.")
]

# ---------------------------------------
# 2. State & Helper Functions
# ---------------------------------------
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'temp_input' not in st.session_state:
    st.session_state.temp_input = None

AI_AVATAR = "✨"
USER_AVATAR = "👤"

# 안정화된 타이핑 함수 (버그 수정 버전)
def type_writer(text, speed=0.02):
    placeholder = st.empty()
    display_text = ""
    try:
        for char in text:
            display_text += char
            placeholder.markdown(display_text + "▍")
            time.sleep(speed)
    finally:
        placeholder.markdown(display_text)
    return display_text

# 메시지 저장 (애니메이션 제어 플래그 포함)
def bot_say(content, html=False):
    st.session_state.messages.append({"role": "assistant", "content": content, "html": html, "animated": False})

def user_say(content):
    st.session_state.messages.append({"role": "user", "content": content, "animated": True})

# ---------------------------------------
# 3. Main Interface & Rendering Logic (★핵심: 렌더링 분리★)
# ---------------------------------------

# [Header]
st.markdown("<h1 style='text-align: center; font-family: serif; margin-bottom: 5px;'>NEXUS AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:14px; color:#555; letter-spacing: 2px;'>THE ARCHITECTURE OF DOMINANCE</p>", unsafe_allow_html=True)
st.divider()

# [STEP 0: Init]
if st.session_state.step == 0:
    # [Persona: Authoritative & Cynical]
    msg = "NEXUS 활성화.\n\n우리는 웹사이트나 챗봇 따위를 만들지 않습니다. 우리는 비즈니스를 지배할 지능형 아키텍처를 설계합니다.\n\n당신의 비즈니스는 비효율로 인해 죽어가고 있습니다. 원인을 분석하고 우리의 솔루션을 제시하겠습니다.\n\n당신이 속한 산업군을 선택하십시오."
    bot_say(msg)
    st.session_state.step = 1

# [Rendering Logic: 안정화된 애니메이션 처리]
# 로직 처리 후 재실행되면 이 부분이 실행되어 애니메이션을 안정적으로 처리함.
for i, msg in enumerate(st.session_state.messages):
    avatar = AI_AVATAR if msg["role"] == "assistant" else USER_AVATAR
    with st.chat_message(msg["role"], avatar=avatar):
        
        is_last_message = (i == len(st.session_state.messages) - 1)
        
        if msg["role"] == "assistant" and not msg.get("animated") and is_last_message:
            if msg.get("html"):
                # HTML은 애니메이션 없이 즉시 출력 (코드 노출 방지)
                st.markdown(msg["content"], unsafe_allow_html=True)
            else:
                # 텍스트는 타이핑 애니메이션 실행
                type_writer(msg["content"])
            msg["animated"] = True
        else:
            # 이전 메시지 또는 유저 메시지는 즉시 출력
            if msg.get("html"):
                st.markdown(msg["content"], unsafe_allow_html=True)
            else:
                st.markdown(msg["content"])

# ---------------------------------------
# 4. Dynamic Interaction Area (Bottom)
# ---------------------------------------

# [STEP 1: Industry Selection]
if st.session_state.step == 1:
    st.markdown("<p style='font-size:12px; color:#666; margin-bottom:10px; letter-spacing: 1.5px;'>SELECT INDUSTRY</p>", unsafe_allow_html=True)
    
    industries = list(DATA_MATRIX.keys())
    # 버튼 레이아웃 조정 (최대 3열로 표시)
    cols = st.columns(min(len(industries), 3))
    
    for i, industry in enumerate(industries):
        if cols[i % 3].button(industry):
            st.session_state.temp_input = industry
            st.rerun()

# [STEP 2: Pain Point Selection]
if st.session_state.step == 2:
    industry = st.session_state.user_data.get('industry', DEFAULT_INDUSTRY)
    st.markdown(f"<p style='font-size:12px; color:#666; margin-bottom:10px; letter-spacing: 1.5px;'>SELECT BOTTLENECK IN {industry}</p>", unsafe_allow_html=True)
    
    pain_points = DATA_MATRIX.get(industry, {}).get('pain_points', [])
    
    if pain_points:
        cols = st.columns(min(len(pain_points), 3))
        for i, point in enumerate(pain_points):
            if cols[i % 3].button(point):
                st.session_state.temp_input = point
                st.rerun()

# [STEP 3: User Choice (History vs Consultation)]
if st.session_state.step == 3:
    st.markdown("<p style='font-size:12px; color:#666; margin-bottom:10px; letter-spacing: 1.5px;'>SELECT NEXT ACTION</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    if c1.button("NEXUS AI 연혁 보기"):
        st.session_state.temp_input = "History"
        st.rerun()

    if c2.button("즉시 아키텍처 도입 상담"):
        st.session_state.temp_input = "Consultation"
        st.rerun()

# [Input Handling: 로직 처리]
input_disabled = True # 이 홈페이지는 채팅 입력을 사용하지 않음 (버튼 기반)
st.chat_input(disabled=input_disabled)

# 버튼 입력(temp_input) 처리
if st.session_state.temp_input:
    prompt = st.session_state.temp_input
    st.session_state.temp_input = None # 사용 후 초기화
    
    user_say(prompt)

    # [STEP 1 -> 2: Industry Selected]
    if st.session_state.step == 1:
        industry = prompt
        if industry not in DATA_MATRIX:
             industry = DEFAULT_INDUSTRY # Fallback
        
        st.session_state.user_data['industry'] = industry

        # [Thinking Visualization]
        with st.status(f"산업 데이터 로드 중: {industry}", expanded=False) as status:
            time.sleep(0.8)
            status.update(label="로드 완료.", state="complete", expanded=False)

        resp = f"[{industry}] 분야 확인.\n\n현재 귀사가 직면한 가장 치명적인 병목 현상(Bottleneck)은 무엇입니까? 선택하십시오."
        bot_say(resp)
        st.session_state.step = 2
        st.rerun()

    # [STEP 2 -> 3: Pain Point Selected & Case Study Presentation]
    elif st.session_state.step == 2:
        pain_point = prompt
        st.session_state.user_data['pain_point'] = pain_point
        industry = st.session_state.user_data.get('industry', DEFAULT_INDUSTRY)
        
        # 케이스 데이터 찾기
        industry_data = DATA_MATRIX.get(industry)
        case = industry_data.get('cases', {}).get(pain_point)
        
        # Fallback: 매칭되는 케이스가 없으면 해당 산업의 첫 번째 케이스 사용
        if not case and industry_data.get('cases'):
             case = list(industry_data.get('cases').values())[0]

        if case:
            # [Thinking Visualization - The Core Analysis]
            with st.status("NEXUS 엔진 분석 실행 중...", expanded=True) as status:
                st.write(f"🔍 {industry} 분야 벤치마크 데이터 분석...")
                time.sleep(1.5)
                st.write(f"⚙️ '{pain_point}' 해결을 위한 AI 통합 시뮬레이션...")
                time.sleep(2.0)
                st.write("💡 잠재적 ROI 계산 및 성공 사례 매핑...")
                time.sleep(1.0)
                status.update(label="분석 완료. 솔루션 도출.", state="complete", expanded=False)

            # Diagnosis Message
            msg1 = f"분석 완료.\n\n귀사의 문제는 '{case['problem']}' 때문입니다.\n\n우리는 이 문제를 이미 정복했습니다. {case['title']} 사례를 제시합니다."
            bot_say(msg1)

            # Case Study Card (HTML)
            metrics_html = ""
            for label, value in case['metrics']:
                metrics_html += f"""
                <div class='metric'>
                    <div class='metric-value'>{value}</div>
                    <div class='metric-label'>{label}</div>
                </div>
                """

            case_html = f"""
            <div class='case-study-card'>
                <div class='label-small'>PROVEN ARCHITECTURE</div>
                <div class='case-title'>{case['title']}</div>
                <p><strong>솔루션 개요:</strong> {case['solution']}</p>
                <div class='metric-container'>
                    {metrics_html}
                </div>
            </div>
            """
            bot_say(case_html, html=True)
            
            # Follow-up Message
            msg2 = f"이것이 우리의 증명 방식입니다. 단순한 AI 도입이 아닌, 비즈니스 프로세스 자체를 재설계하는 것.\n\n우리의 진화 과정(연혁)이 궁금하십니까, 아니면 즉시 당신의 비즈니스에 이 아키텍처를 도입하고 싶습니까?"
            bot_say(msg2)

            st.session_state.step = 3
            st.rerun()

    # [STEP 3 -> 4: History or Consultation]
    elif st.session_state.step == 3:
        action = prompt

        if "연혁" in action:
            # [Thinking Visualization]
            with st.status("시스템 진화 로그 로드 중...", expanded=False) as status:
                time.sleep(0.5)
                status.update(label="로드 완료.", state="complete", expanded=False)

            # History Display (HTML)
            history_html = "<div class='history-section'><div class='label-small'>THE EVOLUTION LOGS</div>"
            for version, event in COMPANY_HISTORY:
                history_html += f"""
                <div style='display: flex; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid #222;'>
                    <div style='width: 120px; color: #D4AF37; font-weight: bold;'>{version}</div>
                    <div style='flex: 1; color: #FFF;'>{event}</div>
                </div>
                """
            history_html += "</div>"
            bot_say(history_html, html=True)
            
            msg = "우리는 멈추지 않고 진화해왔습니다. 이제 당신의 차례입니다. 상담을 신청하십시오."
            bot_say(msg)
            
            st.session_state.step = 4 # Go to Consultation
            st.rerun()

        elif "상담" in action:
            # 다음 단계에서 메시지 출력
            st.session_state.step = 4
            st.rerun()


# [STEP 4: Lead Capture (The CTA)]
if st.session_state.step == 4:
    # Consultation 시작 메시지 (History를 보고 오지 않은 경우에만 출력)
    if not any("상담을 신청하십시오." in m['content'] for m in st.session_state.messages if m['role'] == 'assistant'):
        msg = "현명한 판단입니다. 도입 컨설팅을 시작합니다. 정보를 입력하십시오."
        bot_say(msg)

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='label-small'>INITIATE CONSULTATION</div>", unsafe_allow_html=True)
    st.info("💡 NEXUS 아키텍처는 귀사의 기존 인프라(웹사이트, 앱, 내부 시스템)에 완벽하게 통합됩니다.")

    with st.form("consultation_form"):
        c1, c2 = st.columns(2)
        with c1: name = st.text_input("담당자명", placeholder="홍길동")
        with c2: company = st.text_input("회사명", placeholder="주식회사 OOO")
        
        contact = st.text_input("연락처", placeholder="010-XXXX-XXXX")
        budget = st.selectbox("예상 프로젝트 규모", ["미정 (상담 후 결정)", "1,000만원 ~ 5,000만원", "5,000만원 이상", "1억원 이상"])

        if st.form_submit_button("전략팀과 논의 시작"):
            if name and company and contact:
                # 여기에 DB 저장 로직 추가 (Google Sheets 등)
                # print(f"NEW LEAD: {name}, {company}, {contact}, {budget}, Data: {st.session_state.user_data}")
                
                # Final Message
                with st.status("요청 처리 중...", expanded=False) as status:
                    time.sleep(1.0)
                    status.update(label="처리 완료.", state="complete", expanded=False)
                
                st.success("접수 완료. NEXUS 수석 아키텍트가 24시간 내에 분석 데이터를 기반으로 연락드립니다. 비효율을 제거할 준비를 하십시오.")
                st.session_state.step = 5 # End state
            else:
                st.warning("필수 정보를 입력하십시오.")
